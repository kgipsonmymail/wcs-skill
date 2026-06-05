# 代码规范

本文件是项目代码规范的纲领性文档。规范细节参照 `references/coding_standard_template.md`，工作流程门禁参照 `references/workflow_checklists.md`。

## 必须遵守

1. **验证在前，提交在后**：未通过验证不提交。
2. **事实记录**：`docs/dev_log.md` 记录实现与验证的事实，不写流水账。
3. **错误留档**：缺陷根因、失败尝试、最终修复写入 `docs/error_book.md`。
4. **文档同步**：验证通过后立即更新受影响文档，不遗漏。
5. **最小变更**：diff 聚焦，避免无关重构。
6. **不公开敏感信息**：不暴露本地环境信息、私密路径或凭据。

## 命名与结构

- Markdown 文件与引用文件沿用现有文件名，不做随意重命名
- 新增辅助文件应与技能正文明确分离，不污染核心目录
- 目录结构反映模块职责，变更时更新 `docs/structure.md`

## 验证要求

- 测试通过后再提交（无测试时做等价的手工验证）
- lint、类型检查、构建检查按变更范围执行
- 未完成内容复核前，不要创建发布型提交

## 提交要求

- 格式：`<type>: <摘要>`
- type：`feat` / `fix` / `refactor` / `docs` / `chore`
- 单次提交保持聚焦，可审阅、可回滚

## 文档同步时机

- 架构/文件变更 → 更新 `docs/structure.md` 和 `docs/project_status.md`
- 新增或变更能力 → 更新 `docs/features.md` 和 `docs/project_status.md`
- 缺陷修复 → 更新 `docs/error_book.md` 和 `docs/dev_log.md`
- 任何交付变更 → 更新 `docs/dev_log.md`
- 安装方式、维护入口或仓库定位变化 → 更新 `README.md`
