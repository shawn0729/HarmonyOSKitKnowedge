# a2h Execute Prompt Templates

这份模板用于后续迁移新项目时，直接复制给 Codex / pipeline skills。

## 0. 变量占位

- `{ANDROID_SRC}`: Android 项目根目录
- `{HMOS_PROJECT}`: ArkTS/HarmonyOS 目标工程根目录
- `{STYLE_SET}`: 风格集；没有就填 `none`
- `{START_BATCH}`: 从哪个 batch 开始，例如 `Batch 1`
- `{START_STAGE}`: 从哪个 Stage 开始，例如 `Stage 1`

---

## 1. 新项目分析 Prompt

```text
@a2h-spec 分析并迁移 Android 项目 `{ANDROID_SRC}` 到 `{HMOS_PROJECT}`。

要求：
- 强制使用 .codex/agents 里的 agent
- Android 分析阶段优先使用 a2h-android-analyzer
- Phase A/B/C 产出写入 spec/baseline/
- 如果 ui-snapshots 缺少 view.xml 或 meta.json，先自动补齐再继续
- 所有页面先生成 ui-manifest 和分页 page spec，不要直接跳到本地直改
- style_set: {STYLE_SET}
```

---

## 2. 计划生成 Prompt

```text
@a2h-plan 基于当前 spec/baseline 生成执行计划。

要求：
- 输出 ui-plan.md 和 feature-plan.md
- UI 页面按 batch 分组
- Feature 按 Base Layer 和 Feature Slices 拆分
- 给出依赖关系、并行关系、每批预计 agent 数量
- style_set: {STYLE_SET}
```

---

## 3. 等我审批再执行 Prompt

```text
先执行 @a2h-plan 给我审批，不要直接进入 @a2h-execute。
审批后默认从 ui-plan 的第一个未完成 batch 开始。
```

---

## 4. 严格 Agent 执行 Prompt

```text
@a2h-execute 从 {START_BATCH} 开始，强制使用 .codex/agents。

执行约束：
- Stage 1 只允许 a2h-activity-converter
- 每页只允许改自己的 output_file
- 不允许主执行器本地直改页面兜底
- Batch 完成后必须在主工作区编译
- 编译失败先按 output_file ownership 回灌给对应 page agent 修
- 共享文件问题单独建 task，不要混进单页 agent
- 缺失 string/resource/公共组件时先报告，不要越权改文件
```

---

## 5. 从中断点继续 Prompt

```text
@a2h-execute 从 {START_STAGE} 继续执行，强制使用 .codex/agents。

继续前先做：
- 读取 ui-manifest.md / feature-plan.md 判断未完成项
- 检查 git status，确认是否有 agent 半写入或误删文件
- 如果有损坏页面，先恢复并重派发对应 page agent

继续规则：
- 保持原 ownership，不要改成主执行器本地修
- 先完成当前 batch / slice，再进入下一个
```

---

## 6. 只重试失败页面 Prompt

```text
@a2h-execute 只重试 Stage 1 失败页面，强制使用 .codex/agents。

要求：
- 只重派发 FAILED 或编译不过的页面
- 沿用原 output_file ownership
- 先修页面自身错误，再做 batch compile
- 不要重跑已经通过编译的页面
```

---

## 7. 执行完成后验证 Prompt

```text
@a2h-verify 验证本轮迁移结果。

要求：
- 在主工作区编译检查
- 审计 ui-manifest 页面状态
- 检查 placeholder-registry 是否完整
- 汇总本轮新增的编译错误模式和页面差异风险
```

---

## 8. 迁移回顾 Prompt

```text
@a2h-retrospect 回顾本轮迁移，并优化 skill / agent。

重点关注：
- plan vs actual 是否偏离
- 哪些页面如果不走 a2h-activity-converter 会明显退化
- 本轮出现的 ArkTS 编译错误模式
- 哪些规则应该固化到 a2h-execute 和 agent prompt
```

---

## 9. 一套最稳的完整顺序

```text
1. @a2h-spec 分析 `{ANDROID_SRC}`
2. @a2h-plan 生成计划
3. 我审批 ui-plan / feature-plan
4. @a2h-execute 从 Batch 1 开始，强制使用 .codex/agents
5. @a2h-verify 做主工作区验证
6. @a2h-retrospect 沉淀经验并优化 skill / agent
```
