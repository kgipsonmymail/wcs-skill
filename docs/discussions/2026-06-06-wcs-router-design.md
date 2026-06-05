# WCS 路由器设计讨论

> 创建时间：2026-06-06
> 状态：**讨论中** — 从问题诊断到方案设计

---

## 一、问题诊断

### 1.1 现状：Modules 1-7 构建了知识库，没有构建执行引擎

Modules 1-7 产出了大量"数据"：

| 产出 | 类型 | 作用 |
|------|------|------|
| `project_index.yaml`（16 种任务类型） | 知识库 | 定义任务分类 |
| `task_states.md`（15 种任务状态） | 知识库 | 定义状态分支 |
| `skills_index.yaml`（81 个 skill） | 知识库 | 可用工具清单 |
| `doc_sync_checklist.md` | 规则 | commit 前检查项 |
| `scan_skills.py` | 工具 | 扫描 skill 索引 |
| `scan_structure.py` | 工具 | 扫描文件结构 |

**但没有任何文档定义**："AI 收到一个任务时，具体按什么顺序调用这些知识？"

### 1.2 症状：WCS 目前是 checklist，不是 router

当前 `wcs-cn/SKILL.md` 的结构是线性流程：

```
阶段0：初始化对齐
阶段1：门禁检查（读所有规范）
阶段2：实现
阶段3：验证
阶段4：文档同步
阶段5：交接
```

这是 **checklist**——告诉 AI"做这件事要过哪些关"。

WCS 的定位要求的是 **router**——告诉 AI"你这个任务属于哪类，该走哪条路，该带什么工具"。

### 1.3 根本原因

WCS 的定位（来自 `wcs-cn/SKILL.md`）：

> "每个开发任务**第一个激活它**，由它**分析任务**、**激活合适的 skill**、**引导阅读必要的 doc**、**定位需要的 file**"

关键词：**分析 → 激活 → 引导 → 定位**

这是**路由决策链**，不是**线性执行链**。

Modules 1-7 填充了"被路由的内容"（16种任务类型、81个skill等），但没有建立"路由决策机制"本身。

---

## 二、路由器的设计目标

### 2.1 核心职责

WCS 作为路由器，其核心职责是：

```
输入：用户的原始任务描述
      ↓
WCS 路由器
      ↓
输出：
  - 任务类型判定
  - 激活的 skill（可以是 0 个或多个）
  - 需要阅读的 doc 列表（按优先级排序，不是全部）
  - 需要定位的 file 路径（可选）
  - 建议的执行顺序
```

### 2.2 设计原则

**原则 1：路由决策优先于一切代码动作**

> 任何代码变更之前，必须先完成路由决策。未完成路由不得执行任何代码操作。

**原则 2：按需激活，不是全部加载**

> 不激活不需要的 skill，不阅读不相关的 doc。避免 token 浪费。

**原则 3：路由结果可追溯**

> 每次路由决策记录到交接文档，便于后续 AI 接续。

**原则 4：路由是可配置的**

> 项目可自定义 `project_index.yaml`，覆盖默认的路由规则。

---

## 三、路由决策流程设计

### 3.1 提议的三阶段模型

```
┌─────────────────────────────────────────────────────────────┐
│ 阶段 0：任务接收（Route）                                     │
│                                                             │
│ 输入：用户原始描述                                             │
│ 动作：                                                       │
│   1. 解析任务意图（what does user want?）                    │
│   2. 读取项目中枢索引（project_index.yaml）                   │
│   3. 匹配任务类型（task_contexts）                            │
│   4. 匹配任务状态（task_states）                              │
│   5. 输出：路由决策包（task_type + skills_to_activate +      │
│              docs_to_read + files_to_locate）               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 阶段 1：准备（Prepare）← 按路由决策包的指引执行                │
│                                                             │
│   - 激活必要的 skill                                         │
│   - 按优先级阅读必要的 doc（不是全部）                         │
│   - 定位需要的文件                                           │
│   - 完成开发前置门禁（但只针对当前任务相关的部分）               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 阶段 2：执行（Execute）← 交给对应的 skill 执行                 │
│                                                             │
│   - 实现功能 / 修复缺陷 / 重构等                              │
│   - WCS 保持监控，不替代执行                                  │
│   - 异常时接收 skill 的回调，决定是否路由到其他 skill           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ 阶段 3：验证与交接（Verify & Handover）                       │
│                                                             │
│   - 按 task_state 的要求执行验证                             │
│   - 更新相关 doc（按 doc_sync_checklist）                    │
│   - 输出交接文档（含路由结果追溯）                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 路由决策包的示例

假设用户说："给这个 API 加个 rate limiting"

```yaml
route_decision:
  task_type: enhancement
  task_state: enhancement_in_progress
  matched_context: api_rate_limiting
  skills_to_activate:
    - backend-self-test    # 优先级 1
  docs_to_read:
    - docs/CODING_STANDARDS.md    # 优先级 1（必须）
    - docs/architecture.md          # 优先级 2（建议）
    - docs/api_contract.md         # 优先级 3（如有）
  files_to_locate:
    - src/api/
    - src/middleware/
  recommended_order:
    - step1: read CODING_STANDARDS.md
    - step2: read architecture.md
    - step3: activate backend-self-test
    - step4: implement in src/api/
    - step5: verify with backend-self-test
```

---

## 四、待讨论的关键问题

### 4.1 路由决策谁来执行？

**选项 A：WCS 自己执行路由逻辑（内置）**

- 优点：WCS 加载时自带路由能力，不需要外部依赖
- 缺点：SKILL.md 的路由规则是静态的，无法动态更新

**选项 B：WCS 调用外部路由脚本（如 scan_router.py）**

- 优点：路由逻辑可以独立迭代，支持复杂推理
- 缺点：引入了额外的执行依赖

**选项 C：结合 A 和 B**

- 默认路由规则内置在 SKILL.md
- 复杂场景调用 `scripts/route.py`
- 项目可自定义 `project_index.yaml` 覆盖默认

### 4.2 `project_index.yaml` 的位置？

**当前**：`docs/project_index.yaml`（在 wcs-skill 自己的 docs/ 里）

**问题**：这个中枢索引应该属于 **wcs-skill 自身**，还是 **目标项目**？

- 如果属于 wcs-skill 自身 → WCS 只知道"有哪些 skill/doc"，不知道"目标项目的具体结构"
- 如果属于目标项目 → 每个项目需要维护自己的 `project_index.yaml`

**初步结论**：两者分离
- wcs-skill 的 `docs/project_index.yaml` → 定义"通用任务类型 → 通用 skill/doc 映射"
- 目标项目的 `docs/project_index.yaml` → 定义"项目特定的任务类型 → 项目特定的 doc/file 映射"
- WCS 加载时**先读目标项目的 `project_index.yaml`**，在此基础上叠加通用规则

### 4.3 如何避免"中枢索引 itself becomes a problem"？

codegraph 的问题是：维护一个实时索引本身就是负担。我们希望"AI 按需查，不需要实时同步"。

**初步结论**：采用"懒加载 + 按需更新"策略
- 中枢索引是**静态 YAML**，不是实时数据库
- AI 在路由时读取，不需要后台进程维持
- 当 AI 发现中枢索引与实际不符时，触发更新（类似于 doc_sync_checklist）

### 4.4 三层架构（skill → doc → file）的路由顺序？

```
skill 层：WCS 决定激活哪些 skill
   ↓
doc 层：skill 引导阅读哪些 doc
   ↓
file 层：doc 引导定位哪些 file
```

**问题**：路由决策是一次性完成，还是分阶段逐步细化？

**初步结论**：分阶段
- 阶段 0（Route）：一次性完成三层路由，输出完整的路由决策包
- 阶段 1（Prepare）：按路由决策包执行，遇到缺失时回滚到 Route 重新决策

---

## 五、行动项

- [ ] **讨论确认**：路由决策的执行方式（4.1）
- [ ] **讨论确认**：`project_index.yaml` 的分层策略（4.2）
- [ ] **讨论确认**：懒加载 vs 实时索引（4.3）
- [ ] **讨论确认**：一次性路由 vs 分阶段路由（4.4）
- [ ] **设计**：新的 SKILL.md 结构（router-first）
- [ ] **实现**：新的路由决策流程原型

---

## 六、参考资料

- `wcs-cn/SKILL.md`：当前 WCS 技能定义（待重构）
- `docs/project_index.yaml`：当前任务类型索引
- `docs/task_states.md`：当前任务状态定义
- `docs/discussions/2026-06-05-three-tier-docs-architecture.md`：三层架构原始讨论
