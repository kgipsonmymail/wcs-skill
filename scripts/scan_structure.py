#!/usr/bin/env python3
"""
scan_structure.py - 扫描项目目录，生成结构索引 SQLite 数据库

用途：
  - 探索 SQLite vs YAML 的文件索引效果
  - 支持快速文件定位、模块关联查询
  - 0 依赖：纯 Python stdlib + sqlite3

输出：docs/structure.db

使用方法：
  python3 scan_structure.py /path/to/project           # 扫描项目
  python3 scan_structure.py /path/to/project -o out.db  # 指定输出

测试对比：
  - 同样项目，用 YAML 索引需要多久？
  - 用 SQLite 查询文件定位需要多久？
  - YAML 可读性 vs SQLite 查询能力，哪个更实用？
"""

import os
import sys
import sqlite3
import argparse
import time
from pathlib import Path
from typing import Optional


def ensure_tables(conn: sqlite3.Connection) -> None:
    """创建数据库表"""
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            size INTEGER,
            mtime REAL,
            extension TEXT,
            is_dir INTEGER DEFAULT 0,
            relative_path TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            file_count INTEGER DEFAULT 0
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS file_module (
            file_id INTEGER,
            module_id INTEGER,
            PRIMARY KEY (file_id, module_id),
            FOREIGN KEY (file_id) REFERENCES files(id),
            FOREIGN KEY (module_id) REFERENCES modules(id)
        )
    """)
    c.execute("CREATE INDEX IF NOT EXISTS idx_files_ext ON files(extension)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_files_path ON files(path)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_files_mtime ON files(mtime)")
    conn.commit()


def guess_module(file_path: Path, root: Path) -> Optional[str]:
    """根据路径猜测模块名"""
    rel = str(file_path.relative_to(root))
    parts = Path(rel).parts
    if not parts:
        return None
    # 顶层目录作为模块名
    top = parts[0]
    # 跳过常见的非模块目录
    skip = {'.git', '.github', 'node_modules', '__pycache__', '.venv',
            'venv', 'dist', 'build', '.idea', '.vscode', 'assets', 'static',
            'public', 'coverage', '.pytest_cache', '.mypy_cache'}
    if top in skip:
        return None
    return top


def scan_directory(root: Path, conn: sqlite3.Connection, verbose: bool = False) -> int:
    """扫描目录树并写入 SQLite"""
    c = conn.cursor()
    count = 0
    errors = 0

    for entry in root.rglob('*'):
        try:
            stat = entry.stat()
            rel_path = str(entry.relative_to(root))
            ext = entry.suffix.lower() if entry.is_file() else None
            is_dir = 1 if entry.is_dir() else 0

            c.execute("""
                INSERT OR REPLACE INTO files (path, size, mtime, extension, is_dir, relative_path)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (str(entry), stat.st_size, stat.st_mtime, ext, is_dir, rel_path))

            # 猜测模块并关联
            module = guess_module(entry, root)
            if module and entry.is_file():
                c.execute("SELECT id FROM modules WHERE name = ?", (module,))
                row = c.fetchone()
                if row:
                    module_id = row[0]
                else:
                    c.execute("INSERT INTO modules (name) VALUES (?)", (module,))
                    module_id = c.lastrowid
                c.execute("SELECT id FROM files WHERE path = ?", (str(entry),))
                file_id = c.fetchone()[0]
                try:
                    c.execute("INSERT OR IGNORE INTO file_module (file_id, module_id) VALUES (?, ?)",
                              (file_id, module_id))
                except Exception:
                    pass

            count += 1
            if verbose and count % 500 == 0:
                print(f"  scanned {count} items...")
        except (OSError, PermissionError, sqlite3.Error) as e:
            errors += 1
            if verbose and errors <= 5:
                print(f"  skip {entry}: {e}", file=sys.stderr)
            continue

    # 更新模块文件计数
    c.execute("""
        UPDATE modules SET file_count = (
            SELECT COUNT(*) FROM file_module fm WHERE fm.module_id = modules.id
        )
    """)
    conn.commit()
    return count


def query_demo(conn: sqlite3.Connection) -> None:
    """演示查询（用于对比 YAML）"""
    c = conn.cursor()
    print("\n=== SQLite 查询演示 ===")

    # 按模块统计文件数
    print("\n[模块文件统计]")
    c.execute("SELECT name, file_count FROM modules ORDER BY file_count DESC LIMIT 10")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]} files")

    # 按扩展名统计
    print("\n[文件类型统计]")
    c.execute("""
        SELECT extension, COUNT(*) as cnt
        FROM files
        WHERE extension IS NOT NULL AND is_dir = 0
        GROUP BY extension
        ORDER BY cnt DESC
        LIMIT 10
    """)
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]} files")

    # 最近修改的 10 个文件
    print("\n[最近修改的 10 个文件]")
    c.execute("""
        SELECT relative_path, mtime FROM files
        WHERE is_dir = 0
        ORDER BY mtime DESC
        LIMIT 10
    """)
    for row in c.fetchall():
        import datetime
        dt = datetime.datetime.fromtimestamp(row[1]).strftime('%Y-%m-%d %H:%M')
        print(f"  {dt}  {row[0]}")

    # 查找特定文件类型
    print("\n[查找 .py 文件 (LIMIT 5)]")
    c.execute("SELECT relative_path FROM files WHERE extension = '.py' LIMIT 5")
    for row in c.fetchall():
        print(f"  {row[0]}")


def main():
    parser = argparse.ArgumentParser(description="Scan project structure into SQLite")
    parser.add_argument("project", type=str, help="项目目录路径")
    parser.add_argument("-o", "--output", type=str,
                        default=None, help="输出 SQLite 文件路径")
    parser.add_argument("--root", type=str, default=None,
                        help="项目根目录（用于计算相对路径，默认=project）")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.exists():
        print(f"Error: {project} does not exist", file=sys.stderr)
        sys.exit(1)

    root = Path(args.root).resolve() if args.root else project
    output = Path(args.output) if args.output else project / "docs" / "structure.db"

    # 确保输出目录
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Scanning: {project}")
    print(f"Output:   {output}")

    conn = sqlite3.connect(str(output))
    ensure_tables(conn)

    # 如果已存在，清空旧数据（保留表结构）
    conn.execute("DELETE FROM file_module")
    conn.execute("DELETE FROM files")
    conn.execute("DELETE FROM modules")

    t0 = time.time()
    count = scan_directory(project, conn, verbose=args.verbose)
    elapsed = time.time() - t0

    print(f"\nScanned {count} items in {elapsed:.2f}s")
    print(f"DB size: {output.stat().st_size / 1024:.1f} KB")

    query_demo(conn)
    conn.close()

    print(f"\nDone. Open with: sqlite3 {output}")


if __name__ == "__main__":
    main()
