# 开发规划

## 规划说明

本文件是仓库当前开发规划的主看板。

- `done`：已完成并已进入仓库
- `next`：下一步优先处理
- `doing`：正在开发
- `todo`：已确认但尚未开始
- `watch`：持续观察，等待上游或后续需求触发

---

## 已完成

- `done`：将本地 `wcs` 技能整理为独立公开仓库
- `done`：补齐 WCS 要求的基线文档集合
- `done`：完成首次 GitHub 发布准备
- `done`：补充 `wcs-cn` 中文版镜像目录
- `done`：将仓库整理为 `wcs/` 与 `wcs-cn/` 并行结构
- `done`：补充清晰的文档导航，便于查看状态、功能和规划
- `done`：将仓库级文档统一切换为中文，并默认采用 `wcs-cn` 维护流程
- `done`：删除英文版 `wcs/` 目录（2026-06-05）
- `done`：建立 YAML 中枢索引 `docs/project_index.yaml`（2026-06-05）

---

## 核心开发队列（基于 WCS 定位）

### 模块 1：任务理解与上下文调度（P0）

**目标**：理解用户任务，选择合适的 skill、阅读合适的 doc

**实现方式**：
- 中枢文档 `project_index.yaml` 定义任务类型到 skill/doc 的映射
- WCS 启动时读取中枢，分析任务类型，推荐对应的 skill 和 doc
- AI 根据推荐按需激活 skill、阅读 doc

**状态**：`done` — 扩展到 16 种任务类型，每种配置 trigger_keywords

---

### 模块 2：任务状态触发机制（P0）

**目标**：根据任务状态（开新任务/修bug/加新功能/善后等）触发不同的 code standard

**实现方式**：
- 不再一次性完整阅读所有规范
- 根据当前状态，按需触发对应的规范子集
- 类似于 skill 机制：根据状态激活对应的规范 checklist

**状态**：`done` — `docs/task_states.md` 定义 15 种任务状态的触发规则

---

### 模块 3：本地 Skill 索引（P0）

**目标**：扫描本地 `~/.hermes/skills/`，建立 skill 索引，支持任务1顺利进行

**实现方式**：
- Python 脚本扫描 skills 目录
- 读取 SKILL.md 的 name、description、tags 字段
- 生成 `docs/skills_index.yaml`
- **附加**：记录 skill 使用情况，评估是否有效

**状态**：`done` — `scripts/scan_skills.py` 已实现（0 依赖，纯 stdlib）

---

### 模块 4：Doc 维护机制（P0）

**目标**：保证 doc 与项目同步更新

**实现方式**：
- 定义"哪些 docs 必须在 commit 前更新"的清单
- AI 开发后按清单检查并更新对应 doc
- 把此机制加入交接完整性检查

**状态**：`done` — `docs/doc_sync_checklist.md` 定义完整规则

---

### 模块 5：目录结构 SQLite 化（P1）

**目标**：将 `docs/structure.md` 升级为 SQLite，支持快速文件定位

**实现方式**：
- Python 脚本扫描源代码目录，建立文件索引
- SQLite 存储：文件路径、最后修改时间、关联模块
- 测试 YAML vs SQLite 的效果差异
- 实验结论：YAML 作为中枢索引，SQLite 作为可选增强

**状态**：`done` — `scripts/scan_structure.py` 已实现，实验记录于 `docs/structure_index_experiment.md`

---

### 模块 6：Errorbook 释放机制（P1）

**目标**：定时清空 errorbook，将内容归纳到系统性文件

**实现方式**：
- 定义触发条件（如：errorbook 超过 30 条 / 每季度 / 人工触发）
- 释放流程：阅读 → 分类归纳 → 更新对应 doc → 清空
- 类比 memory 释放机制

**状态**：`done` — `docs/errorbook_release.md` 定义完整生命周期

---

### 模块 7：Docs 架构扩展评估（P2）

**目标**：评估现有 docs 架构是否需要扩展

**评估内容**：
- 现有 9 个基线 docs 是否足够
- 是否需要按项目类型增删 docs
- 中枢索引 `project_index.yaml` 是否能覆盖所有场景

**状态**：`done` — `docs/docs_architecture_review.md` 给出评估结论（现有架构足够）

---

## 当前重点

- `next`：整理 Git 版本 vs 部署版本分离方案（讨论中）
- `next`：重建 CODING_STANDARDS.md、references/ 文档中文化、prompt.txt 重建
- `next`：评估 codegraph、context-model、rtk 等文件感知方案
- `next`：优化 WCS 三层架构（中枢——docs——全文件）

## 待开发

- `todo`：Module 8（待定义）——基于三层架构优化的下一阶段
- `todo`：部署版 wcs-cn 的目录结构确认（Git 版本 vs 部署版本分离方案落地）
- `todo`：prompt.txt 释放机制落地（用户输入缓存 → 归档流程）

## 观察项

- `watch`：关注模块1-7在实际项目中的效果，再决定下一阶段开发方向
- `watch`：WCS 定位是否需要随着开发推进调整
