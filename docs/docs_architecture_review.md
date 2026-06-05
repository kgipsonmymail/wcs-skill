# Docs 架构扩展评估

## 评估日期

2026-06-05

---

## 当前 9 个基线 Doc 评估

| Doc | 必要性 | 扩展性 | 结论 |
|-----|--------|--------|------|
| `README.md` | ⭐⭐⭐ 必须 | 始终保持入口功能 | 保留 |
| `project_status.md` | ⭐⭐⭐ 必须 | 承载架构/行为快照 | 保留 |
| `structure.md` | ⭐⭐⭐ 必须 | 大型项目可增强为 SQLite | 保留（YAML 够用） |
| `dev_plan.md` | ⭐⭐⭐ 必须 | 项目规模变大时自然分层 | 保留 |
| `dev_log.md` | ⭐⭐ 必须 | 按项目生命周期归档 | 保留，考虑历史归档 |
| `error_book.md` | ⭐⭐ 必须 | 需定期释放（Module 6） | 保留，生命周期管理 |
| `features.md` | ⭐⭐ 必须 | 按模块/组件分层 | 保留，考虑结构化 |
| `CODING_STANDARDS.md` | ⭐⭐⭐ 必须 | 随项目增加自然扩展 | 保留 |
| `workflow.md` | ⭐ 一般 | 工作流稳定后可简化 | 保留但可精简 |

**评估结论**：9 个基线 doc 结构合理，无需增删。

---

## 当前 docs 架构的优点

1. **覆盖完整**：从状态到规划、从日志到规范，无遗漏
2. **命名清晰**：文件名即语义，无需解释
3. **更新有规律**：按任务类型有明确的更新清单（Module 4）
4. **层级清晰**：`project_index.yaml` 提供中枢导航

---

## 潜在扩展场景

### 场景 A：超大型项目（文件数 > 5000）

可能需要：
- 按领域拆分 `features.md` → `features/frontend.md`、`features/backend.md`
- 按模块拆分 `structure.md` → `structure/backend.md`、`structure/frontend.md`
- 新增 `docs/glossary.md`（统一术语表）

**触发条件**：当 `features.md` 超过 500 行时考虑拆分

### 场景 B：多团队协作

可能需要：
- 新增 `docs/OWNERS.md`（模块负责人）
- 新增 `docs/CHANGELOG.md`（版本变更记录）
- `dev_log.md` 改为按模块分文件

**触发条件**：团队 > 5 人时考虑

### 场景 C：对外开源

可能需要：
- 新增 `CONTRIBUTING.md`
- 拆分 `README.md` → 精简 README + 详细 docs/README.md
- 新增 `docs/ARCHITECTURE.md`（对外架构说明）

**触发条件**：项目对外开源时

### 场景 D：WCS 自身演进

WCS 作为方法论框架，当它管理更多项目时：
- 可能需要新增 `projects/` 子目录，记录每个被管项目的情况
- 可能需要 `docs/templates/` 存放各类型项目的 doc 模板

---

## 评估结论

### 当前结论（2026-06-05）

**现有 9 个基线 docs 足够，不需要扩展。**

原因：
1. WCS 目前管理的项目规模适中
2. 当前没有 > 5000 文件的超大型项目
3. 没有多团队协作场景
4. 框架自身文档需求已满足

### 未来触发扩展的条件

| 条件 | 扩展动作 |
|------|---------|
| `features.md` > 500 行 | 按模块拆分 features |
| `structure.md` > 500 行 | 考虑 SQLite 增强 |
| 团队 > 5 人 | 新增 OWNERS + CHANGELOG |
| 项目对外开源 | 新增 CONTRIBUTING + ARCHITECTURE |
| WCS 管理 > 10 个项目 | 新增 `projects/` 索引 |

### 扩展原则

> 不要提前优化。当前够用就不扩展，扩展时优先拆大文件，而不是新增文件。

---

## 与其他模块的关系

- Module 1（task_contexts）：通过 YAML 中枢索引各类 doc
- Module 4（doc_sync）：保证 doc 同步更新
- Module 5（SQLite 索引）：大型项目的可选增强
- **本模块**：定义何时应该扩展 docs 架构

---

## 下次评估时间

当以下任一情况出现时，重新评估：

- 任何 doc 文件超过 500 行
- WCS 管理的项目数量 > 5
- `dev_log.md` 单文件超过 1000 行
