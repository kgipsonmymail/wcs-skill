# Doc 同步检查清单

## 核心理念

> 文档是对代码的承诺。代码变了，文档不更新，就是对未来的自己撒谎。

Doc 同步是 WCS 开发流程的必要环节，不是可选项。

---

## 必更新清单

根据任务类型，commit 前必须更新以下 doc：

| 任务类型 | 必须更新的 doc | 原因 |
|----------|--------------|------|
| **所有任务** | `dev_log.md` | 记录所有变更，历史可追溯 |
| bug_fix | `error_book.md` | 记录根因和解决方案 |
| new_feature | `features.md` + `dev_plan.md` | 新增能力 + 规划更新 |
| refactor | `structure.md`（若结构变了） | 结构变更须同步 |
| 任何影响用户可见行为 | `project_status.md` | 状态变更 |
| 新项目初始化 | 全部 9 个基线 doc | 建立基准 |

### 9 个基线 Doc 清单

1. `README.md` — 入口、快速上手、文档导航
2. `docs/project_status.md` — 当前架构与功能状态
3. `docs/structure.md` — 目录与模块映射
4. `docs/dev_plan.md` — 路线图与待办
5. `docs/dev_log.md` — 实现与验证记录
6. `docs/error_book.md` — 缺陷根因与解决手册
7. `docs/features.md` — 已实现能力索引
8. `docs/CODING_STANDARDS.md` — 项目代码规范纲领
9. `docs/workflow.md` — 执行流程约定

---

## Doc 更新时机规则

### 规则 1：代码变更后必须更新 doc

任何代码 commit 必然伴随 `dev_log.md` 更新。

### 规则 2：按变更性质决定更新范围

```
代码变更 + 新能力  → dev_log + features + dev_plan + project_status
代码变更 + Bug修复 → dev_log + error_book + project_status
代码变更 + 重构    → dev_log + structure + project_status
纯 Doc 变更        → 仅更新涉及的 doc + dev_log
```

### 规则 3：更新时保持一致性

- Doc 之间不要矛盾（引用单一事实来源）
- 同一概念在不同 doc 中用同一术语
- 相关 doc 同时更新（如 features + dev_plan）

### 规则 4：Commit 前自检

提交前对照清单确认：

1. 本次变更涉及的所有 doc 都已更新 ✓
2. 更新内容与代码变更一致 ✓
3. 没有引入与其他 doc 的矛盾 ✓
4. `dev_log.md` 已记录本次变更 ✓

---

## 交接完整性检查

交接前额外检查：

- [ ] `dev_log.md` 包含本次所有变更记录
- [ ] `dev_plan.md` 反映了当前待办状态
- [ ] 如果有 bug：`error_book.md` 有记录
- [ ] 如果有新能力：`features.md` 有条目
- [ ] 如果有结构变更：`structure.md` 已更新
- [ ] `project_status.md` 反映最新状态

---

## 与 Task States 的联动

本清单与 `task_states.md` 联动：

- **Module 2** 定义了每个任务状态激活哪些规范子集
- **本清单** 定义了这些规范子集中 doc 更新的具体要求

两者结合，构成完整的"状态 → 响应"规则。

---

## 常见问题

**Q: 如果忘记更新 doc 就 commit 了怎么办？**
A: 立即补更。在下一个 commit 中补上 doc 更新，不要等到下一次代码变更。

**Q: 怎么判断是否需要更新 `project_status.md`？**
A: 自问："用户/其他 AI 能感知到这个变更吗？"如果能，就更新。

**Q: doc 更新和代码实现哪个先？**
A: 代码先实现、验证通过后，同步更新 doc。验证通过是 doc 更新的前提。

**Q: 什么时候可以跳过某些 doc 更新？**
A: 当任务明确只是内部重构且不影响任何外部可见行为时，可以跳过 `features.md` 和 `project_status.md`，但 `dev_log.md` 永远不能跳过。
