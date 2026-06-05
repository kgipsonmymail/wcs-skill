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
- 提供 YAML 中枢索引，支持三层架构（skill → doc → file）
- **新增（Module 1-7）**：16 种任务上下文、15 种任务状态触发规则、本地 Skill 索引脚本、Doc 同步检查清单、SQLite 结构索引实验、Errorbook 释放机制、Docs 架构评估

## 当前约束

- 中枢索引 `project_index.yaml` 需要随项目演进手动维护
- Skill 索引脚本已实现（`scripts/scan_skills.py`），但需要定期运行以保持最新
- SQLite 结构索引为可选增强，不是默认方案

## 维护说明

- 查看已完成与待开发事项，优先看 [`docs/dev_plan.md`](./dev_plan.md)
- 查看已经落地的能力范围，查看 [`docs/features.md`](./features.md)
- 查看重构讨论记录，查看 [`docs/discussions/2026-06-05-three-tier-docs-architecture.md`](./discussions/2026-06-05-three-tier-docs-architecture.md)
