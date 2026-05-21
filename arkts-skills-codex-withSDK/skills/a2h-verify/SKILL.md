---
name: a2h-verify
description: 第四步：验证迁移产出。编译检查 + 静态分析 + 页面状态审计 + confidence 降级审查 + 功能验收。即使用户只说"验证"或"测试"，也应触发。
---

# a2h-verify

## 1. 定位

Pipeline 层第四步，**统一验证编排**。聚合多种验证手段，给出一份结构化的通过/失败报告。

```
a2h-spec → a2h-plan → a2h-execute → a2h-verify（本 skill）
                                        │
                                        ├─ 编译修复
                                        ├─ 静态分析
                                        ├─ 占位符扫描
                                        ├─ App 身份校验
                                        ├─ 页面状态审计（NEW）
                                        ├─ 功能验收（feature-index）
                                        ├─ UI 对齐（增强 + confidence 降级审查）
                                        ├─ Spec 覆盖率
                                        └─ 生成验证报告 + Retrospect 引导
```

**核心原则**：a2h-verify 是验证编排层，不实现修复逻辑，所有修复工作委托给 Domain Skill。验证失败时自动生成修复 plan 并回环到 a2h-execute，用户不需要手动重启流水线。

---

## 2. 输入

自动读取以下文件：

| 文件 | 用途 |
|------|------|
| `spec/baseline/ui-manifest.md` | 页面清单、优先级、confidence、页面状态 |
| `spec/baseline/feature-index.md` | 功能总索引、V1/V2 分配、依赖图 |
| `spec/baseline/plans/feature-plan.md` | 已执行的功能执行计划 |
| `spec/baseline/plans/ui-plan.md` | 已执行的 UI 转换计划 |
| `spec/baseline/ui/page_NNNN.md` | 各页面详细 UI Spec |
| `spec/baseline/features/F-xxx.md` | 各功能详细 Spec |
| `spec/migration-report.md` | a2h-execute 执行报告 |
| `spec/placeholder-registry.md` | 占位符注册表（如果存在） |
| `entry/src/main/ets/**/*.ets` | 迁移产出代码 |

如果 `spec/migration-report.md` 不存在，提示用户先执行 `a2h-execute`。

---

## 3. 验证清单

按顺序执行，每项产出独立的通过/失败状态：

### 3a. 全量编译修复

委托 `hmos_fix_build_errors`，自动循环最多 20 轮：

```
hmos_fix_build_errors（最多 20 轮）
  │
  ├─ 编译通过 → CHECK-1: PASS
  │
  └─ 20 轮仍失败 → 升级:
      ├─ 调用 arkts-knowledge-verifier 诊断
      │   ├─ 诊断后修复 → PASS
      │   └─ 仍然无法修复 → CHECK-1: FAIL（记录剩余错误列表）
      └─ FAIL 不阻塞后续检查项
```

### 3b. 静态分析

对所有 `.ets` 文件执行以下 grep 检查：

| 检查项 | 命令 | 严重级别 |
|--------|------|---------|
| `any` 类型 | `grep -rn ": any\b" --include="*.ets"` | ERROR |
| 废弃导入 | `grep -rn "from '@ohos\." --include="*.ets"` | WARN |
| SQL 拼接 | `grep -rn "'\s*+\s*" --include="*.ets"` 在 SQL 上下文中 | ERROR |
| `as` 类型断言 | `grep -rn " as " --include="*.ets"` | WARN |
| `eval()` | `grep -rn "eval(" --include="*.ets"` | ERROR |
| aboutToAppear 参数获取 | `grep -rn "aboutToAppear" --include="*.ets"` 中含 `pathInfo` | ERROR |

汇总结果：ERROR 0 + WARN 0 → CHECK-2: PASS，否则 CHECK-2: FAIL。

### 3b-2. 占位符扫描（必选）

两步扫描：

**Step 1: 结构化扫描** — 读取 `spec/placeholder-registry.md`
- 统计 pending 状态的占位符数量
- 对每个 pending 条目，检查目标页面/功能是否已在代码中实现
- 已实现但未回填 → 标记为"可回填未回填"

**Step 2: 兜底扫描** — grep 未注册的占位符
- `grep -rn "TODO:" --include="*.ets" entry/src/`
- `grep -rn "console.info('TODO:" --include="*.ets" entry/src/`
- 对比注册表，找出未注册的占位符并补录到注册表

**结果判定**：
- pending = 0 且无未注册项 → CHECK-3: PASS
- pending > 0 但均为 deferred（V2 范围外）→ CHECK-3: PASS（附 warnings）
- 存在可回填但未回填的项 → CHECK-3: FAIL

### 3b-3. App 身份校验（必选）

验证 App 配置文件中的身份信息不是模板默认值：

```
App 身份校验规则:
  │
  ├─ 1. app.json5 的 bundleName 不匹配 "com.example.*"
  │     → 匹配则 FAIL: "bundleName 仍是模板默认值"
  │
  ├─ 2. app.json5 的 vendor 不等于 "example"
  │     → 等于则 FAIL: "vendor 仍是模板默认值"
  │
  ├─ 3. app.json5 的 versionName 不等于 "1.0.0"
  │     → 等于则 WARN: "versionName 可能未从 Android 同步"
  │
  ├─ 4. string.json 的 app_name 与 Spec 记录一致（如果 feature-index.md 中有 App 名称定义）
  │     → 不一致则 FAIL: "app_name 与 Spec 不匹配"
  │
  ├─ 5. foreground.png / background.png 文件大小 > 1KB
  │     → ≤ 1KB 则 WARN: "图标文件疑似默认图"
  │
  └─ 6. layered_image.json 存在且引用 $media:background + $media:foreground
       → 缺失或引用错误则 FAIL: "自适应图标配置异常"
```

**结果判定**：
- 0 FAIL + 0 WARN → CHECK-4: PASS
- 0 FAIL + N WARN → CHECK-4: PASS (附 warnings)
- 任何 FAIL → CHECK-4: FAIL

### 3b-4. 页面状态审计（必选，NEW）

检查 `spec/baseline/ui-manifest.md` 中所有页面的 status 字段，按优先级分组审计。

**Step 1: 读取页面清单**

从 `ui-manifest.md` 的页面清单表格中提取每个页面的：
- 页面 ID
- 优先级（P0/P1/P2）
- 当前 status（pending / converted / verified / skipped）
- confidence（high / medium / low）

**Step 2: 按优先级分组统计**

| 优先级 | 总数 | verified | converted | pending | skipped |
|--------|------|----------|-----------|---------|---------|
| P0 | 统计 | 统计 | 统计 | 统计 | 统计 |
| P1 | 统计 | 统计 | 统计 | 统计 | 统计 |
| P2 | 统计 | 统计 | 统计 | 统计 | 统计 |

**Step 3: 逐页检查 .ets 文件存在性**

遍历 `spec/baseline/ui/page_NNNN.md`，读取每个页面 Spec 中记录的 ArkTS 目标文件路径，验证对应的 `.ets` 文件是否存在于 `entry/src/main/ets/` 下。

**结果判定**：
- P0 页面 100% verified → CHECK-5: PASS
- P0 页面有 converted 但未 verified → CHECK-5: FAIL（列出未验证的 P0 页面及当前状态）
- P0 页面有 pending → CHECK-5: FAIL（列出未转换的 P0 页面）
- P1 页面通过率 ≥ 80% → 附 info
- P1 页面通过率 < 80% → 附 warnings

### 3c. 功能验收

从 `spec/baseline/feature-index.md` 读取功能清单，逐项检查：

```
feature-index.md 功能列表
  │
  ├─ V1 项（必须通过）:
  │   ├─ 功能代码文件存在
  │   ├─ 路由/导航已注册
  │   ├─ ViewModel 已创建
  │   ├─ 数据层已接入
  │   └─ ...（从 feature-index.md 读取各功能验收标准）
  │
  └─ V2 项（可选通过）:
      ├─ 动画流畅
      ├─ 性能达标
      └─ ...
```

**验收方法**：

1. 读取 `spec/baseline/feature-index.md` 中的功能列表
2. 对每个 V1 功能 ID（F-xxx），读取 `spec/baseline/features/F-xxx.md` 中的验收标准
3. 自动化检查：
   - 文件是否存在：检查 `feature-plan.md` 中该功能对应的 output 文件
   - 路由注册：grep 相关 router 配置
   - 关键方法：grep @Component / async 方法名 / $r 引用
4. 无法自动化的项标记为"需人工验收"

每项通过自动化检查或标记为需要人工验收。

**结果判定**：
- V1 所有自动化检查项 PASS → CHECK-6: PASS
- V1 有 FAIL → CHECK-6: FAIL
- V2 项不影响 CHECK-6 判定

### 3d. UI 对齐验证（增强）

> **2026-04 更新**：CHECK-7 默认尝试 `arkts-visual-verify`（按页面截图闭环修复）。仅在前置条件不满足时降级到原有的 `arkts-ui-alignment + android-screenshot-analyzer` 静态对比。

```
UI 对齐验证:
  │
  ├─ 情况 A（首选，推荐）: adb/hdc 可用 + Android/HarmonyOS 双端模拟器在跑
  │   → 委托 arkts-visual-verify 执行按页面闭环验证
  │     依赖 spec/app-relationship-tree.json（缺失则 visual-verify 内部
  │     自动调用 app-relationship-tree skill 生成）
  │     单页流程：dumpLayout → 截图 → 多模态对比 → 修复代码 → 重新截图 → 收敛 → 下一页
  │   → CHECK-7: PASS 当所有 P0 页面 high 差异 = 0
  │
  ├─ 情况 B（降级）: 仅有 Android 静态截图（spec/ref/screenshots/ 或用户提供），无双端模拟器
  │   → 委托 arkts-ui-alignment + android-screenshot-analyzer 静态对比
  │   → 输出对齐度评分
  │   → CHECK-7: PASS if 对齐度 ≥ 80%
  │
  ├─ 情况 C: 仅 Android 项目路径可访问，无截图、无模拟器
  │   → 提示用户:
  │     "推荐方案：启动双端模拟器后由 arkts-visual-verify 自动闭环验证；
  │      备选方案：用 adb 命令批量截图 → 落到 spec/ref/screenshots/ → 走静态对比。
  │      adb shell screencap -p /sdcard/screen_<page>.png
  │      adb pull /sdcard/screen_<page>.png spec/ref/screenshots/"
  │   → CHECK-7: DEFERRED（非 SKIP）
  │
  └─ 情况 D: 无截图、无 Android 项目、无模拟器
      → CHECK-7: SKIP（保持现有行为）
```

**前置条件检测**（情况 A 的判定依据）：
- `which adb` 或 `find ~/Library -name adb` 返回非空
- `which hdc` 或 `find /Applications/DevEco-Studio.app -name hdc` 返回非空
- `adb devices` 列表中至少 1 个非 offline 设备
- `hdc list targets` 列表中至少 1 个目标
- 当前环境支持多模态读图

**confidence 感知增强**（情况 A、B 共用）：
- 对 `ui-manifest.md` 中 confidence: high 的页面，要求对齐度 ≥ 80%（情况 B）/ high 差异 = 0（情况 A）
- 对 confidence: medium 的页面，要求对齐度 ≥ 60% / 允许 ≤ 2 条 high 差异
- 对 confidence: low 的页面，不硬性要求对齐度，但记录实际评分

如有 `spec/baseline/ui/page_NNNN.md` 中包含 screenshot.png 引用，使用多模态 LLM 对比视觉还原度。

### 3d-2. confidence 降级审查（必选，NEW）

对 `ui-manifest.md` 中 confidence 为 medium 或 low 的页面，执行额外审查：

**Step 1: 提取待审查页面**

从 `ui-manifest.md` 筛选 confidence != high 的页面列表。

**Step 2: 逐页审查**

对每个 medium/low confidence 页面：
1. 检查对应 `.ets` 文件中 TODO 标记数量
2. 检查占位符注册表中该页面相关的 pending 条目数
3. 检查 UI 组件完整度（对比 `page_NNNN.md` 中定义的组件列表 vs 实际代码中的组件）
4. 评估实际转换质量：
   - **结构准确**：布局层级、组件类型基本匹配
   - **样式偏差**：布局正确但颜色/字号/间距有偏差
   - **TODO 标记较多**：超过 3 个 TODO 标记
   - **严重缺失**：缺少关键 UI 组件或交互逻辑

**Step 3: 生成建议**

| 实际转换质量 | 建议 |
|------------|------|
| 结构准确，样式偏差 | 人工审查样式细节 |
| TODO 标记较多 | 需人工补充 UI 数据 |
| 严重缺失 | 需重新提供页面数据后重新转换 |

**结果判定**：
- 所有 medium/low 页面已审查且无严重缺失 → CHECK-8: PASS（附审查列表）
- 存在严重缺失的页面 → CHECK-8: FAIL（列出需要重新处理的页面）
- 无 medium/low confidence 页面 → CHECK-8: SKIP

### 3e. Spec 覆盖率检查

检查 Spec 中定义的功能和页面是否都有对应的代码实现。

**UI 覆盖率**：
1. 读取 `spec/baseline/ui-manifest.md` 的页面清单
2. 对每个页面，检查 ArkTS 目标文件是否存在
3. 计算覆盖率 = 存在文件的页面数 / 总页面数

**功能覆盖率**：
1. 读取 `spec/baseline/feature-index.md` 的功能清单
2. 对每个功能 ID，检查 `feature-plan.md` 中对应 task 的产出文件是否存在
3. 检查关键方法/组件是否在文件中定义（grep @Component / async 方法名 / $r 引用）
4. 生成覆盖状态：
   - VERIFIED: 文件存在 + 关键实现存在
   - PARTIAL: 文件存在但关键实现缺失（可能是占位符）
   - MISSING: 文件不存在

**结果判定**：
- UI 覆盖率 100% + 功能 V1 VERIFIED 率 100% → CHECK-9: PASS
- UI 覆盖率 < 100% 或功能 V1 VERIFIED 率 < 100% → CHECK-9: FAIL
- 功能 V1 VERIFIED 率 ≥ 80% 且 < 100% → CHECK-9: FAIL（附差距列表）

### 3e-2. CHECK-10: 风格合规（条件执行）

**前置条件**: 读取 plan Context 中的 `Style` 字段。`style_set = none` 或字段缺失时跳过此检查（状态: SKIP）。

**执行逻辑**（`style_set != none` 时）：

1. 加载对应风格集的 orchestrator skill（如 `arkts-style-orchestrator`）
2. 对已生成的代码执行反模式扫描：
   - 命名规范：文件名、类名、变量名是否符合风格要求
   - Import 顺序：是否按风格规定的分组排序
   - UI tokens：是否使用了风格定义的颜色/间距/字体 tokens
   - 组件结构：是否遵循风格的组件内结构顺序（如 @Param → @Local → build → @Builder）
   - ViewModel 模式：业务逻辑是否正确提取到 ViewModel
3. 生成风格合规报告

**结果判定**：
- 无违规 → CHECK-10: PASS
- 有违规但均为 WARN 级别 → CHECK-10: PASS（附建议列表）
- 有 ERROR 级别违规 → CHECK-10: FAIL（附违规清单）

**注意**: CHECK-10 不纳入 V1 门控判定（Section 6），风格合规是建议性的，不阻断迁移完成。

### 3f. Retrospect 引导（必选）

验证报告生成后，自动输出引导信息：

```
验证完成后:
  │
  ├─ 全部通过:
  │   输出: "验证全部通过。建议执行 a2h-retrospect 提取本次迁移经验，
  │          优化 skill 以提升下次迁移效果。"
  │
  └─ 有失败项:
      输出: "存在失败项，请先处理。处理完毕后建议执行 a2h-retrospect。"
```

此步骤不执行 retrospect，仅提示用户。

### 3g. 生成统一验证报告

汇总以上所有检查结果，写入 `spec/verify-report.md`（模板见 Section 4）。

---

## 4. 验证报告模板

存储路径：`spec/verify-report.md`

```markdown
# 验证报告

- 验证时间: YYYY-MM-DD HH:mm
- 迁移报告: spec/migration-report.md

## 验证结果总览

| 检查项 | 编号 | 状态 | 详情 |
|--------|------|------|------|
| 全量编译 | CHECK-1 | PASS/FAIL | 编译轮数: X, 剩余错误: Y |
| 静态分析 | CHECK-2 | PASS/FAIL | ERROR: X, WARN: Y |
| 占位符扫描 | CHECK-3 | PASS/FAIL | pending: X, 可回填未回填: Y, 未注册: Z |
| App 身份校验 | CHECK-4 | PASS/FAIL | bundleName: X, vendor: X, version: X |
| 页面状态审计 | CHECK-5 | PASS/FAIL | P0 verified: X/Y, P1 verified: Z/W |
| 功能验收 | CHECK-6 | PASS/FAIL | V1 通过: X/Y, V2 通过: Z/W |
| UI 对齐 | CHECK-7 | PASS/FAIL/SKIP/DEFERRED | 对齐度: X% |
| confidence 降级审查 | CHECK-8 | PASS/FAIL/SKIP | medium: X, low: Y, 严重缺失: Z |
| Spec 覆盖率 | CHECK-9 | PASS/FAIL | UI: X%, 功能: Y% |
| 风格合规 | CHECK-10 | PASS/FAIL/SKIP | 违规: X (ERROR: Y, WARN: Z) |

## 门控判定

- V1 门控: PASS/FAIL
- 失败项: [列表]
- P0 页面全部 verified: YES/NO

## 详细结果

### CHECK-1: 全量编译
- 状态: PASS/FAIL
- 修复轮数: X
- 剩余错误: (如果 FAIL，列出错误)

### CHECK-2: 静态分析
| 文件 | 行号 | 检查项 | 级别 |
|------|------|--------|------|
| ... | ... | ... | ... |

### CHECK-3: 占位符扫描（摘要视图，完整数据见 spec/placeholder-registry.md）
| ID | 文件 | 类型 | 目标 | 状态 | 备注 |
|----|------|------|------|------|------|
| PH-001 | ... | navigation | ... | pending/resolved/deferred | ... |

### CHECK-4: App 身份校验
| 检查项 | 状态 | 值 | 说明 |
|--------|------|-----|------|
| bundleName | PASS/FAIL | com.xxx.yyy | ... |
| vendor | PASS/FAIL | xxx | ... |
| versionName | PASS/WARN | x.y.z | ... |
| app_name | PASS/FAIL | ... | ... |
| 图标文件 | PASS/WARN | foreground: XKB, background: YKB | ... |
| 自适应图标 | PASS/FAIL | layered_image.json | ... |

### CHECK-5: 页面状态审计

| 优先级 | 总数 | verified | converted | pending | skipped | 通过率 |
|--------|------|----------|-----------|---------|---------|--------|
| P0 | X | Y | Z | W | - | Y/X% |
| P1 | ... | ... | ... | ... | ... | ... |
| P2 | ... | ... | ... | ... | ... | ... |

未验证的 P0 页面:
| 页面 | 当前状态 | 原因 |
|------|---------|------|
| page_NNNN | converted | Step 3d 验证未通过 / 未执行 |
| page_MMMM | pending | Stage 1 转换失败 |

页面 .ets 文件存在性:
| 页面 | Spec 中定义的目标文件 | 文件存在 |
|------|---------------------|---------|
| page_NNNN | pages/XxxPage.ets | YES/NO |

### CHECK-6: 功能验收
| 功能 ID | 功能名称 | V 级别 | 状态 | 备注 |
|---------|---------|--------|------|------|
| F-001 | ... | V1 | PASS/FAIL | ... |
| F-002 | ... | V2 | PASS/SKIP | ... |

### CHECK-7: UI 对齐（如果执行）
| 页面 | confidence | 对齐度 | 阈值 | 状态 | 差异描述 |
|------|-----------|--------|------|------|---------|
| page_0001 | high | 85% | 80% | PASS | ... |
| page_0003 | medium | 65% | 60% | PASS | 样式细节偏差 |
| page_0015 | low | 40% | - | INFO | 仅供参考 |

### CHECK-8: confidence 降级审查
| 页面 | confidence | 实际转换质量 | TODO 数 | pending 占位符 | 建议 |
|------|-----------|------------|---------|--------------|------|
| page_0003 | medium | 结构准确，样式偏差 | 1 | 0 | 人工审查样式细节 |
| page_0015 | low | TODO 标记较多 | 5 | 2 | 需人工补充 UI 数据 |
| page_0022 | low | 严重缺失 | 8 | 4 | 需重新提供页面数据后重新转换 |

### CHECK-9: Spec 覆盖率

**UI 覆盖率**: X/Y (Z%)
| 页面 | Spec 定义 | 代码实现 | 状态 |
|------|----------|---------|------|
| page_NNNN | pages/XxxPage.ets | 存在 | COVERED |
| page_MMMM | pages/YyyPage.ets | 不存在 | MISSING |

**功能覆盖率**: A/B (C%)
| 功能 ID | 功能名称 | 代码实现 | 状态 |
|---------|---------|---------|------|
| F-001 | ... | VERIFIED | 文件存在 + 关键实现存在 |
| F-002 | ... | PARTIAL | 文件存在但关键实现缺失 |
| F-003 | ... | MISSING | 文件不存在 |

### CHECK-10: 风格合规（style_set != none 时）
- 状态: PASS/FAIL/SKIP
- 风格集: <style_set 值>
- 违规统计: ERROR X, WARN Y

| 文件 | 规则 | 级别 | 描述 |
|------|------|------|------|
| pages/XxxPage.ets | import-order | WARN | Import 顺序不符合风格规范 |
| components/YyyCard.ets | naming | ERROR | 文件名应为 PascalCase |
```

---

## 5. 验证失败回环

验证失败时**不终止流水线**，而是自动生成修复 plan 回环到 a2h-execute：

```
a2h-verify
  │
  ├─ 全部通过 → 输出报告，进入 a2h-retrospect
  │
  └─ 有失败项 → 自动回环:
      │
      ├─ Step 1: 从失败项提取修复任务
      │   ├─ 编译失败 → task: 编译修复 (hmos_fix_build_errors)
      │   ├─ 静态违规 → task: 修正违规代码 (knowledge-verifier)
      │   ├─ 占位符未回填 → task: 回填占位符代码
      │   ├─ App 身份异常 → task: 修正 App 配置 (arkts-app-identity)
      │   ├─ P0 页面未 verified → task: 补全页面功能验证
      │   ├─ 功能验收失败 → task: 补全缺失功能 (对应 skill)
      │   ├─ UI 不对齐 → task: UI 调整 (ui-alignment)
      │   ├─ confidence 降级严重缺失 → task: 重新采集数据 + 重新转换
      │   ├─ Spec 覆盖缺失 → task: 补全缺失实现
      │   └─ 风格合规失败 → task: 修正风格违规（加载对应风格 orchestrator）
      │
      ├─ Step 2: 生成修复 plan
      │   文件: spec/plans/plan-fix-<timestamp>.md
      │   格式: 与 a2h-plan 产出格式一致
      │
      ├─ Step 3: 委托 a2h-execute 执行修复 plan
      │
      └─ Step 4: 重新执行 a2h-verify（仅检查之前失败的项）
```

回环最多 3 轮。3 轮后仍有失败项，输出报告并提示用户手动介入。

---

## 6. 门控

**V1 门控标准**：

```
门控判定:
  │
  ├─ CHECK-1 全量编译: MUST PASS
  ├─ CHECK-5 页面状态审计: P0 页面 100% verified MUST PASS
  ├─ CHECK-6 功能验收: V1 项 100% PASS MUST PASS
  │
  以上三项全部通过？
  │
  ├─ 是 → 门控通过，可进入 a2h-retrospect
  │
  └─ 否 → 触发回环（Section 5），或提示用户手动介入
```

V2 级别验收项、P1/P2 页面、confidence 降级审查结果不阻塞门控，但记录在报告中作为后续优化方向。

---

## 7. 与 Domain Skill 的关系

a2h-verify 是**验证编排层**，编排以下 Domain Skill：

```
a2h-verify（编排层）
  │
  ├─ hmos_fix_build_errors    — 全量编译修复
  ├─ arkts-knowledge-verifier — 编译升级诊断 + 静态分析辅助
  ├─ arkts-ui-alignment       — UI 对齐验证（可选）
  ├─ arkts-app-identity       — App 身份校验
  └─ arkts-spec-evolver       — Spec 覆盖率审计（可选）
```

如果 Domain Skill 不存在或不可用，a2h-verify 跳过对应检查项，在报告中标记为 SKIP。

---

## 8. 触发 Prompt 示例

```
验证
```

```
测试一下
```

```
检查下迁移结果
```

```
跑一下验证
```

```
编译通过吗
```

```
检查代码质量
```

```
页面状态怎么样
```

```
P0 页面都验证了吗
```

自然语言触发时，a2h-verify 先检查 spec/migration-report.md 是否存在。如果不存在，提示用户先执行 a2h-execute。
