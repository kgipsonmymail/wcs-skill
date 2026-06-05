# Git 版本与部署版本的分离

## 已确认的决策

### 版本定义

- **Git 版本**（`~/.hermes/skills/wcs-skill/`）：管理 WCS 自身的迭代和演进。包含 `docs/`、`wcs-cn/` 源码、`scripts/`、`references/`。

- **部署版本**（`wcs-cn/SKILL.md`）：AI 实际执行任务时加载的 skill。**不包含 `docs/`**，只包含 `SKILL.md` 和 `references/`。

### prompt.txt 的位置

`docs/prompt.txt` 存在于两个地方：

1. **Git 版本的** `docs/prompt.txt`：`~/.hermes/skills/wcs-skill/docs/prompt.txt`（WCS 自身维护用）
2. **用户开发项目中的** `docs/prompt.txt`：AI 在每个项目 `docs/` 下维护（AI 实际使用时读）

### 部署版结构（wcs-cn/）

```
wcs-cn/
├── SKILL.md              # 部署版入口
└── references/           # 模板文件（从 Git 版本复制）
    ├── core_docs_template.md
    ├── workflow_checklists.md
    ├── coding_standard_template.md
    └── project_index_template.yaml
```

### Git 版本结构（wcs-skill/）

```
wcs-skill/
├── wcs-cn/               # 部署版源码（上游）
│   ├── SKILL.md
│   └── references/
├── docs/                 # WCS 自身维护用的文档
│   ├── prompt.txt       # 用户输入缓存（WCS 自用）
│   ├── error_book.md    # WCS 自身的问题记录
│   ├── project_index.yaml
│   ├── task_states.md
│   ├── dev_log.md
│   ├── dev_plan.md
│   ├── discussions/      # 重构讨论存档
│   └── ...其他文档
├── scripts/
├── references/           # 模板文件源
└── SKILL.md             # Git 版本入口（name: wcs）
```

### Git 版本 docs/ 的定位

Git 版本的 `docs/` 是 WCS **自身**维护用的文档，和 AI 在**用户项目**中维护的 `docs/` 是同一个概念——即 WCS 自身作为一个"项目"，用 WCS 管理自己。

### 部署版的 references/ 同步

部署版 `wcs-cn/references/` 应该与 Git 版本的 `wcs-cn/references/` 保持一致。更新流程：
1. 修改 Git 版本的 `wcs-cn/references/`
2. 部署时同步到各设备的 `wcs-cn/references/`

## 待确认

1. **部署版 references/ 的同步机制**：手动复制、symlink 还是安装脚本？
2. **Git 版本根目录的 SKILL.md**：`wcs-skill/SKILL.md`（name: wcs）是否还有存在必要？还是说只用 `wcs-cn/SKILL.md`（name: wcs-cn）就够了？
3. **error_book.md 的位置**：WCS 自身的问题记录放在 Git 版本的 `docs/` 中，这个决策已确认。
