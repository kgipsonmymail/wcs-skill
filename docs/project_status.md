# 项目状态

## 当前快照

- 项目：`wcs-skill` 开源技能仓库
- 类型：Hermes 技能仓库
- 当前默认维护对象：[`wcs-cn/SKILL.md`](../wcs-cn/SKILL.md)
- YAML 中枢索引：[`docs/project_index.yaml`](./project_index.yaml)
- 规划主文档：[`docs/dev_plan.md`](./dev_plan.md)
- 能力索引：[`docs/features.md`](./features.md)

## 当前能力

- 提供 WCS 中文版流程定义，可用于功能开发、缺陷修复、重构与文档维护
- 提供项目基线文档模板
- 提供从受理、实施、验证到交接的流程清单
- 提供可复用的代码规范模板
- **新增**：YAML 中枢索引，支持三层架构（skill → doc → file）

## 当前约束

- `wcs/` 英文版目录已删除（2026-06-05）
- 中枢索引 `project_index.yaml` 需要随项目演进手动维护
- 当前脚本能力仍以占位目录为主，尚无实际自动化工具

## 维护说明

- 查看已完成与待开发事项，优先看 [`docs/dev_plan.md`](./dev_plan.md)
- 查看已经落地的能力范围，查看 [`docs/features.md`](./features.md)
- 查看重构讨论记录，查看 [`docs/discussions/2026-06-05-three-tier-docs-architecture.md`](./discussions/2026-06-05-three-tier-docs-architecture.md)
