# 核心文档模板（跨项目）

使用本模板在不同仓库间维持稳定的文档体系。

## 必备文件与最低章节

### `README.md`
- 项目概览
- 快速开始
- 常用命令
- 指向 `docs/` 的链接地图

### `docs/project_status.md`
- 技术栈与架构快照
- 已实现模块与当前能力
- 运行状态、约束与已知限制

### `docs/structure.md`
- 目录树（顶层与关键子模块）
- 主要文件/模块职责映射
- 维护者导航提示

### `docs/dev_plan.md`
- 进行中与待办任务
- 优先级、负责人（可选）、目标里程碑
- 风险或依赖说明

### `docs/dev_log.md`
- 日期与任务标题
- 变更内容
- 验证依据
- 必要时回滚说明

### `docs/error_book.md`
- 现象
- 根因
- 失败尝试（可选但建议）
- 最终修复与预防要点

### `docs/features.md`
- 按模块/领域列出的功能清单
- 当前状态（`done`、`partial`、`planned`）
- 指向实现文档或关键文件的链接

### `docs/CODING_STANDARDS.md`
- 必须遵守的规则
- 命名与结构规则
- 测试与提交策略
- 文档更新策略

### `docs/workflow.md`
- 从接受到交接的端到端流程
- 质量门禁
- 角色与协作约定

### `docs/prompt.txt`（可选，但 AI 协作密集时建议）
- 稳定的提示约束
- 跨 AI 代理的协作原则

## 粒度规则

- 保持 `README.md` 简洁、以导航为主
- 细节放在专门文档中，通过链接引用
- 避免在多个文件中重复同一段落
- 日志与计划优先用条目式记录

## 更新触发规则

- 架构/文件变更：更新 `docs/structure.md` 与 `docs/project_status.md`
- 新增或变更能力：更新 `docs/features.md` 与 `docs/project_status.md`
- 缺陷修复：更新 `docs/error_book.md` 与 `docs/dev_log.md`
- 任何已交付变更：更新 `docs/dev_log.md`
