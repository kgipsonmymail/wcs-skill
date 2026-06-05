# 基线文档模板（跨项目通用）

本模板用于在任意仓库中建立稳定、最小、可维护的文档体系。

## 必备文件与最小章节

### `README.md`
- 项目概述
- 快速上手
- 常用命令
- 指向 `docs/` 的链接地图

### `docs/project_status.md`
- 技术栈与架构快照
- 已实现的模块与当前能力
- 运行时状态、约束条件、已知限制

### `docs/structure.md`
- 目录树（顶层与关键子模块）
- 主要文件/模块的职责映射
- 维护者导航提示

### `docs/dev_plan.md`
- 进行中与待办任务
- 优先级、负责人（可选）、目标里程碑
- 风险或依赖说明

### `docs/dev_log.md`
- 日期与任务标题
- 变更内容
- 验证依据
- 回滚备注（如有）

### `docs/error_book.md`
- 现象
- 根因
- 失败尝试（可选但建议）
- 最终修复与预防措施

### `docs/features.md`
- 按模块/领域划分的能力列表
- 当前状态（`done` / `partial` / `planned`）
- 指向实现文档或关键文件的链接

### `docs/CODING_STANDARDS.md`
- 必须遵守的规则
- 命名与结构规范
- 测试与提交策略
- 文档更新策略

### `docs/workflow.md`
- 从受理到交接的端到端流程
- 质量门禁
- 角色与协作约定

### `docs/prompt.txt`（AI 工作流项目建议保留）
- 稳定的提示约束
- 多 AI 协作原则

## 粒度规则

- `README.md` 保持简洁、只做导航
- 详细内容放在专用 doc 中，用链接引用
- 避免跨文件重复同一段落
- 日志和计划优先用列表记录

## 更新触发规则

- 架构/文件变更 → 更新 `docs/structure.md` 和 `docs/project_status.md`
- 新增或变更能力 → 更新 `docs/features.md` 和 `docs/project_status.md`
- 缺陷修复 → 更新 `docs/error_book.md` 和 `docs/dev_log.md`
- 任何交付变更 → 更新 `docs/dev_log.md`
