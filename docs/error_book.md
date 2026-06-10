# 问题手册

> 遇到 bug/错误时，**立刻**在本文档写一条，不用等释放。
> 格式：**问题 / 调试时间 / 尝试过程 / 根因 / 解决 / 下次遇到**

---

## 当前已知问题

### blockToWechatHtml 两套渲染路径导致主题色不一致

**问题**：公众号版 shared 页面切换主题色后，有些加粗跟随主题色，有些始终黑色
**调试时间**：1.5 小时
**尝试过程**：
1. 确认 `default.css` 的 `.md-strong { color: inherit }` 存在
2. 确认 reading view 通过 `injectThemeCSS` 注入 `.md-strong { color: ${color} !important }`
3. 确认 shared 页面没有引入任何 CSS 文件（无 import，无 `injectThemeCSS` 调用）
4. 确认 shared 页面编译后的 `default.css` 里 `.md-strong{color:#6366f1}` 是硬编码 indigo，不是用户选择的主题色
5. 追溯 `blockToWechatHtml` 发现：paragraph/list/alert/blockquote 用 `renderInlineMarkdown`（inline style ✅），但 default case 和 table cells 用 `md()` → `renderMarkdownSync`（输出 `<strong class="md-strong">` ❌）
**根因**：`blockToWechatHtml` 内部有两套渲染机制——
- `renderInlineMarkdown(text, color)` → 调用 `marked.parseInline()` 直接处理文本，**inline style** 输出 `style="color:${color} !important;font-weight:bold;"`
- `md()` → `renderMarkdownSync(text)` → 调用 `marked.parse()` 全量渲染，**CSS class** 输出 `<strong class="md-strong">`

shared 页面没有引入 `default.css`，所以 `.md-strong` 没有颜色定义，显示默认黑色（而非主题色）。

reading view 之所以正常，是因为 `injectThemeCSS` 在 `:root` 注入 `.md-strong { color: ${color} !important }`，覆盖了 `default.css` 里的 `color: inherit`。

**解决**：`blockToWechatHtml` 的 default case（`blockToWechatHtml` 函数内 case "default"）和 table cells/th 全部改用 `renderInlineMarkdown(content, color)`，统一走 inline style 路径。同时删除废弃的 `md()` 函数和 `renderMarkdownSync` import。

**涉及文件**：
- `frontend/src/pages/SharedDocument.tsx` — `blockToWechatHtml` 函数，default case（第 619 行）、table td（第 603 行）、table th（第 595 行）
- `frontend/src/lib/md-renderer/themes/default.css` — `.md-strong` 定义（第 175 行）
- `frontend/src/lib/md-renderer/themes/index.ts` — `injectThemeCSS` 函数

**下次遇到**：主题色相关的问题 → 先确认是 inline style（`renderInlineMarkdown`）还是 CSS class（`renderMarkdownSync`）→ shared 页面没有 CSS 导入，只有 inline style 路径可用

**记录时间**：2026-06-11

---



---

## 已归档条目

### .env 文件被 git 覆盖导致 API Key 丢失

**问题**：rebase 冲突导致 `.env` 被重置为占位符，所有 API Key 丢失
**调试时间**：1 小时
**尝试过程**：检查环境变量、查看 git log、追踪 .gitignore、尝试 git stash 恢复
**根因**：`.env` 从创建第一天起就被 `.gitignore` 保护，从未进入 git 追踪范围。`git stash` 只能保存**已追踪文件**的改动，对 untracked 文件无效。操作链：git add → git stash → git pull --rebase → .env 被覆盖 → git stash pop → 什么都没恢复 → 错误重建为占位符
**解决**：.env 文件应该始终被 .gitignore 忽略，不进版本控制。本地备份才是唯一保护手段
**下次遇到**：不要尝试从 git 恢复 .env，从可信来源（用户、密码管理器）重新写入。重要文件操作前先 `git status` 确认，不要基于假设行动
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
