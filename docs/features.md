# 功能详情

> 本文件是功能网络/功能树的**提纲**，描述每个功能的业务逻辑和前后端互动。
> 详细级别（函数/类型/文件路径）在 `features.d/` 子目录中按需维护。
> 动态维护规则：errorbook 纠正 bug 时，将排查到的文件和函数同步到对应的 subordinate doc。

---

## 功能网络

```
WCS-Skill
├── 状态展开式加载
│   └── 功能：AI 读取项目时，先识别状态，按状态决定读哪个 doc
├── Errorbook 积累与释放
│   └── 功能：遇到 bug 立刻记，>20 条触发归纳释放
├── Subagent 监督闭环
│   └── 功能：delegate_task 时传递完整 context，返回后主 Agent 补救
├── 三层 Docs 结构
│   └── 功能：用 project_index.yaml 做中枢，docs/ 做治理，git 做版本
└── md-renderer 渲染路径一致性
    └── 功能：公众号版 blockToWechatHtml 统一走 inline style，避免 CSS class 在无 CSS 导入页面失效
```

---

## 功能详情

### 1. 状态展开式加载

**业务逻辑**：AI 收到任务后，先读 `project_index.yaml` 识别状态（计划/开发/Bug/维护等），再按状态决定读哪个 doc，而不是一次性塞入所有文档。

**前后端互动**：
- 无前后端，纯 AI 协作逻辑

**Subordinate doc**：`features.d/state-loading.yaml`

---

### 2. Errorbook 积累与释放

**业务逻辑**：遇到 bug 时立刻在 `error_book.md` 写一条（标准 5 字段：问题/调试时间/尝试过程/根因/解决/下次遇到），不等待释放。条目 >20 或 1 个月触发释放流程：阅读 → 分类归纳到 features.md/CODING_STANDARDS.md → 清空。

**前后端互动**：
- 无前后端，纯 AI 协作逻辑

**Subordinate doc**：`features.d/errorbook.yaml`

---

### 3. Subagent 监督闭环

**业务逻辑**：使用 `delegate_task` 时，主 Agent 必须传递 4 个 context 块（项目入口/强制完成项/Subagent 反思块/max_iterations），subagent 返回后执行 4 步监督补救。

**前后端互动**：
- 无前后端，纯 AI 协作逻辑

**Subordinate doc**：`features.d/subagent闭环.yaml`

---

### 4. 三层 Docs 结构

**业务逻辑**：Git 版本用 `wcs-cn/SKILL.md` + `docs/` + `references/` 三层。部署版只有 `wcs-cn/SKILL.md` + `references/`。`project_index.yaml` 作为 YAML 中枢连接所有层。

**前后端互动**：
- 无前后端，纯文档架构

**Subordinate doc**：`features.d/三层-docs-结构.yaml`

---

## Subordinate Docs 管理规则

### features.d/ 目录结构

```
features.d/
├── _index.yaml       # 功能清单索引（自动生成）
├── state-loading.yaml
├── errorbook.yaml
├── subagent闭环.yaml
└── 三层-docs-结构.yaml
```

### 动态维护触发机制

**触发条件（满足任一即维护）：**
- 修复 bug 时 → errorbook 条目的"根因"+"解决"涉及的文件和函数 → 追加到对应 `features.d/{功能}.yaml` 的关键对象和已知坑
- 新增功能时 → 在 `features.d/` 创建 `{功能名}.yaml`，在 `features.md` 的功能网络树和功能详情节添加入口
- 释放 errorbook 时 → 分类归纳到 features.md → 同步更新 `features.d/` 对应条目的已知坑
- 架构调整时 → 更新 features.md 的功能网络树 → 同步更新 `features.d/` 对应条目

**维护优先级：**
1. 已知坑（来自 errorbook）> 关键对象（来自 debug 过程）
2. 不追求一次性填满，按需逐步积累
3. features.d/ 的价值在于"下次遇到同类 bug 能快速定位"

### features.d/{功能}.yaml 格式

```yaml
功能: 功能名称
概述: 一句话描述

# 参与模块（前后端）
前端模块: []
后端模块: []

# 关键对象（动态维护，Bug 调试时补充）
关键对象:
  - 文件: src/pages/XXX.tsx
    关键函数/类型:
      - ComponentName    # 组件
      - useStoreName    # hooks/store
  - 文件: backend/handler/xxx.go
    关键函数/类型:
      - HandlerFunc     # handler 函数

# 已知坑（来自 errorbook）
已知坑:
  - 调试时间: 0.5h
    现象: 错误信息
    根因: 真正的原因
    涉及文件: [文件列表]
```

---

## features.d/ 现有条目

- ✅ state-loading.yaml — 关键对象: project_index.yaml / task_states.md / workflow.md / SKILL.md
- ✅ errorbook.yaml — 关键对象: error_book.md / errorbook_release.md / SKILL.md；6个已知坑
- ✅ subagent闭环.yaml — 关键对象: SKILL.md / dev_log.md / CODING_STANDARDS.md
- ✅ 三层-docs-结构.yaml — 关键对象: wcs-cn/ / docs/ / references/

---

## features.d/ ↔ structure.d/ 联动机制

features.d/ 和 structure.d/ 从不同视角描述同一套系统，互相引用形成网络：

| features.d/ 条目 | → 关联 structure.d/ 条目 |
|-----------------|------------------------|
| state-loading | structure.d/wcs-cn.yaml（SKILL.md 是状态加载的执行体） |
| errorbook | structure.d/docs.yaml（error_book.md 在 docs/ 下） |
| subagent闭环 | structure.d/wcs-cn.yaml（SKILL.md 定义 subagent 协作规范） |
| 三层-docs-结构 | structure.d/wcs-cn.yaml + structure.d/docs.yaml（两层都在 docs/ 下） |

**联动规则：**
- 当某个文件在 features.d/ 的关键对象里出现时，对应的 structure.d/ 条目也应包含该文件
- Bug 调试时：先从 features.d/ 定位功能网络，再从 structure.d/ 定位文件路径，双向印证
