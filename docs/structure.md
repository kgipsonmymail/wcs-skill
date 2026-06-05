# 仓库结构

## 顶层目录

```
wcs-skill/
├── wcs-cn/               # 中文技能主目录（当前维护版）
├── docs/                 # 仓库自身文档
│   ├── project_index.yaml  # YAML 中枢索引
│   ├── discussions/        # 重构讨论存档
│   ├── project_status.md
│   ├── structure.md
│   ├── dev_plan.md
│   ├── dev_log.md
│   ├── features.md
│   ├── error_book.md
│   ├── CODING_STANDARDS.md
│   ├── workflow.md
│   └── prompt.txt
├── references/            # WCS 模板
│   ├── core_docs_template.md
│   ├── workflow_checklists.md
│   ├── coding_standard_template.md
│   └── project_index_template.yaml  # 中枢文档模板
├── SKILL.md              # 主技能定义
├── README.md             # 仓库入口
└── LICENSE              # MIT 许可证
```

## 参考文件

- `references/core_docs_template.md`：基线文档模板
- `references/coding_standard_template.md`：通用代码规范模板
- `references/workflow_checklists.md`：端到端流程清单
- `references/project_index_template.yaml`：中枢文档模板

## 维护导航

- 修改中文技能行为时，维护 `wcs-cn/SKILL.md`
- 修改中枢索引时，更新 `docs/project_index.yaml`
- 记录仓库级维护动作时，更新 `docs/dev_log.md`
- 维护公开说明与导航时，更新 `README.md`
