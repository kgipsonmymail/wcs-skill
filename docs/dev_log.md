# 开发日志

> 里程碑摘要，与 git log 互为补充。**不作为有效信息源。**

## 2026-07 功能实现摘要

- 2026-07-10：mediary-dev 图标按钮样式统一（IconButton 组件）
  - 新建 `IconButton` 组件，两种 variant：`icon`（纯图标 rounded-full p-1.5）和 `action`（图标+文字 rounded-lg px-3 py-2）
  - 迁移 DocumentShare、DocumentDisplay Pin、DocumentSidePanel Pin、DocumentListItem Edit2 到 IconButton
  - 解决手机端菜单里分享按钮文字掉到图标下方的问题

- 2026-07-09：mediary-dev 分享页公众号预览响应式适配（手机端页边距收紧，桌面端保持正常）
  - 移除两层多余的 wrapper div（原来 max-width:580px × 2 层导致手机版太窄）
  - 同步去掉 wrapWechatArticle 里的 max-width/margin/padding 约束
  - 阅读版和公众号版统一响应式 padding：手机 px-4，桌面 sm:px-8

- 2026-07-09：mediary-dev DocumentEdit.tsx 手机端 Header 优化
  - Bug 修复：新窗口打开按钮图标 Trash2 → ExternalLink（之前有两个 Trash2 并排）
  - 新增手机端更多菜单（⋯ MoreVertical），收纳：侧边栏/新窗口打开/置顶/分享/版本历史/删除
  - 桌面端行为不变，保持所有按钮直接显示
  - 删除操作增加 confirm 确认防误删

## 2026-06 功能实现摘要

- 2026-06-11：mediary-dev 公众号版 blockToWechatHtml 主题色一致性问题（1.5h）— default case 和 table cells 用 renderMarkdownSync 输出 .md-strong class，shared 页面无 CSS 导致加粗显示黑色；统一改用 renderInlineMarkdown，走 inline style 路径

- 2026-06-10：mediary-dev 文档列表状态持久化（Zustand + localStorage，筛选条件/页码/滚动位置）
- 2026-06-10：mediary skill 识别词优化（穷举大小写/拼写/中文/组合变体，解决 401 调用失败）
- 2026-06-10：mediary skill 标准化调用规范（手动解析 .env，api_get/api_post 辅助函数）
- 2026-06-10：mediary skill 新增 error_book.md（.env 覆盖事故根因分析）
- 2026-06-09：mediary-dev 文档版本历史功能（subagent 成果，主 Agent 补救提交）

## 2026-06 WCS 自身迭代

- 2026-06-10：WCS features.d/ 和 structure.d/ 全面填充，关键对象和关联映射完整
- 2026-06-10：WCS errorbook 积累机制建立（遇到 bug 立刻记，释放阈值20）
- 2026-06-10：WCS Bug 阶段标准4步排查流程写入 features.md
- 2026-06-10：WCS features.md/structure.md 建立 dynamic 维护触发机制和联动映射
- 2026-06-10：WCS dev_log.md 重新定位为里程碑摘要（640行旧内容清除）
- 2026-06-10：WCS errorbook 积累机制 + features/structure 重新定位
- 2026-06-07：WCS 状态展开式加载（project_index → 按状态读 doc → 按需展开下一步）
- 2026-06-07：WCS Subagent 监督闭环（强制完成项 + 退出前检查 + 主 Agent 补救）
- 2026-06-05：WCS v2.0 七大模块完成（task_contexts / 状态触发 / skill 索引 / doc 同步 / SQLite 索引 / errorbook 释放 / docs 架构评估）
