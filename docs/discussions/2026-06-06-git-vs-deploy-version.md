# Git 版本与部署版本的分离

## 已确认的决策（2026-06-06）

### 结论：git 版即部署版，不需要区分

- **Git 版本 = 部署版本**。推送到 GitHub 就是给别人下载的，安装到本地就是自己在用的。同一份文件，同一个目录。

### 目录结构确认

```
wcs-skill/                ← git 仓库根目录 = 部署版根目录
├── wcs-cn/              ← 实际被加载的 skill（name: wcs-cn）
│   ├── SKILL.md
│   ├── references/       ← skill 使用的模板文件
│   ├── assets/
│   └── scripts/
├── docs/                 ← WCS 自身迭代的文档（gitignore 不包含 docs/）
└── scripts/              ← 辅助脚本（skill 索引、结构扫描等）
```

### 删除的内容

- ~~`SKILL.md`~~（英文旧版入口，已删除）
- ~~`references/`~~（与 `wcs-cn/references/` 重复，已删除）

### 本地特有数据的处理

- 本地特有的数据（如 skill 管理信息）放到 `~/.hermes/` 下被 gitignore 的目录中
- 不上传 GitHub，保护隐私

### prompt.txt 的位置

- 用户开发项目的 `docs/prompt.txt`（AI 实际使用时读）
- 不放在 `wcs-cn/` 中（`wcs-cn/` 不含 `docs/`）

### references/ 的位置

- 只存在于 `wcs-cn/references/`（skill 内部）
- `wcs-cn/references/` 和 `wcs-cn/` 一起被安装

## 待讨论（已搁置）

~~1. 部署版 references/ 的同步机制~~
~~2. 根目录 SKILL.md 是否还有存在必要~~

以上议题已通过"git 版即部署版"决策一并解决。
