# 仓库结构

> 本文件是文件结构网络的**提纲**，描述每个目录和关键文件的作用。
> 详细级别（函数/类型/依赖关系）在 `structure.d/` 子目录中按需维护。
> 动态维护规则：errorbook 纠正 bug 时，将排查到的文件和函数同步到对应的 subordinate doc。
> `structure.d/` 与 `scan_structure.py` 联动验证，防止结构老化过时。

---

## 顶层结构网络

```
wcs-skill/
├── wcs-cn/              # 部署版 skill（AI 实际加载）
├── docs/                # Git 版本治理文档
├── references/          # 模板和参考
├── scripts/             # 自动化脚本
└── .git/                # Git 版本控制
```

---

## 目录详情

### wcs-cn/

**作用**：部署版 skill。AI 执行任务时加载 `wcs-cn/SKILL.md`，不加载 Git 版本的 docs。

**Subordinate doc**：`structure.d/wcs-cn.yaml`

---

### docs/

**作用**：Git 版本治理文档。包括 project_index.yaml（中枢）、CODING_STANDARDS、workflow、features、structure 等所有基线文档。

**Subordinate doc**：`structure.d/docs.yaml`

---

### references/

**作用**：模板和参考文档。为项目提供标准模板（core_docs_template.md 等）。

**Subordinate doc**：`structure.d/references.yaml`

---

### scripts/

**作用**：自动化脚本。`scan_skills.py` 扫描本地 skills，`scan_structure.py` 扫描文件结构。

**Subordinate doc**：`structure.d/scripts.yaml`

---

## 顶层文件

| 文件 | 作用 |
|------|------|
| `SKILL.md` | WCS 主技能定义（根目录，name: wcs） |
| `README.md` | 仓库入口说明 |
| `LICENSE` | MIT 许可证 |

---

## 结构网络网络验证

使用 `scripts/scan_structure.py` 验证文档与实际结构的一致性：

```bash
# 扫描结构
python3 scripts/scan_structure.py . -v

# 验证 structure.d/ 与实际文件的一致性
# 缺失：structure.d/ 有记录但文件不存在 → 标记为"孤立条目"
# 冗余：scan 到但 structure.d/ 无记录 → 标记为"未归档文件"
```

**验证时机（满足任一即比对）：**
- 每次维护时
- scan_structure.py 有新的重要文件时
- 架构调整涉及文件增删时

**维护优先级：**
1. 关键文件（来自 bug 调试）> 目录结构（来自架构分析）
2. 不追求一次性填满，按需逐步积累
3. structure.d/ 的价值在于"维护时能快速知道文件在哪"

---

## Subordinate Docs 管理规则

### structure.d/ 目录结构

```
structure.d/
├── _index.yaml       # 结构索引（自动生成）
├── wcs-cn.yaml
├── docs.yaml
├── references.yaml
├── scripts.yaml
└── scan_verify.yaml   # 上次 scan_structure.py 验证结果
```

### structure.d/{模块}.yaml 格式

```yaml
模块: 模块名称
路径: docs/xxx
作用: 一句话描述

# 关键文件（动态维护，Bug 调试时补充）
关键文件:
  - path: src/pages/XXX.tsx
    作用: 做什么
    关键函数/类型:
      - ComponentName
      - useStoreName
  - path: backend/handler/xxx.go
    作用: 做什么
    关键函数/类型:
      - HandlerFunc

# 依赖关系（动态维护）
依赖: []
被依赖: []

# scan_structure.py 验证状态
scan_status:
  last_scan: null
  missing_files: []
  extra_files: []
```

---

## structure.d/ 现有条目

- ✅ wcs-cn.yaml — 关键文件: SKILL.md / references/
- ✅ docs.yaml — 关键文件: project_index.yaml / features.md / structure.md / error_book.md / features.d/ / structure.d/
- ✅ references.yaml — 关键文件: api_reference.md / coding_standard_template.md 等
- ✅ scripts.yaml — 关键文件: scan_skills.py / scan_structure.py（已含关键函数）
- ✅ scan_verify.yaml — 上次 scan_structure.py 验证结果（2026-06-10）

---

## structure.d/ ↔ features.d/ 联动机制

structure.d/ 和 features.d/ 从不同视角描述同一套系统，互相引用形成网络：

| structure.d/ 条目 | → 关联 features.d/ 条目 |
|-----------------|----------------------|
| wcs-cn.yaml | features.d/state-loading（SKILL.md 是状态加载执行体）；features.d/subagent闭环（SKILL.md 定义协作规范）；features.d/三层-docs-结构 |
| docs.yaml | features.d/errorbook（error_book.md 在 docs/ 下）；features.d/subagent闭环（dev_log.md 在 docs/ 下） |

**联动规则：**
- 当某个文件在 structure.d/ 的关键文件里出现时，对应的 features.d/ 条目也应包含该文件
- Bug 调试时：先从 features.d/ 定位功能网络，再从 structure.d/ 定位文件路径，双向印证
