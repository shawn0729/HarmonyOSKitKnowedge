---
name: a2h-retrospect
description: 第五步：回顾本轮迁移，沉淀经验，优化 skill。分析 plan vs 实际差异，提取确定性修正和设计决策。双 Pipeline 经验对比。即使用户只说"回顾"或"优化"，也应触发。
---

# a2h-retrospect

## 1. 定位

Pipeline 层第五步，**闭环自优化**。让 Domain Skill 越用越好。

```
a2h-spec → a2h-plan → a2h-execute → a2h-verify → a2h-retrospect（本 skill）
                                                       │
                                                       ├─ 分析差异
                                                       ├─ 提取经验
                                                       ├─ 分类沉淀
                                                       └─ 生成回顾报告
```

**核心原则**：满足自动写入条件（频次 ≥3、修复一致、确定性 100%）的模式自动写入 skill references；不满足条件的仍暂存为 staged patch。

---

## 2. 输入

自动读取以下文件：

| 文件 | 用途 |
|------|------|
| `spec/plans/plan-*.md` | 计划：suggested_skills + task 列表 |
| `spec/migration-report.md` | 实际执行：skill 使用 + 覆盖记录 + 失败列表 |
| `spec/verify-report.md` | 验证结果：通过/失败项 |
| `spec/baseline/ui-manifest.md` | UI Pipeline 页面清单与 confidence 评估 |
| `git diff` (本轮迁移范围) | 代码变更全貌 |

如果 `spec/verify-report.md` 不存在，提示用户先执行 `a2h-verify`。

### 前置检查

执行 retrospect 前，自动检查输入文件是否就绪：

```
前置检查:
  │
  ├─ 1. spec/verify-report.md 存在？
  │     → 不存在: 提示 "请先执行 a2h-verify"，终止
  │
  ├─ 2. spec/migration-report.md 存在？
  │     → 不存在: 提示 "请先执行 a2h-execute"，终止
  │
  └─ 3. spec/plans/plan-*.md 存在？
        → 不存在: WARN "无 plan 文件，跳过 plan vs actual 对比"
```

所有检查通过后才开始分析流程。

---

## 3. 分析流程（5 步）

### Step 1: Plan vs 实际 Skill 使用差异 + Stage 对比

从 plan 提取 `suggested_skills`，从 migration-report 提取实际使用的 skill，比对：

```
Plan suggested_skills  vs  Migration-report actual_skills
  │
  ├─ 完全一致 → 标记 MATCH
  ├─ 被覆盖（升级）→ 标记 OVERRIDE，记录原因
  ├─ 被覆盖（降级）→ 标记 DOWNGRADE，标红分析
  └─ 未使用 → 标记 UNUSED，分析是否多余
```

输出 Skill 覆盖率 = MATCH 数 / 总 task 数。

#### Stage 对比分析

对比 Stage 1（UI Pipeline，a2h-activity-converter 直接转换）与 Stage 3 Step 3a（Feature Slice UI 补充转换）的转换质量：

```
Stage 1 (UI Pipeline) vs Stage 3 (Feature Slice UI supplement)
  │
  ├─ 页面范围对比:
  │   ├─ Stage 1 转换的页面列表（来自 ui-manifest.md confidence:high 页面）
  │   └─ Stage 3 Step 3a 转换的页面列表（来自 Feature Slice 中的 UI 任务）
  │
  ├─ 编译错误率对比:
  │   ├─ Stage 1 页面平均编译错误数
  │   ├─ Stage 3 页面平均编译错误数
  │   └─ 差异分析（哪种 Pipeline 产出更少编译错误）
  │
  └─ 保真度/准确度对比:
      ├─ Stage 1 页面 verify 通过率
      ├─ Stage 3 页面 verify 通过率
      └─ UI 还原度评估（布局、交互、样式的匹配程度）
```

### Step 2: 编译错误 Pattern 提取

从 `hmos_fix_build_errors` 的修复记录中提取可复用的编译错误模式：

```
编译错误日志
  │
  ├─ 分类:
  │   ├─ 类型错误（any / as / 类型不匹配）
  │   ├─ 导入错误（废弃模块 / 错误路径）
  │   ├─ API 错误（不存在 / 签名变更 / 废弃）
  │   ├─ 语法错误（ArkTS 特有限制）
  │   └─ 配置错误（module.json5 / build-profile.json5）
  │
  └─ 每个 pattern 提取:
      ├─ 错误特征（正则匹配）
      ├─ 修复方案
      └─ 出现频次
```

### Step 3: API 修正提取

从 `arkts-knowledge-verifier` 的验证记录中提取 API 修正：

```
Knowledge-verifier 日志
  │
  ├─ API 修正:
  │   ├─ 错误 API → 正确 API（替换映射）
  │   ├─ 废弃 API → 新 API（升级映射）
  │   └─ 不存在 API → 替代方案（新增映射）
  │
  └─ 每条修正提取:
      ├─ 原 API 签名
      ├─ 正确 API 签名
      └─ 修正原因
```

### Step 4: 分类

将 Step 2-3 的提取结果分为两类：

| 类型 | 定义 | 示例 |
|------|------|------|
| **确定性修正** | 100% 可自动应用的规则 | `@ohos.data.rdb` → `@kit.ArkData`; `file://` → `fd://` |
| **设计决策** | 需要人工判断的架构选择 | 选择 LazyForEach vs ForEach; 状态管理用 @StorageLink vs @Provide |

### Step 5: Confidence 准确度评估

对比 Phase A（a2h-spec）中对页面的 confidence 预测与实际转换质量，评估预测准确度：

```
ui-manifest.md confidence 预测  vs  实际转换结果
  │
  ├─ high confidence 页面:
  │   ├─ 转换顺利（符合预期）→ 标记 ACCURATE
  │   └─ 转换出现问题（编译错误多 / verify 失败）→ 标记 OVER_ESTIMATED
  │       → 标红，提取导致高估的原因，反馈改进 confidence 评估逻辑
  │
  ├─ medium confidence 页面:
  │   ├─ 转换顺利 → 标记 UNDER_ESTIMATED，可升级评估
  │   └─ 转换困难 → 标记 ACCURATE
  │
  ├─ low confidence 页面:
  │   ├─ 转换顺利 → 标记 UNDER_ESTIMATED，可升级评估
  │   └─ 转换困难 → 标记 ACCURATE
  │
  └─ 输出准确度指标:
      ├─ 总体准确率 = ACCURATE 数 / 总页面数
      ├─ 高估率 = OVER_ESTIMATED 数 / high confidence 页面数
      ├─ 低估率 = UNDER_ESTIMATED 数 / (medium + low) confidence 页面数
      └─ 各 confidence 等级的实际通过率分布
```

---

## 4. 两类沉淀

### 4a. 确定性修正 → 自动写入 Skill References

对于编译错误 pattern 和 API 修正中的确定性修正，满足条件时自动写入目标 skill 的 references/ 文件：

#### 自动写入条件（3 个条件全部满足）

1. **频次 ≥ 3**：同一模式在本轮或历史累计出现 ≥ 3 次
2. **修复方式一致**：每次出现的修复方案相同（非一事一议）
3. **确定性 100%**：无需人工判断，可机械应用

```
确定性修正
  │
  ├─ 检查 3 个条件
  │   ├─ 全部满足 → 自动写入 references/
  │   └─ 不满足   → 降级为 Staged Patch（暂存等待审核）
  │
  ├─ Step 1: 读取目标 references 文件
  │   检查是否已有相同 pattern
  │   ├─ 已存在 → 更新频次和日期
  │   └─ 不存在 → 追加新条目
  │
  ├─ Step 2: 写入 references 文件
  │   直接追加到对应 .md 文件末尾
  │
  └─ Step 3: 输出写入日志
      在回顾报告中记录自动写入的条目
```

#### References 目标 skill 映射

| 修正内容 | 目标 Skill | 写入文件 |
|---------|-----------|---------|
| 编译错误 pattern | `hmos_fix_build_errors` | `references/known-patterns.md` |
| API 映射修正 | `arkts-knowledge-verifier` | `references/api-corrections.md` |
| Symbol 验证 | `arkts-knowledge-verifier` | `references/verified-symbols.md` |
| 导入路径修正 | `arkts-knowledge-verifier` | `references/api-corrections.md` |
| 资源映射修正 | `android2hmos_resources_convert` | `references/` 对应文件 |
| 组件映射修正 | `arkts-component-builder` | `references/` 对应文件 |
| App 身份配置修正 | `arkts-app-identity` | `references/` 对应文件 |
| UI 模式修正 | `arkts-pattern-library` | `references/` 对应文件 |

#### 不满足条件的修正：Staged Patch

不满足自动写入条件的修正，仍使用 Staged Patch 方式暂存：

```
Staged Patch（降级路径）
  │
  ├─ 生成 .patch 文件到 .agents/skills/<target-skill>/references/
  ├─ 命名规则: <date>-<brief-description>.patch
  └─ 在回顾报告中标记 PENDING_REVIEW，等待用户审核
```

### 4b. 设计决策 → 变更摘要

对于需要人工判断的设计决策：

```
设计决策
  │
  ├─ Step 1: 列出变更摘要
  │   - 决策内容
  │   - 选择原因
  │   - 影响范围
  │
  ├─ Step 2: 等待人工审批
  │   用户确认后，才写入对应文件
  │
  └─ Step 3: 审批通过后写入
      目标: docs/development-experience.md 或对应 skill reference
```

### 4c. 关键经验 → Memory 系统

将本次迁移中值得跨会话复用的经验写入 Claude Code memory 系统：

```
经验类型筛选:
  │
  ├─ 确定性修正中出现 3+ 次的 pattern → 写入 feedback memory
  │   示例: "ArkTS 中不能用 @ohos. 前缀，必须用 @kit."
  │
  ├─ 设计决策中被用户审批通过的选择 → 写入 project memory
  │   示例: "LazyForEach 性能优于 ForEach，大列表场景始终使用 LazyForEach"
  │
  ├─ Skill 覆盖率分析中的 OVERRIDE 原因 → 写入 feedback memory
  │   示例: "有 Android 源码时，dispatcher 比直接调 component-builder 质量更高"
  │
  ├─ 双 Pipeline 对比结论 → 写入 feedback memory
  │   示例: "Stage 1 direct conversion produces better UI than Stage 3 re-creation"
  │
  └─ Confidence 准确度发现 → 写入 project memory
      示例: "confidence:medium pages with complete layout XML converted well"
```

Memory 写入格式遵循 auto memory 系统的规范（frontmatter + content）。

---

## 5. 增量学习模式

### 触发方式

`a2h-execute` 编译检查点后可选触发增量学习，无需等到完整 retrospect。

### 增量分析流程

```
编译修复完成
  │
  ├─ Step 1: 读取本次修复日志
  │   从 hmos_fix_build_errors 的修复记录中提取新 pattern
  │
  ├─ Step 2: 对比已有 references
  │   读取 known-patterns.md / api-corrections.md / verified-symbols.md
  │   │
  │   ├─ 已知模式 → 跳过（可选更新频次）
  │   ├─ 新模式 + 累计 ≥ 3 次 → 自动写入对应 reference
  │   └─ 新模式 + 累计 < 3 次 → 记录到计数器文件
  │
  └─ Step 3: 更新计数器
      写入 spec/retrospect-counter.json
```

### 临时计数文件

路径：`spec/retrospect-counter.json`

```json
{
  "last_updated": "2026-03-27T14:30:00Z",
  "pending_patterns": [
    {
      "id": "pattern-unique-id",
      "target_skill": "hmos_fix_build_errors",
      "target_file": "references/known-patterns.md",
      "error_signature": "错误特征描述",
      "fix_summary": "修复方案摘要",
      "count": 2,
      "first_seen": "2026-03-27",
      "last_seen": "2026-03-27",
      "examples": [
        { "file": "path/to/file.ets", "line": 42, "date": "2026-03-27" }
      ]
    }
  ]
}
```

### 自动晋升

当 `pending_patterns` 中某条记录的 `count` 达到 3：

1. 自动从 `pending_patterns` 中移除
2. 写入对应 skill 的 references 文件
3. 在回顾报告中记录 `AUTO_PROMOTED` 状态

---

## 6. 安全边界

**自动写入范围（满足 3 个条件时允许）**：
- 写入 `.agents/skills/*/references/` 中的 `known-patterns.md`、`api-corrections.md`、`verified-symbols.md`
- 追加新条目或更新已有条目的频次/日期

**绝对不做的事**：
- 不删除 references 文件中的已有条目
- 不直接修改 `docs/development-experience.md`
- 不直接修改 `docs/dev-pitfalls.md`
- 不自动 `git apply` .patch 文件

**降级为 Staged Patch 时的操作**：
- 生成 .patch 文件（新建文件，不覆盖已有文件）
- 输出变更摘要（在报告中列出）
- 提供 review 指引（告诉用户如何操作）

用户审核 Staged Patch 的命令示例：

```bash
# Review patch
cat .agents/skills/hmos_fix_build_errors/references/YYYY-MM-DD-import-fix.patch

# Apply patch
cd .agents/skills/hmos_fix_build_errors/references/
git apply YYYY-MM-DD-import-fix.patch
```

---

## 7. 回顾报告

存储路径：`docs/retrospect-report-YYYY-MM-DD.md`

```markdown
# 回顾报告

- 回顾时间: YYYY-MM-DD HH:mm
- 迁移报告: spec/migration-report.md
- 验证报告: spec/verify-report.md

## Skill 覆盖分析

- Skill 覆盖率: X% (MATCH: A, OVERRIDE: B, DOWNGRADE: C, UNUSED: D)

| Task | Plan 建议 | 实际使用 | 状态 | 覆盖原因 |
|------|----------|---------|------|---------|
| ... | ... | ... | MATCH/OVERRIDE/... | ... |

## 编译错误 Pattern

| Pattern | 错误特征 | 修复方案 | 频次 |
|---------|---------|---------|------|
| ... | ... | ... | X |

## API 修正

| 原 API | 正确 API | 修正原因 |
|--------|---------|---------|
| ... | ... | ... |

## 确定性修正 Patch

| Patch 文件 | 目标 Skill | 修正数 | 状态 |
|-----------|-----------|--------|------|
| .agents/skills/.../xxx.patch | hmos_fix_build_errors | 3 | PENDING_REVIEW |
| .agents/skills/.../yyy.patch | arkts-knowledge-verifier | 2 | PENDING_REVIEW |

## UI Pipeline vs Feature Pipeline 对比

| 维度 | Stage 1 (UI Pipeline) | Stage 3 (Feature Slice) | 优势方 |
|------|----------------------|------------------------|-------|
| 转换页面数 | X | Y | — |
| 平均编译错误数 | A | B | Stage X |
| verify 通过率 | C% | D% | Stage X |
| UI 还原度 | 高/中/低 | 高/中/低 | Stage X |
| 平均修复耗时 | Xmin | Ymin | Stage X |

**结论**: ...（Stage 1 直接转换 vs Stage 3 Feature Slice 补充的优劣总结）

## Confidence 准确度

| Confidence 等级 | 页面数 | ACCURATE | OVER_ESTIMATED | UNDER_ESTIMATED | 实际通过率 |
|-----------------|--------|----------|----------------|-----------------|-----------|
| high | X | A | B | — | C% |
| medium | X | A | — | B | C% |
| low | X | A | — | B | C% |
| **总计** | X | A | B | C | D% |

**高估案例**（需改进 confidence 评估）:
- Page: ... → 原因: ...

**低估案例**（可升级 confidence）:
- Page: ... → 原因: ...

## 设计决策

| 决策 | 选择 | 原因 | 影响范围 | 状态 |
|------|------|------|---------|------|
| ... | ... | ... | ... | PENDING_APPROVAL |

## 操作指引

### 审核并应用 Patch

\`\`\`bash
# 1. Review patch
cat <patch-file-path>

# 2. Apply (确认无误后)
git apply <patch-file-path>

# 3. Commit
git add -A && git commit -m "chore: apply retrospect patch <patch-name>"
\`\`\`

### 审批设计决策

确认上述设计决策后，告诉我"审批通过"，我会将决策写入对应文档。
```

---

## 8. 与 Domain Skill 的关系

a2h-retrospect 是**经验沉淀层**，分析以下 Domain Skill 的产出：

```
a2h-retrospect（沉淀层）
  │
  ├─ 分析 hmos_fix_build_errors 的修复记录 → 编译 pattern
  ├─ 分析 arkts-knowledge-verifier 的验证记录 → API 修正
  ├─ 分析 a2h-execute Stage 1 的 Agent 派发记录 → 覆盖率
  │
  └─ 沉淀到:
      ├─ hmos_fix_build_errors/references/    — 编译 pattern patch
      ├─ arkts-knowledge-verifier/references/ — API 映射 patch
      ├─ arkts-component-builder/references/  — 组件映射 patch
      └─ docs/retrospect-report-*.md          — 回顾报告
```

a2h-retrospect 不调用 Domain Skill 执行任何修改，只读取它们的产出进行分析。

---

## 9. 触发 Prompt 示例

```
回顾
```

```
优化 skill
```

```
总结这次迁移经验
```

```
分析下哪些可以改进
```

```
沉淀一下踩坑
```

```
有哪些 pattern 可以复用
```

自然语言触发时，a2h-retrospect 先检查 spec/verify-report.md 是否存在。如果不存在，提示用户先执行 a2h-verify。
