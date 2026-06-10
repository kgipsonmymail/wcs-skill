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
└── 三层 Docs 结构
    └── 功能：用 project_index.yaml 做中枢，docs/ 做治理，git 做版本
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

### 动态维护规则

1. **新增功能** → 在 `features.d/` 创建 `{功能名}.yaml`，在 `features.md` 的功能网络和功能详情节添加入口
2. **Bug 纠正时** → 在 errorbook 条目的"根因"和"解决"中提取涉及的文件和函数，追加到对应 `features.d/{功能}.yaml`
3. **定期同步** → 每次释放 errorbook 后，更新对应的 `features.d/` 条目

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

（暂无条目，动态维护开始后逐步填充）
