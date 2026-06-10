# 维护流程

## 受理

- 确认本次维护默认以 `wcs-cn/` 为主
- 确认仓库文档、规划和状态是否与当前技能内容一致
- 确认是否涉及发布、提交或远端同步

## 开发前置门禁

- 阅读 `docs/CODING_STANDARDS.md`
- 阅读 `wcs-cn/SKILL.md` 及相关 `wcs-cn/references/`
- 明确本次变更范围、验证方式和需要同步的文档

## 实施

- 优先维护 `wcs-cn/` 对应的中文说明和仓库级文档
- 如无用户明确要求，不围绕 `wcs/` 英文版展开额外整理
- 保持仓库描述与当前技能内容一致，不写脱离仓库事实的说明

## 验证

- 检查仓库结构和文档导航是否正常
- 检查规划、状态、功能、日志之间的术语是否一致
- 检查 Git 状态是否适合提交与推送

## 交接

- 记录本次维护范围、修改结果和验证情况
- 记录是否已提交、是否已推送
- 记录后续待办与已知风险

---

## Bug 阶段

遇到报错或问题时，使用以下标准排查流程：

### 第一步：定位关键文件

根据错误信息，先找最可能包含问题的文件：
- 前端报错 → `src/pages/` 或 `src/components/`
- API 报错 → `backend/handler/` 或 `backend/router.go`
- 类型报错 → `src/types/` 或相关 model 文件
- 构建报错 → `vite.config.ts` / `tsconfig.json` / `package.json`

不要猜测，先用错误信息里的关键词搜索文件。

### 第二步：定位关键代码

在确定的文件内找到报错的具体行/函数：
- 用错误堆栈定位行号
- 用关键词搜索函数名
- 确认是 tokenizer、renderer、handler 还是 store

### 第三步：查找关联代码

找到关键代码后，扩展搜索范围：
- 这个函数被谁调用？（搜索函数名）
- 这个文件 import 了什么？（查关联模块）
- 相关的配置文件在哪里？（如 theme、inject 函数）

**常见关联模式**：
- 前端渲染问题 → 同时查 `store` + `theme` + `vite.config.ts`
- API 问题 → 同时查 `router` + `handler` + `middleware`
- 构建问题 → 同时查 `tsconfig.json` + `package.json` + `vite.config.ts`

### 第四步：精准修改

在找到所有关联代码后，一次性修改到位：
- 不要只改一个文件就提交
- 确认关联文件的改动一致
- 改完后立即 `npm run build` 或 `go build` 验证

### Bug 阶段强制动作

1. **遇到错误立刻写 errorbook 条目**（不等释放）
2. **每次尝试失败都记录到 errorbook 的"尝试过程"**
3. **找到根因后，立刻更新 errorbook 的"根因"和"解决"字段**
