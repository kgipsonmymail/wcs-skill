# WCS 技能仓库

WCS（Wind Code Standard）是面向 AI 驱动开发的可复用流程技能。它通过核心文档基线、开发前置门禁、先验证后提交、结构化交接等要求，在不同仓库中统一协作方式。

## 仓库结构

```
wcs-skill/                ← git 仓库根目录
├── wcs-cn/              ← 实际被加载的 skill（name: wcs-cn）
│   ├── SKILL.md
│   ├── references/       ← skill 使用的模板文件
│   ├── assets/
│   └── scripts/
├── docs/                 ← WCS 自身迭代的文档（优化过程记录）
└── scripts/              ← 辅助脚本（skill 索引、结构扫描等）
```

## 核心文件

- `wcs-cn/SKILL.md`：WCS 中文版技能定义
- `docs/project_index.yaml`：WCS 自身维护用的 YAML 中枢索引

## 安装与使用

1. 将整个 `wcs-skill/` 目录作为 skill 安装到 Hermes
2. 在开始新功能、修复缺陷、接手他人工作或做发布整理时，触发 `wcs-cn`
3. AI 会先读取 `docs/project_index.yaml` 了解项目上下文，然后按流程执行

## 文档导航

- [YAML 中枢索引](docs/project_index.yaml) — 项目上下文入口
- [开发规划](docs/dev_plan.md)
- [功能清单](docs/features.md)
- [项目状态](docs/project_status.md)
- [仓库结构](docs/structure.md)
- [开发日志](docs/dev_log.md)
- [问题手册](docs/error_book.md)
- [代码规范](docs/CODING_STANDARDS.md)
- [维护流程](docs/workflow.md)
- [用户输入记录](docs/uin.md)
- [重构讨论](docs/discussions/)

## 许可证

MIT
