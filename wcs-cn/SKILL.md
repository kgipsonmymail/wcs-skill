---
name: wcs-cn
description: 跨项目统一的代码规范技能：在实现任何新功能或修复缺陷前强制执行文档维护与开发前置门禁。本技能应在任意仓库中开始、继续或评审软件开发任务时使用。
---

# WCS（Wind Code Standard）中文版

## 定位

> WCS 是 AI 开发方法论框架。每个开发任务第一个激活它，由它分析任务、激活合适的 skill、引导阅读必要的 doc、定位需要的 file，在保证开发质量的前提下最快完成任务。WCS 通过在实践中不断总结经验来迭代自身。

## 何时使用

在以下任一情形下触发本技能：

- 在任意仓库中开始新功能
- 修复缺陷或回归问题
- 接续其他 AI 或工程师未完成的工作
- 准备提交或发布交接
- 审计项目文档与实现是否一致
- 接入新项目（onboarding）

## 核心规则

除非用户明确覆盖，否则执行以下全部规则。

1. 收到任务后，先读取 `docs/project_index.yaml`（或项目根目录的对应中枢文件）
2. 根据 `task_contexts` 匹配任务类型，激活对应的 skill 和 doc
3. 根据任务状态（Module 2: task_states.md）决定激活哪个规范子集
4. 写代码前先完成开发前置门禁
5. 仅在功能验证通过后再提交
6. 提交前按 `docs/doc_sync_checklist.md` 更新相关 doc
7. 产出简洁、可接续的交接说明

## 必备文档基线

WCS 部署版（`wcs-cn/`）本身不包含 `docs/`，只包含 `SKILL.md` 和 `references/`。

AI 在**目标项目**中维护以下基线文档。若缺失，先使用本技能的 `references/core_docs_template.md` 创建：

- README.md（入口、快速上手、文档导航）
- docs/project_status.md（当前架构与功能状态）
- docs/structure.md（目录与模块映射）
- docs/dev_plan.md（路线图与待办）
- docs/dev_log.md（实现与验证记录）
- docs/error_book.md（缺陷根因与解决手册）
- docs/features.md（已实现能力索引）
- docs/CODING_STANDARDS.md（项目代码规范纲领）
- docs/workflow.md（执行流程约定）
- docs/uin.md（AI 协作提示或约束，每 30 条按释放规则处理）

允许按项目增补文档，未经用户同意不得删减上述基线集合。

## 操作流程

遵循 `references/workflow_checklists.md` 中的清单。

### 阶段 0：初始化与对齐

1. 定位既有代码规范文档（优先 docs/CODING_STANDARDS.md）
2. 发现缺失的基线文档并补全骨架
3. 明确功能/缺陷范围、约束与验收标准
4. 确认单一事实来源所在，避免文档重复

### 阶段 1：开发前置门禁（强制）

在修改代码前完成全部项：

- 阅读代码规范与工作流文档
- 制定与验收标准绑定的实现计划
- 制定验证计划（单元/手工/集成等，视情况而定）
- 识别将变更的文件与模块
- 对高风险变更准备回滚策略

若本门禁未完成，停止实现。

### 阶段 2：按规范实现

- 先实现最小正确解，再优化
- 保持单一职责与命名清晰
- 将环境相关配置外置
- 为变更补充或更新相关测试
- 保持 diff 聚焦；避免无关重构

### 阶段 3：提交前验证

- 对变更范围运行所需测试/检查
- 端到端验证受影响的用户流程
- 确认无阻塞级 lint/类型/构建失败
- 在 docs/dev_log.md 中汇总验证依据

验证未通过时不要提交。

### 阶段 4：验证通过后的文档同步

测试通过后更新文档：

- docs/dev_log.md：改了什么、遇到什么问题、如何验证
- docs/error_book.md：根因、失败尝试、最终修复（若涉及缺陷）
- docs/project_status.md：新行为与使用影响
- docs/features.md：新增/更新的能力条目
- docs/dev_plan.md：标记已完成项并细化待办
- README.md：若用户可见行为变化则更新快速上手/文档索引
- docs/structure.md：仅当文件/模块结构变化时

### 阶段 5：协作交接

产出简洁交接块，包含：

- 任务范围与结果
- 变更文件
- 已执行的验证
- 已知限制或风险
- 建议的后续动作

保持交接可被机器解析、便于其他 AI 接续。

## 多 AI 协作约定

- 使用 `references/core_docs_template.md` 中的稳定标题与一致文档结构
- 变更记录写事实，不写聊天记录式流水账
- 明确记录假设，减少上下文丢失
- 文档间优先用链接引用，避免冲突性重复内容
- 规划、实现与状态文档中术语保持一致

## 本技能的输出约定

触发本技能时产出：

1. 开发前置门禁清单的执行结果
2. 实现结果与验证摘要
3. 文档同步报告（更新了哪些、为何更新）
4. 可供其他 AI 或工程师接续的最终交接说明

## 相关文档索引

WCS 自身仓库的文档结构（供维护自身时参考）：

> **注意**：WCS 是用 WCS 管理 WCS 自身的项目。wcs-skill 目录既是 git 仓库根，也是实际被加载的 skill 目录。详见 `docs/discussions/2026-06-06-git-vs-deploy-version.md`。

| 文档 | 用途 |
|------|------|
| `docs/project_index.yaml` | 中枢索引：task_contexts 映射（Module 1） |
| `docs/task_states.md` | 任务状态触发机制（Module 2） |
| `docs/skills_index.yaml` | 本地 skill 索引（Module 3，自动生成） |
| `docs/skills_index.md` | skill 索引说明 + 扫描脚本 |
| `docs/doc_sync_checklist.md` | Doc 同步检查清单（Module 4） |
| `docs/structure_index_experiment.md` | SQLite vs YAML 实验记录（Module 5） |
| `docs/structure.db` | SQLite 结构索引（可选，Module 5） |
| `docs/errorbook_release.md` | Errorbook 释放机制（Module 6） |
| `docs/docs_architecture_review.md` | Docs 架构扩展评估（Module 7） |
| `docs/discussions/2026-06-05-three-tier-docs-architecture.md` | 重构讨论记录 |
