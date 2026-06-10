# 问题手册

> 遇到 bug/错误时，**立刻**在本文档写一条，不用等释放。
> 格式：**问题 / 调试时间 / 尝试过程 / 根因 / 解决 / 下次遇到**

---

## 当前已知问题

（无）

---

## 已归档条目

### .env 文件被 git 覆盖导致 API Key 丢失

**问题**：rebase 冲突导致 `.env` 被重置为占位符，所有 API Key 丢失
**调试时间**：1 小时
**尝试过程**：检查环境变量、查看 git log、追踪 .gitignore
**根因**：`.env` 被 git 跟踪但没有在冲突处理时被正确保留
**解决**：.env 文件应该始终被 .gitignore 忽略，不进版本控制
**下次遇到**：不要尝试从 git 恢复 .env，直接用 .env.example 重建
**记录时间**：2026-06-10

### marked v18 renderer 白名单验证规则

**问题**：`renderer 'footnote_def' does not exist` / `renderer 'alert' does not exist`
**调试时间**：0.5 小时
**尝试过程**：搜索所有 renderer 文件、对比旧版本、逐一排查
**根因**：marked v18 有白名单机制，自定义 renderer token 必须在白名单里注册才能被识别
**解决**：自定义 renderer 必须在 `src/renderer/index.ts` 的 `KNOWN_TOKENS` 列表里登记，包括 tokenizer 位置（顶部）和 renderer 位置（末尾）
**下次遇到**：自定义 renderer 不生效 → 先检查 KNOWN_TOKENS 列表
**记录时间**：2026-06-10

### @ts-expect-error 注释位置错误

**问题**：TypeScript 报错位置和 @ts-expect-error 注释行不一致，导致构建失败
**调试时间**：0.5 小时
**尝试过程**：在报错行上方逐行添加 @ts-expect-error 定位真正报错位置
**根因**：@ts-expect-error 必须精准加在**真正报错的行**上方，不能加在相关行上方
**解决**：报错信息指明的行号才是要加注释的位置，不是"看起来相关的行"
**下次遇到**：TypeScript 报错 → 直接在报错行加 @ts-expect-error，不要猜测
**记录时间**：2026-06-10

### CSS var() fallback 在变量未定义时不生效

**问题**：CSS `var(--md-text-color, #333)` 始终显示 #333，不是预期 fallback
**调试时间**：1 小时
**尝试过程**：检查 CSS 文件、刷新浏览器、网络请求
**根因**：CSS `var()` fallback 只有在变量"已定义但被覆盖"时才生效；如果变量根本不存在，fallback 是默认值，不是你写的值
**解决**：CSS 变量必须通过 `injectThemeCSS()` 在运行时注入到 `:root`，才能被 `var()` 正确读取
**下次遇到**：CSS 变量不生效 → 检查变量是否通过 injectThemeCSS 注入到 :root，不是只写在 CSS 文件里
**记录时间**：2026-06-10

### 删除功能后遗留文件导致构建失败

**问题**：`footnotes.ts` 已从代码删除但文件残留，导致 TypeScript 编译失败
**调试时间**：0.5 小时
**尝试过程**：搜索所有引用、清理 import、检查构建日志
**根因**：删了功能引用但忘记删除文件本身
**解决**：删除功能时，确保同时删除相关文件和目录，不要只清空代码
**下次遇到**：删了功能 → 同时删文件，git status 能发现残留文件
**记录时间**：2026-06-10

### console.log 调试日志残留

**问题**：`index.ts` 中的 `console.log` 调试输出忘记清理
**调试时间**：0.1 小时
**根因**：临时调试代码没有及时清理机制
**解决**：调试完成后立刻删除 console.log，不要"以后再清理"
**下次遇到**：提交前用 git diff 检查是否有残留 console.log
**记录时间**：2026-06-10

---

## 本次教训（2026-06-10）- 流程改进

**问题**：本次开发遇到的 6 个真实错误全部未进 errorbook

**根因**：errorbook 只有释放流程，没有积累流程。dev_log 成了垃圾堆，
所有经验散落各处（dev_log、mediary skill Pitfalls），没有能被下次直接复用的地方。

**改进**：errorbook 积累格式已固定为标准 5 字段格式，遇到问题立刻记。
