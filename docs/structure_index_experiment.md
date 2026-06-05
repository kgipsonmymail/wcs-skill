# 目录结构索引：SQLite vs YAML 实验记录

## 实验日期

2026-06-05

## 结论

**YAML 索引更适合作为中枢文档，SQLite 作为补充工具。**

### YAML 作为中枢索引的理由

1. **人类可读**：直接 cat/view，无需任何工具
2. **版本控制友好**：git diff 有意义，能 merge
3. **无需工具链**：任何 AI 都能直接解析
4. **语义丰富**：可携带 purpose、tags、read_when 等元数据
5. **WCS 定位决定**：YAML 中枢是 AI 的"导航文件"，不是数据库

### SQLite 作为补充的理由

1. **查询速度快**：万级文件仍是毫秒级
2. **复杂查询**：按扩展名、修改时间、模块统计等
3. **实验结论**：本次测试 321 项，扫描耗时 0.04s

### 最终决策

| 用途 | 方案 |
|------|------|
| 中枢索引（task_contexts 映射） | YAML (`project_index.yaml`) — 必须 |
| 文件定位（快速找文件） | `docs/structure.md`（手写概要）— 够用 |
| 大型项目结构分析 | SQLite (`docs/structure.db`) — 可选增强 |
| Skill 索引 | YAML (`docs/skills_index.yaml`) — 自动生成 |

## 实验数据

```
扫描范围：wcs-skill 仓库（321 items）
扫描耗时：0.04s
DB 大小：140 KB
```

## scripts/scan_structure.py 使用场景

```bash
# 大型项目（>1000 文件）建议用 SQLite
python3 scripts/scan_structure.py /path/to/large-project

# 小型项目，手写 structure.md 足够
```

## 何时考虑 SQLite 增强

- 项目文件数 > 1000
- 需要按扩展名/模块统计
- 需要频繁查找"最近修改的文件"
- 需要按模块导出文件列表
