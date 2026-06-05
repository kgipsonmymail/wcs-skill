# 三层文档管理架构讨论

> 创建时间：2026-06-05
> 讨论背景：codegraph/context-model/RTK 插件研究 + WCS 框架优化

---

## 一、问题陈述

### 当前 WCS 阅读顺序的问题

**现状**：新开对话 → AI 阅读所有 docs → 开始执行任务

**问题**：
- 每个任务都要读全部 docs，效率低
- docs 数量增长后，上下文爆炸
- AI 无法快速定位与当前任务相关的文档
- 不同类型任务（功能开发/bug修复/架构调整）需要不同的文档子集

### 期望的三层管理架构

```
┌─────────────────────────────────────────────────────────────┐
│  中枢文档（YAML/项目总览）                                     │
│  - 项目全局索引                                               │
│  - 文档位置映射                                               │
│  - AI 决策依据（看哪些 docs）                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │ 引用
┌──────────────────────▼──────────────────────────────────────┐
│  docs 目录（按主题/模块组织）                                   │
│  - dev_plan.md / dev_log.md / features.md                    │
│  - 模块级文档（backend.md / frontend.md / database.md）         │
│  - AI 按需选择性阅读                                           │
└──────────────────────┬──────────────────────────────────────┘
                       │ 引用
┌──────────────────────▼──────────────────────────────────────┐
│  全文件（源代码）                                              │
│  - AI 可直接定位到具体文件/函数                                 │
└─────────────────────────────────────────────────────────────┘
```

**核心优化**：AI 收到任务后，**先读中枢文档** → 决定需要哪些 docs → 按需阅读

---

## 二、参考系统研究

### 2.1 CodeGraph

**功能**：代码知识图谱，通过 AST 分析建立代码结构索引

```
代码文件 → AST 解析 → 符号索引 → 关系图
                            ↓
                      MCP Server 提供查询接口
```

**可借鉴**：
- 用程序维持对所有文件的感知（增量索引）
- 关系映射能力（函数调用链、依赖关系）
- 查询接口（按符号/关系检索）

**不采用**：
- 不做 AST 级别的代码分析（重、依赖 Node.js）
- 不 fork 或二次开发（成为直接使用者）

### 2.2 Context-Mode（RTK 相关）

**功能**：上下文压缩，据说节省 98% tokens

**可借鉴**：
- 按任务裁剪上下文的思路
- 主动决定"看什么、不看什么"

**不采用**：
- 不安装基础依赖（Node.js 环境、RTK Rust 工具链）

### 2.3 RTK（Token Guard）

**功能**：Eagle Mem 的 token 保护，监控 shell 输出 token

**结论**：重依赖（Rust 工具链），暂不考虑

---

## 三、依赖优先级框架

按你的优先级排序：

| 优先级 | 方案 | 说明 |
|--------|------|------|
| 0 | **纯自管理**（0依赖） | 用 YAML/纯文本做中枢，不装任何外部工具 |
| 1 | **轻依赖** | 加一点功能就能实现最多作用（如用 sqlite 做索引） |
| 2 | **现成项目** | 成为 codegraph 的直接使用者，不 fork/二次开发 |
| 3 | **基础依赖** | codegraph 所依赖的相关配置（Node.js 等） |

---

## 四、提案：YAML 中枢 + docs 按需索引

### 4.1 中枢文档设计（YAML）

```yaml
# project_index.yaml
project:
  name: mediary
  type: go-frontend分离架构
  tech_stack:
    backend: Go + Gin
    frontend: React + Vite
    database: MySQL 8.0
    
docs:
  # 全局导航（必读）
  - path: docs/project_status.md
    purpose: 项目状态总览
    read_when: [onboarding, architecture_change]
    
  - path: docs/structure.md
    purpose: 目录结构映射
    read_when: [onboarding, new_module]
    
  # 模块级文档（按需）
  - path: docs/backend/api.md
    purpose: 后端 API 结构
    tags: [backend, api]
    read_when: [backend_change, api_integration]
    
  - path: docs/frontend/components.md
    purpose: 前端组件结构
    tags: [frontend, component]
    read_when: [frontend_change, ui_feature]

  - path: docs/database/schema.md
    purpose: 数据库 schema
    tags: [database, schema]
    read_when: [database_change, migration]

# 任务类型 → 文档推荐映射
task_contexts:
  bug_fix:
    priority_docs:
      - docs/error_book.md
      - docs/dev_log.md
    tags: [debug, backend, frontend]
    
  new_feature:
    priority_docs:
      - docs/dev_plan.md
      - docs/features.md
      - docs/structure.md
    tags: [feature, full_stack]
    
  refactor:
    priority_docs:
      - docs/structure.md
      - docs/project_status.md
    tags: [architecture, backend, frontend]
```

### 4.2 AI 决策流程

```
任务输入
  ↓
解析任务类型（bug_fix / new_feature / refactor / unknown）
  ↓
查 project_index.yaml → 确定推荐 docs
  ↓
按需阅读（不强制读全部）
  ↓
如需具体文件，再查 structure.md 的目录映射
```

### 4.3 自管理 vs 轻依赖

**自管理方案（0依赖）**：
- 纯 YAML + Python 脚本（`project_index.yaml` 管理）
- AI 读取 YAML，根据 `read_when` 和 `tags` 决定阅读范围
- 缺点：YAML 需手动维护同步

**轻依赖方案（推荐）**：
- 用 sqlite 做增量索引（比 codegraph 轻量得多）
- Python 脚本扫描 docs 目录，建立索引
- AI 通过 SQL 查询"与 task 相关的 docs"
- 依赖：Python 3 + sqlite3（标准库，无需安装）

---

## 五、目录结构调整提案

### 现状

```
wcs-skill/
├── SKILL.md              # 英文版主技能
├── wcs/                  # 英文镜像
├── wcs-cn/               # 中文镜像（实际维护）
├── docs/                 # 仓库自身文档
│   ├── project_status.md
│   ├── structure.md
│   ├── dev_plan.md
│   ├── dev_log.md
│   └── ...
└── references/           # 模板
```

### 提案（删除英文版）

```
wcs-skill/
├── SKILL.md              # 中文版主技能（当前 wcs-cn/SKILL.md 提升上来）
├── docs/                 # 仓库自身文档
│   ├── project_index.yaml   # 新增：中枢文档
│   ├── project_status.md
│   ├── structure.md
│   ├── dev_plan.md
│   ├── dev_log.md
│   ├── features.md
│   ├── error_book.md
│   └── discussions/          # 新增：讨论存档（git 备份）
│       └── 2026-06-05-three-tier-docs-architecture.md
├── references/           # 模板
│   ├── core_docs_template.md
│   ├── workflow_checklists.md
│   ├── coding_standard_template.md
│   └── project_index_template.yaml  # 新增：中枢文档模板
└── scripts/              # 新增：轻量工具脚本
    └── index_docs.py    # 新增：docs 索引脚本
```

---

## 六、待讨论问题

1. **YAML vs SQLite**：中枢文档用纯 YAML 还是 SQLite？
   - YAML：0 依赖，人工维护
   - SQLite：轻依赖，自动索引

2. **project_index.yaml 的粒度**：是粗粒度（只有 path + purpose）还是细粒度（包含 tags、task_contexts 映射）？

3. **docs 自动发现 vs 手动注册**：docs 里的文档是 AI 自动扫描发现，还是必须在 project_index.yaml 里注册？

4. **三层架构的 AI 执行**：如何在 SKILL.md 里描述这个"先读中枢、按需读 docs"的流程？

5. **英文版删除时机**：是这次优化一起删，还是先优化再删？

---

## 七、下一步

- [ ] 确认三层架构方向
- [ ] 确定 YAML vs SQLite 选择
- [ ] 设计 project_index.yaml 结构
- [ ] 更新 SKILL.md 描述新的 AI 阅读流程
- [ ] 删除英文版 wcs/ 目录
