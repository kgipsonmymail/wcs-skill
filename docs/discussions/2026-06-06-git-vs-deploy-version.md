# Git 版本与部署版本的分离

## 问题背景

WCS 以 skill 形式存在，但 skill 本身也有"开发迭代"和"实际使用"两个生命周期。以往我们在同一套文件中混合了两种目的，导致：

- 维护 WCS 自身时不知道该改哪里
- 本地测试时不知道用的是哪个版本
- 开发版的文档污染了部署版

## 两个版本的定义

### Git 版本（wcs-skill 仓库）

- **位置**：`~/.hermes/skills/wcs-skill/`（即 Git 工作目录）
- **目的**：管理 WCS 自身的迭代和演进
- **用户**：正在开发 WCS 的 AI 或工程师
- **核心内容**：
  - `docs/`：讨论、规划、日志、实验记录
  - `wcs-cn/`：skill 源码（待发布的部署版 skill 内容）
  - `scripts/`：辅助脚本
  - `references/`：模板和索引文件

### 部署版本（安装到 Hermes 的实际 skill）

- **位置**：由 Hermes 平台决定，例如 `~/.hermes/skills/wcs-cn/` 或通过 symlink 指向 Git 版本的 `wcs-cn/`
- **目的**：被 AI 在日常开发任务中执行使用
- **用户**：执行开发任务的 AI
- **核心内容**：`wcs-cn/SKILL.md` 和必要的 `references/*.md`

## 关键区别

| 维度 | Git 版本 | 部署版本 |
|------|----------|----------|
| 受众 | 开发 WCS 的 AI | 执行任务的 AI |
| 包含讨论/规划文档 | 是 | 否 |
| 包含开发实验 | 是 | 否 |
| 包含 wcs-cn SKILL.md | 是（源码） | 是（symlink 或 copy） |
| 包含 prompt.txt（用户输入缓存） | 否 | 是 |
| 包含 error_book.md | 否（用 dev_log 代替） | 是 |

## 待讨论

1. **部署版的 `docs/` 应该放什么？**
   - 方案 A：部署版 `wcs-cn/` 下不包含 `docs/` 目录，只通过 symlink 引用 Git 版本的 docs
   - 方案 B：部署版有自己独立的 `docs/` 目录（只包含 `project_status.md`、`prompt.txt`、`error_book.md` 等实际执行时需要的文档）
   - 方案 C：完全不做目录分离，Git 版本即部署版本（当前状态）

2. **Git 版本的 docs/ 哪些内容属于部署版？**
   - `prompt.txt`：属于部署版，不应进入 git
   - `error_book.md`：属于部署版
   - `project_status.md`、`dev_log.md`、`dev_plan.md`：取决于项目是谁的项目——如果是 WCS 自身维护，则是 Git 版；如果是 AI 使用 WCS 时面对的具体项目，则是部署版

3. **本地测试流程**
   - 修改 Git 版本（wcs-skill/）中的 `wcs-cn/SKILL.md` 后，如何同步到本地部署的 skill？
   - 是否需要一个安装脚本？

4. **当前状态确认**
   - `docs/prompt.txt`：目前放在 Git 版本中，但内容是"用户输入缓存"，应属于部署版

## 讨论时间

待与用户进一步讨论后决定。
