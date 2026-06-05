# WCS 技能仓库

WCS（Wind Code Standard）是面向 AI 驱动开发的可复用流程技能。它通过核心文档基线、开发前置门禁、先验证后提交、结构化交接等要求，在不同仓库中统一协作方式。

## 仓库内容

- `wcs-cn/`：中文版技能定义与维护流程，当前默认使用这一套
- `docs/`：本仓库的状态、规划、日志与维护说明
- `references/`：WCS 使用的模板文件

## 核心文件

- `docs/project_index.yaml`：YAML 中枢索引，AI 启动任务时首先阅读此文件
- `wcs-cn/SKILL.md`：WCS 中文版技能定义

## 使用方式

1. 将 `wcs-cn/` 复制到本地 Hermes skills 目录
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
- [协作提示](docs/prompt.txt)
- [重构讨论](docs/discussions/2026-06-05-three-tier-docs-architecture.md)

## 许可证

MIT
