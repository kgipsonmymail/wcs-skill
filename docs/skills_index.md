# Skills 索引

> 本文件由 `scripts/scan_skills.py` 自动生成，请勿手动编辑。

## 核心数据

- **生成脚本**：`scripts/scan_skills.py`
- **数据文件**：`docs/skills_index.yaml`
- **扫描范围**：`~/.hermes/skills/` 下所有 skill 目录

## 快速查看

```bash
# 查看完整索引
cat docs/skills_index.yaml

# 重建索引（推荐每周一次）
python3 scripts/scan_skills.py

# 纯 stdlib 模式（无 PyYAML 依赖）
python3 scripts/scan_skills.py --no-yaml

# 指定输出路径
python3 scripts/scan_skills.py -o ./my_index.yaml
```

## 分类说明

| 分类 | 说明 |
|------|------|
| `core` | 核心 skill（WCS、systematic-debugging 等），始终可用 |
| `project` | 项目专属 skill（mediary、video-daily 等） |
| `tool` | 工具类 skill（dogfood、context-query 等） |
| `platform` | 平台/系统类 skill（github、mcp、mlops 等） |

## 已知结构问题

- `wcs-cn/` 是 `wcs-skill/` 的子目录，其 SKILL.md 没有被扫描到（因为扫描以 `~/.hermes/skills/` 为顶层）
- 临时方案：`wcs-skill/SKILL.md`（name: wcs）代表了整个 wcs-skill 仓库
- 建议：长期将 `wcs-cn/` 移为顶层 skill `wcs-cn/`（与 `wcs-skill/` 平级），避免结构歧义

## 使用说明

- AI 在新项目 onboarding 时可参考此索引决定激活哪些 skill
- 运行脚本重建索引：
  ```bash
  python3 scripts/scan_skills.py           # 带 PyYAML（格式更好）
  python3 scripts/scan_skills.py --no-yaml  # 纯 stdlib
  python3 scripts/scan_skills.py -o /path/to/output.yaml  # 指定输出路径
  ```

## 维护说明

- `skills_index.yaml` 由 `scripts/scan_skills.py` 自动生成
- 每次 WCS 开发新任务前，建议运行一次确保索引最新
- 也可定期 cron 化：每周日凌晨 3 点自动重建并 commit
