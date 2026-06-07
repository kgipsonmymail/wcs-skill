# 开发日志

## 2026-06-07 - 状态展开式流程优化讨论

### 讨论背景

与 Wind 在飞书讨论 WCS 优化方向。核心问题：现有 WCS 虽然设计了状态机制，但文档一次性全塞给 AI，上下文负担重。

### 核心思路：触发式加载 vs 全量加载

**旧思路**：加载 skill 时把全部 docs 路径都塞给 AI，让 AI 自己决定读什么
**新思路**：先识别状态，根据状态决定读哪个文档，读完再决定下一步

### 展开式文档读取流程

```
WCS 入口（读 project_index.yaml） → 状态识别 → 按状态加载对应 doc → 按需展开下一步
```

### 状态与文档读取顺序（按 Wind 确认）

| 阶段 | 文档读取顺序 |
|------|-------------|
| 计划阶段 | project_index.yaml → dev_plan.md → （按需）features.md |
| 开发阶段 | project_index.yaml → CODING_STANDARDS.md → workflow.md → （按需）architecture.md |
| Bug 阶段 | project_index.yaml → errorbook.md → （按需）dev_log.md 查相关模块 |
| 需求阶段 | project_index.yaml → features.md → dev_plan.md → （按需）architecture.md |
| 维护阶段 | project_index.yaml → dev_log.md → project_status.md |
| 审查阶段 | project_index.yaml → review_checklist.md |

### 最小化上下文原则

1. **不要一开始就读 dev_log.md** — 太大了，按需才读
2. **不要一开始就读 architecture.md** — 只有架构相关问题才读
3. **不要一开始就读 errorbook.md** — 只有修 bug 才读
4. **project_index.yaml 是唯一开场必读** — 项目概览，最小信息量

### 状态识别触发词

| 状态 | 触发词 |
|------|--------|
| 计划阶段 | "我要做..."、"计划"、"打算" |
| 开发阶段 | "写个..."、"实现..."、"开发" |
| Bug阶段 | "报错"、"bug"、"坏了"、"崩溃" |
| 需求阶段 | "加个功能..."、"新需求"、"加一个" |
| 维护阶段 | "日常维护"、"更新依赖"、"整理" |
| 审查阶段 | "帮我看看代码"、"review"、"评审" |

### 待落地

- ~~review_checklist.md 是否存在（审查阶段需要）~~ → 已确认审查阶段直接读 CODING_STANDARDS.md
- 已实施：更新 SKILL.md 加入状态识别 + 最小化开场原则

### 验证情况

- SKILL.md 已完全重写（约 7800 字符）
- 核心变化：状态识别提前、最小化开场、展开式加载
- workflow_checklists.md 作为参考文献保留，按需激活

### 2026-06-07 续 - Session 反思块

新增**零依赖自我衡量机制**：在 SKILL.md 的输出约定里加入 Session 反思块。

**核心借鉴**：
- systematic-debugging 的 Iron Law（强制自检）
- subagent-driven-development 的阶段输出声明
- plan 的结构化交付物

**反思块格式**：
```
## Session 反思
- 状态识别：[识别了什么状态/是否准确]
- 初始加载：[开场读了哪些 doc / 是否符合最小化原则]
- 按需展开：[后续读了哪些 doc / 是否按状态展开]
- 违反记录：[若有违反最小化原则，说明原因]
- 本次总结：[一句话描述本次是否符合 WCS 原则]
```

**设计思路**：
- 对用户可见，形成监督闭环
- 自我审计数据可积累用于 WCS 迭代
- 零依赖实现，不增加外部依赖

### 2026-06-07 续 - Skill 管理

新增 Skill 管理章节，实现**零依赖按需激活**。

**核心原则**：按需激活，不确定时不激活。只激活当前任务明确需要的 skill。

**Skill 分类**：
- 规范类（wcs-cn）：几乎所有开发任务都需要
- 调试类（systematic-debugging）：调试/修 bug 时
- 项目类（mediary/video-daily）：特定项目开发时
- 辅助类（writing-plans）：需要制定计划时

**各状态 Skill 激活建议**：计划/开发/Bug/需求/维护/审查各有默认激活 + 按需激活规则

**Session 反思块同步更新**：加入 Skill 激活记录字段

### 回滚方式

- 本次为讨论记录，无需回滚
- 具体代码变更待实施

---

## 2026-06-06 下午 - 文档质量整理与 Git vs 部署版分离

### 变更内容

#### references/ 英文文档全部中文化

- `references/api_reference.md`：删除英文内容，重写为中文索引说明
- `references/coding_standard_template.md`：完全重写，删除英文痕迹，质量对齐原版原型
- `references/workflow_checklists.md`：完全重写为中文，流程和检查项全部中文化
- `references/core_docs_template.md`：完全重写为中文，删除英文残留

#### docs/ 文档质量提升

- `docs/CODING_STANDARDS.md`：重写，删除 `wcs/` 英文版引用，质量对齐原版原型
- `docs/uin.md`：完全重建，加入释放机制：
  - 规则1：已完成开发任务 → 检查 dev_log/dev_plan 有无记录，补写后删除
  - 规则2：未完成开发任务 → 提问用户是否继续
  - 规则3：用户见解/方法论 → 归档到 `docs/discussions/user_insights.md`
  - 阈值：30 条触发释放

#### Git 版本 vs 部署版本分离

- 新增讨论文档：`docs/discussions/2026-06-06-git-vs-deploy-version.md`
- `docs/structure.md`：新增版本说明章节
- `docs/dev_plan.md`：新增 Git vs 部署版分离相关待办项

### 验证情况

- `git push` 成功（commit `4edd956`）
- references/ 所有文件已中文化
- uin.md 释放机制已写入文件头部

### 回滚方式

- `git log` 查看提交 `4edd956`
- `git show 4edd956 --stat` 查看变更文件列表

### 2026-06-06 下午 续 - Git vs 部署版分离决策确认

#### 确认内容

- **部署版**（`wcs-cn/`）**无 `docs/`**，只包含 `SKILL.md` + `references/`
- **uin.md** 存在于两个位置：
  1. Git 版本的 `docs/uin.md`（WCS 自用）
  2. 用户开发项目中的 `docs/uin.md`（AI 实际使用时读）
- Git 版本 `wcs-cn/SKILL.md` 更新说明，明确部署版结构
- `docs/discussions/2026-06-06-git-vs-deploy-version.md` 同步更新，整理为"已确认"+"待确认"两部分

#### 验证情况

- `git push` 成功（commit `66409ea`）

---

## 2026-06-05 下午 - WCS v2.0：七大模块完成

### 变更内容

#### 模块 1-7 全部完成

本次系统性开发，完成了 WCS v2.0 的七大核心模块：

| 模块 | 文件 | 状态 |
|------|------|------|
| M1: task_contexts | `docs/project_index.yaml` | 16 种任务类型 + trigger_keywords |
| M2: 任务状态触发 | `docs/task_states.md` | 15 种状态触发规则 |
| M3: Skill 索引 | `scripts/scan_skills.py` | 0 依赖 stdlib，扫描 81 skills |
| M4: Doc 同步 | `docs/doc_sync_checklist.md` | 完整同步规则 + 交接检查 |
| M5: SQLite 索引 | `scripts/scan_structure.py` + 实验记录 | YAML 作为中枢，SQLite 可选增强 |
| M6: Errorbook 释放 | `docs/errorbook_release.md` | 30 条阈值，分类归纳流程 |
| M7: Docs 架构评估 | `docs/docs_architecture_review.md` | 当前 9 个基线 doc 足够 |

#### 关键设计决策

- **YAML 作为中枢索引**：人类可读、版本可控、AI 友好
- **SQLite 作为可选增强**：大型项目（>1000 文件）可用，但非默认
- **0 依赖**：scan_skills.py 和 scan_structure.py 仅用 stdlib
- **trigger_keywords 自主判断**：AI 根据关键词匹配任务类型，不依赖固定流程

### 验证情况

- `scripts/scan_skills.py --no-yaml` 成功扫描 81 skills，生成 `docs/skills_index.yaml`
- `scripts/scan_structure.py .` 成功扫描 321 items（0.04s），生成 `docs/structure.db`
- `wcs-cn/SKILL.md` 已重写，移除英文版引用，添加相关文档索引
- 所有 17 个文件已 commit（`c079c51`）

### 回滚方式

- `git log` 查看提交 `c079c51`
- `git show c079c51 --stat` 查看变更文件列表

---

## 2026-06-05 上午 - WCS 自举循环与三层架构讨论

### 变更内容

#### 自举循环验证

本次维护验证了 WCS 可以用自身的三层 docs 结构管理自身迭代：

1. **YAML 中枢** `docs/project_index.yaml` 已定义 WCS 自身维护的任务上下文
2. **docs 层** `docs/dev_plan.md` 承载七大模块开发队列，`docs/dev_log.md` 记录演进历史
3. **file 层** 通过 `git log` 可追溯每个维护动作

#### 本次固化的决策

- **英文 wcs/ 删除**：确认并执行完毕
- **YAML 中枢确认**：YAML 作为中枢索引（SQLite 待定，需测试后决策）
- **七大模块归档**：确定开发队列（模块1-4 为 P0/P0/P0/P0，模块5-7 为 P1/P1/P2）
- **三层架构文档化**：`docs/discussions/2026-06-05-three-tier-docs-architecture.md` 已归档

#### WCS 定位 v3（已确认）

> "WCS 是 AI 开发方法论框架。每个开发任务第一个激活它，由它分析任务、激活合适的 skill、引导阅读必要的 doc、定位需要的 file，在保证开发质量的前提下最快完成任务。WCS 通过在实践中不断总结经验来迭代自身。"

### 验证情况

- 所有变更已 commit 并推送 GitHub（commit `f8e1252`）
- `docs/project_index.yaml` 的 `task_contexts.wcs_maintenance` 可作为后续维护的导航
- WCS 自举循环跑通：讨论 → 决策 → 文档更新 → git 备份

### 回滚方式

- `git log` 查看提交 `f8e1252`
- Mediary doc 8575 同步更新（外部备份）

---

## 2026-04-13 - 仓库文档中文化与维护视角切换

### 变更内容

- 将 `README.md` 与 `docs/` 下仓库级文档统一改写为中文
- 将仓库默认维护流程切换为 `wcs-cn`，并在文档中明确 `wcs/` 英文版可忽略
- 同步更新规划、状态、功能、结构、规范与协作提示文档

### 验证情况

- 复核 `README.md`、`docs/dev_plan.md`、`docs/project_status.md`、`docs/features.md`、`docs/workflow.md` 的中文表述与维护视角是否一致
- 确认当前仓库结构仍与 `wcs/`、`wcs-cn/` 双目录现状一致

### 回滚方式

- 回退本次文档提交即可恢复此前的英文仓库级文档

---

## 2026-04-13 - 规划文档整理

### 变更内容

- 将 `docs/dev_plan.md` 重构为更清晰的规划面板，使用 `done`、`next`、`todo`、`watch` 标记状态
- 更新 `README.md` 和 `docs/project_status.md`，补充规划主文档入口
- 更新 `docs/features.md`，反映规划可视化能力

### 验证情况

- 复核 `README.md`、`docs/dev_plan.md`、`docs/project_status.md` 和 `docs/features.md` 的术语一致性
- 确认仓库仍满足 WCS 基线文档要求

### 回滚方式

- 回退对应文档提交即可恢复此前的规划文案

---

## 2026-04-13 - 开源打包与发布

### 变更内容

- 将本地 `wcs` 技能整理为独立仓库
- 添加 `README.md`、`LICENSE`、`.gitignore` 与基础占位文件
- 补齐 WCS 要求的基线 `docs/` 文档集合

### 验证情况

- 确认原始本地技能存在于 `C:\Users\wind\.codex\skills\wcs`
- 确认仓库内包含 `SKILL.md` 与全部 `references/*.md` 文件
- 确认当时本地源中尚未包含 `wcs-cn`，因此公开仓库显式记录这一缺口

### 回滚方式

- 若放弃发布，删除 `wcs-skill` 工作目录即可

---

## 2026-04-13 - 增加中文镜像目录

### 变更内容

- 将本地 `wcs-cn` 技能复制到仓库的 `wcs-cn/`
- 更新仓库文档，说明中英文两个版本均已发布
- 添加占位文件，确保 Git 保留空的 `wcs-cn/assets` 与 `wcs-cn/scripts` 目录

### 验证情况

- 确认本地源存在于 `C:\Users\wind\.codex\skills\wcs-cn`
- 确认 `wcs-cn/` 包含 `SKILL.md` 与完整的 `references/*.md`
- 确认新增提交前仓库主分支处于干净状态

### 回滚方式

- 若不再发布中文镜像，可删除 `wcs-cn/` 并回退对应提交

---

## 2026-04-13 - 仓库结构重组

### 变更内容

- 将英文技能内容移动到 `wcs/`
- 保留 `wcs-cn/` 作为并列顶层目录，使中英文版本具有对称结构
- 更新仓库文档，改为指向 `wcs/` 与 `wcs-cn/` 的实际路径

### 验证情况

- 确认 `wcs/` 包含 `SKILL.md`、`references/*.md`、`assets/.gitkeep` 和 `scripts/.gitkeep`
- 确认 `wcs-cn/` 在结构重组后保持完整
- 确认仓库级文档已更新为新路径

### 回滚方式

- 若放弃双目录结构，可将英文技能移回仓库根目录并回退对应提交
