# WCS 技能仓库

WCS（Wind Code Standard）是面向 AI 驱动开发的可复用流程技能。它通过核心文档基线、开发前置门禁、先验证后提交、结构化交接等要求，在不同仓库中统一协作方式。

## 仓库内容

- `wcs-cn/`：中文版技能定义与维护流程，当前默认使用这一套
- `wcs/`：英文版技能目录，仓库保留但日常维护可忽略
- `docs/`：本仓库的状态、规划、日志与维护说明

## 使用方式

1. 将 `wcs-cn/` 复制到本地 Codex skills 目录，并保持目录名为 `wcs-cn`。
2. 在开始新功能、修复缺陷、接手他人工作或做发布整理时，直接触发 `wcs-cn`。
3. 按中文流程完成前置门禁、实现、验证、文档同步和交接。

## 说明

- 本仓库由本地 `wcs` / `wcs-cn` 技能整理发布而来。
- 目前文档维护默认以 `wcs-cn` 为主；英文版目录仅作为兼容保留。

## 文档导航

- [开发规划](docs/dev_plan.md) - 当前主规划面板，区分已完成、下一步和待开发
- [功能清单](docs/features.md) - 已落地能力索引
- [项目状态](docs/project_status.md)
- [仓库结构](docs/structure.md)
- [开发日志](docs/dev_log.md)
- [问题手册](docs/error_book.md)
- [代码规范](docs/CODING_STANDARDS.md)
- [维护流程](docs/workflow.md)
- [协作提示](docs/prompt.txt)

## 许可证

MIT
