#!/usr/bin/env python3
"""
scan_skills.py - 扫描 ~/.hermes/skills/ 目录，生成 skills_index.yaml

用途：
  - AI 启动时快速了解本地有哪些 skill 可用
  - 支持 project_index.yaml 的 skills 层动态更新
  - 0 依赖：纯 Python stdlib + yaml（PyYAML）

输出：docs/skills_index.yaml

使用方法：
  python scan_skills.py
  python scan_skills.py --output ./my_skills.yaml
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import Optional, Dict, List, Any

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


SKILLS_DIR = Path.home() / ".hermes" / "skills"
OUTPUT_PATH = Path(__file__).parent.parent / "docs" / "skills_index.yaml"


def extract_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """从 markdown 文件提取 YAML frontmatter，返回 {name, description, ...}"""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        if YAML_AVAILABLE:
            return yaml.safe_load(match.group(1)) or {}
        else:
            # 纯 stdlib 手动解析（只支持简单的 key: value）
            result = {}
            for line in match.group(1).split('\n'):
                line = line.strip()
                if ':' in line:
                    key, val = line.split(':', 1)
                    result[key.strip()] = val.strip().strip('"').strip("'")
            return result
    except Exception:
        return {}


def scan_single_skill(skill_dir: Path) -> Optional[Dict]:
    """扫描单个 skill 目录（顶层 SKILL.md）"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding='utf-8')
    fm = extract_yaml_frontmatter(content)

    return {
        "name": fm.get("name", skill_dir.name),
        "description": fm.get("description", ""),
        "path": str(skill_dir.relative_to(SKILLS_DIR)),
        "type": "skill",
        "category": classify_skill(skill_dir.name),
    }


def scan_group_skill(skill_dir: Path) -> Optional[Dict]:
    """扫描分组 skill 目录（顶层是 DESCRIPTION.md）"""
    desc_md = skill_dir / "DESCRIPTION.md"
    if not desc_md.exists():
        return None

    content = desc_md.read_text(encoding='utf-8')
    fm = extract_yaml_frontmatter(content)

    # 找所有子 skill
    sub_skills = []
    for sub in skill_dir.iterdir():
        if sub.is_dir():
            sub_md = sub / "SKILL.md"
            if sub_md.exists():
                sub_content = sub_md.read_text(encoding='utf-8')
                sub_fm = extract_yaml_frontmatter(sub_content)
                sub_skills.append({
                    "name": sub_fm.get("name", sub.name),
                    "description": sub_fm.get("description", ""),
                    "path": str(sub.relative_to(SKILLS_DIR)),
                    "category": classify_skill(sub.name),
                })

    return {
        "name": fm.get("name", skill_dir.name),
        "description": fm.get("description", ""),
        "path": str(skill_dir.relative_to(SKILLS_DIR)),
        "type": "group",
        "category": "platform",  # 分组 skill 通常是平台相关的
        "sub_skills": sub_skills,
    }


def scan_implicit_group(skill_dir: Path) -> Optional[Dict]:
    """扫描隐性子目录分组（无 DESCRIPTION.md，但有子 SKILL.md）"""
    # 检查是否有子 SKILL.md
    sub_dirs = [d for d in skill_dir.iterdir() if d.is_dir()]
    sub_skills = []
    for sub in sub_dirs:
        sub_md = sub / "SKILL.md"
        if sub_md.exists():
            sub_content = sub_md.read_text(encoding='utf-8')
            sub_fm = extract_yaml_frontmatter(sub_content)
            sub_skills.append({
                "name": sub_fm.get("name", sub.name),
                "description": sub_fm.get("description", ""),
                "path": str(sub.relative_to(SKILLS_DIR)),
                "category": classify_skill(sub.name),
            })

    if not sub_skills:
        return None

    return {
        "name": skill_dir.name,
        "description": f"隐式分组：{skill_dir.name}",
        "path": str(skill_dir.relative_to(SKILLS_DIR)),
        "type": "group",
        "category": "tool",
        "sub_skills": sub_skills,
    }


def classify_skill(name: str) -> str:
    """根据 skill 名称分类"""
    # 核心 skill（始终需要）
    if name in ("wcs-cn", "wcs-skill", "systematic-debugging", "writing-plans"):
        return "core"
    # 项目 skill
    if name in ("mediary", "video-daily", "wind-projects", "video-daily-matrix",
                "character-consistency-testing", "minimax-image-consistency-testing",
                "minimax-quota-testing"):
        return "project"
    # 工具 skill
    if name in ("dogfood", "context-query", "mmx-cli", "plan",
                "requesting-code-review", "subagent-driven-development",
                "block-editor-rendering-debug", "hermes-usage-tips",
                "design-patterns", "development-thinking", "mediary-sensitive-info-cleanup",
                "mysql-cross-version-migration", "webhook-subscriptions", "godmode"):
        return "tool"
    # 平台/系统 skill
    if any(x in name for x in ("apple", "openhue", "himalaya", "xurl", "notion",
                                "google-workspace", "linear", "obsidian", "powerpoint",
                                "maps", "nano-pdf", "ocr-and-documents", "blogwatcher",
                                "arxiv", "llm-wiki", "polymarket", "minecraft-modpack-server",
                                "pokemon-player", "heartmula", "songsee", "gif-search",
                                "youtube-content", "manim-video", "p5js", "pixel-art",
                                "excalidraw", "architecture-diagram", "ascii-art",
                                "ascii-video", "baoyu-infographic", "ideation",
                                "songwriting-and-ai-music", "autonomous-ai-agents",
                                "claude-code-server-setup", "claude-code", "codex",
                                "opencode", "hermes-agent", "jupyter-live-kernel",
                                "github-auth", "github-repo-management", "github-pr-workflow",
                                "github-issues", "github-code-review", "codebase-inspection",
                                "huggingface-hub", "wechat-to-mediary", "dogfood")):
        return "platform"
    # 知识/研究 skill
    if any(x in name for x in ("mlops", "inference-sh", "data-science", "research",
                                "creative", "media", "smart-home", "social-media",
                                "note-taking", "productivity", "gaming", "email",
                                "feeds", "domain", "diagramming", "gifs", "inference-sh")):
        return "platform"
    return "tool"


def scan_all_skills() -> Dict:
    """扫描所有 skill 目录"""
    skills = []
    groups = []

    for entry in sorted(SKILLS_DIR.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith('.'):
            continue

        # 跳过自身仓库
        if entry.name == "wcs-skill":
            # 主 skill
            result = scan_single_skill(entry)
            if result:
                skills.append(result)
            continue

        # 尝试三种扫描方式
        result = scan_single_skill(entry)
        if result:
            skills.append(result)
            continue

        result = scan_group_skill(entry)
        if result:
            groups.append(result)
            continue

        result = scan_implicit_group(entry)
        if result:
            groups.append(result)

    return {"skills": skills, "groups": groups}


def build_index(scan_result: Dict) -> Dict:
    """将扫描结果构建为 skills_index.yaml 结构"""
    # 按 category 分组
    by_category = {}
    for skill in scan_result["skills"]:
        cat = skill.pop("category")
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(skill)

    # 对每个 group，展开 sub_skills 的 category
    for group in scan_result["groups"]:
        if "sub_skills" in group:
            for sub in group["sub_skills"]:
                cat = sub.pop("category", "tool")
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(sub)
            group.pop("sub_skills", None)

    return {
        "meta": {
            "generated_by": "scripts/scan_skills.py",
            "skills_dir": str(SKILLS_DIR),
            "total_skills": sum(len(v) for v in by_category.values()),
            "total_groups": len(scan_result["groups"]),
        },
        "by_category": by_category,
        "groups": scan_result["groups"],
    }


def main():
    parser = argparse.ArgumentParser(description="Scan skills and generate skills_index.yaml")
    parser.add_argument("--output", "-o", type=str, help="Output path (default: docs/skills_index.yaml)")
    parser.add_argument("--no-yaml", action="store_true", help="Use stdlib parser only (no PyYAML)")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else OUTPUT_PATH

    # 强制不使用 PyYAML（如果指定）
    global YAML_AVAILABLE
    if args.no_yaml:
        YAML_AVAILABLE = False

    if not YAML_AVAILABLE:
        print("PyYAML not available, using stdlib parser", file=sys.stderr)

    if not SKILLS_DIR.exists():
        print(f"Error: {SKILLS_DIR} does not exist", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning {SKILLS_DIR}...")
    scan_result = scan_all_skills()
    index = build_index(scan_result)

    # 确保输出目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if YAML_AVAILABLE:
        content = yaml.dump(index, allow_unicode=True, sort_keys=False, default_flow_style=False)
    else:
        # 纯 stdlib 输出（手动拼 YAML）
        content = stdlib_dump(index)

    output_path.write_text(content, encoding='utf-8')
    print(f"Written: {output_path}")
    print(f"Total skills: {index['meta']['total_skills']}")
    print(f"Total groups: {index['meta']['total_groups']}")
    for cat, items in index["by_category"].items():
        print(f"  [{cat}] {len(items)}")


def stdlib_dump(data, indent=0):
    """纯 stdlib YAML-like dumper（不依赖 PyYAML）"""
    lines = []
    prefix = "  " * indent
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{prefix}{k}:")
                lines.append(stdlib_dump(v, indent + 1))
            else:
                val = f'"{v}"' if isinstance(v, str) and (':' in v or '"' in v) else v
                lines.append(f"{prefix}{k}: {val}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                first = True
                for k, v in item.items():
                    if first:
                        if isinstance(v, (dict, list)):
                            lines.append(f"{prefix}- {k}:")
                            lines.append(stdlib_dump(v, indent + 2))
                        else:
                            lines.append(f"{prefix}- {k}: {v}")
                        first = False
                    else:
                        if isinstance(v, (dict, list)):
                            lines.append(f"{prefix}  {k}:")
                            lines.append(stdlib_dump(v, indent + 2))
                        else:
                            lines.append(f"{prefix}  {k}: {v}")
            else:
                lines.append(f"{prefix}- {item}")
    else:
        lines.append(f"{prefix}{data}")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
