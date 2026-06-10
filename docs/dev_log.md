# 开发日志

> 里程碑摘要，与 git log 互为补充。**不作为有效信息源。**

## 2026-06 功能实现摘要

- 2026-06-10：mediary-dev SM18 回顾功能上线（后端 Go + 前端 React，5 个 Tab，间隔重复算法）
- 2026-06-10：mediary-dev 文档列表状态持久化（Zustand + localStorage，筛选条件/页码/滚动位置）
- 2026-06-10：mediary skill 识别词优化（穷举大小写/拼写/中文/组合变体，解决 401 调用失败）
- 2026-06-10：mediary skill 标准化调用规范（手动解析 .env，api_get/api_post 辅助函数）
- 2026-06-10：mediary skill 新增 error_book.md（.env 覆盖事故根因分析）
- 2026-06-09：mediary-dev 文档版本历史功能（subagent 成果，主 Agent 补救提交）

## 2026-06 WCS 自身迭代

- 2026-06-10：WCS errorbook 积累机制建立（遇到 bug 立刻记，不等释放）
- 2026-06-10：WCS errorbook 释放阈值从 15 调整到 20
- 2026-06-10：WCS dev_log 重新定位为里程碑文档，不再堆放有效信息
- 2026-06-07：WCS 状态展开式加载（project_index → 按状态读 doc → 按需展开下一步）
- 2026-06-07：WCS Subagent 监督闭环（强制完成项 + 退出前检查 + 主 Agent 补救）
- 2026-06-05：WCS v2.0 七大模块完成（task_contexts / 状态触发 / skill 索引 / doc 同步 / SQLite 索引 / errorbook 释放 / docs 架构评估）
