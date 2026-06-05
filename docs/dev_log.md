# 开发日志

## 2026-06-05（下午）- WCS v2.0：七大模块完成

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

## 2026-06-05（上午）- WCS 发展脉络梳理与三层架构讨论

### 变更内容

#### WCS 发展四阶段

1. **阶段一：提示词阶段**
   - 原始形态：只是一段代码规范提示词
   - 核心功能：规定写代码的标准流程

2. **阶段二：Skill 化**
   - 变成可安装的 skill，一次安装全项目生效
   - 强调 docs 维护：git 备份 + docs 至少维护：目录结构、功能清单、错题本、prompt记录、readme、代码规范

3. **阶段三：docs 体系强化**
   - 发现"只有代码规范不够，还需要严格 docs 支持"
   - 重点转向：如何让 docs 保持最新、自动更新

4. **阶段四：三层架构演进（当前）**
   - 引入"中枢文档"概念
   - YAML 中枢 + docs 按需索引 + 全文件
   - 参考 codegraph 的文件感知思路，但保持 0 依赖

#### 待解决的核心问题

1. **WCS 没有自我迭代能力**：不能随着接管的 project 增多而自我提升
2. **规则背后的目标更重要**：规则可能落后，但目标不会

### 讨论议题（见 docs/discussions/2026-06-05-three-tier-docs-architecture.md）

- 中枢文档用 YAML 还是 SQLite？
- docs 发现机制：自动扫描 vs 手动注册
- 英文版 wcs/ 删除时机

### 验证情况

- 完成最新代码拉取（commit 02036fe）
- 建立讨论文档并提交到 git

### 回滚方式

- `git log` 查看讨论文档提交 `e694ec9`

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
