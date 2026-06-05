# 仓库结构

## 版本说明

本仓库是 **Git 版本**（wcs-skill），用于 WCS 自身的开发和迭代。

**部署版本**是 `wcs-cn/SKILL.md`，是 AI 实际执行任务时加载的 skill。部署版应仅包含 `SKILL.md`、`references/` 和执行所需的最小 docs 集合，不包含本 git 版本中的讨论/规划/实验类文档。

## 顶层目录

```
wcs-skill/
├── wcs-cn/               # 中文技能主目录（当前维护版）
├── docs/                 # 仓库自身文档
│   ├── project_index.yaml    # YAML 中枢索引（Module 1）
│   ├── task_states.md        # 任务状态触发机制（Module 2）
│   ├── skills_index.yaml     # 本地 skill 索引（Module 3，自动生成）
│   ├── skills_index.md       # skill 索引说明
│   ├── doc_sync_checklist.md # Doc 同步检查清单（Module 4）
│   ├── structure_index_experiment.md  # SQLite vs YAML 实验记录（Module 5）
│   ├── errorbook_release.md  # Errorbook 释放机制（Module 6）
│   ├── docs_architecture_review.md   # Docs 架构扩展评估（Module 7）
│   ├── discussions/           # 重构讨论存档
│   ├── project_status.md
│   ├── structure.md
│   ├── dev_plan.md
│   ├── dev_log.md
│   ├── features.md
│   ├── error_book.md
│   ├── CODING_STANDARDS.md
│   ├── workflow.md
│   └── prompt.txt
├── references/           # WCS 模板
│   ├── core_docs_template.md
│   ├── workflow_checklists.md
│   ├── coding_standard_template.md
│   └── project_index_template.yaml  # 中枢文档模板
├── scripts/              # 自动化脚本（Module 3 & 5）
│   ├── scan_skills.py       # 扫描本地 skills 生成索引
│   └── scan_structure.py     # 扫描项目结构生成 SQLite
├── SKILL.md              # 主技能定义（根目录，name: wcs）
├── README.md             # 仓库入口
└── LICENSE              # MIT 许可证
```

## 参考文件

- `references/core_docs_template.md`：基线文档模板
- `references/coding_standard_template.md`：通用代码规范模板
- `references/workflow_checklists.md`：端到端流程清单
- `references/project_index_template.yaml`：中枢文档模板

## 维护导航

| 维护目标 | 维护文件 |
|---------|---------|
| 修改 WCS 行为 | `wcs-cn/SKILL.md` |
| 修改中枢索引结构 | `docs/project_index.yaml` |
| 更新 Module 定义 | `docs/dev_plan.md` |
| 记录维护动作 | `docs/dev_log.md` |
| 重建 skill 索引 | `python3 scripts/scan_skills.py` |
| 重建结构索引 | `python3 scripts/scan_structure.py .` |
