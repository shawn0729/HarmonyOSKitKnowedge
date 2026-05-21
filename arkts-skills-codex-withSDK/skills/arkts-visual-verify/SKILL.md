---
name: arkts-visual-verify
description: 按页面粒度自动截图对比验证。在 Android 和 HarmonyOS 模拟器上逐页截图，用多模态模型对比视觉差异，自动修复代码直到收敛，每页独立闭环后再进入下一页。当用户说"截图对比"、"视觉验证"、"检查 UI 一致性"时触发。需要 adb/hdc 可用且两个模拟器已运行。依赖前置 skill app-relationship-tree。
---

# arkts-visual-verify — 按页面截图对比闭环

## 1. 定位

a2h-verify CHECK-7 的增强执行器。按 **单页面闭环** 模式在两端模拟器上截图，用多模态模型对比视觉差异，自动修复代码，单页收敛后再进入下一页。

> **前置 Skill**: 本 skill 依赖 `app-relationship-tree` skill 生成的 `spec/app-relationship-tree.json` 作为核心输入（页面清单、导航关系、组件树、功能域）。如该文件不存在，Phase 1 会自动调用前置 skill 生成。

```
功能清单（P0 优先）
  │
  ├─ Phase 1.5: 批量代码扫描预修复（新增）
  │     grep 通用问题 → 批量修复 → 编译验证
  │
  ├─ 页面 1: Android 截图 vs HarmonyOS 截图
  │     ↓
  │   dumpLayout 获取精确坐标 → 导航链路到达目标页
  │   → 截图 → 崩溃检测 → 多模态对比 → 差异清单
  │   → 修复代码 → 重新截图 → 再对比
  │   单页收敛（无 high 差异）→ 进入下一页
  │
  ├─ 页面 2: ...（同上）
  └─ ...
        ↓
  生成汇总报告
```

**核心原则：每次只处理一个页面，截图 → 对比 → 修复 → 验证，闭环后再进入下一页。**

---

## 2. 前置条件

执行前必须验证以下条件，任何一项不满足则中止并提示用户：

| 条件 | 验证命令 | 失败提示 |
|------|---------|---------|
| adb 可用 | `which adb` 或 `find ~/Library -name adb` | "请安装 Android SDK 并确保 adb 在 PATH 中" |
| hdc 可用 | `which hdc` 或 `find /Applications/DevEco-Studio.app -name hdc` | "请安装 HarmonyOS SDK 并确保 hdc 在 PATH 中" |
| Android 模拟器运行中 | `adb devices \| grep -v "List"` | "请启动 Android 模拟器" |
| HarmonyOS 模拟器运行中 | `hdc list targets` | "请启动 HarmonyOS 模拟器" |
| Android APK 已安装 | `adb shell pm list packages \| grep {package}` | "请先安装 Android APK 到模拟器" |
| HarmonyOS HAP 已安装 | `hdc shell bm dump -n {bundleName}` | "请先部署 HarmonyOS HAP 到模拟器" |
| `app-relationship-tree.json` 存在 | `test -f spec/app-relationship-tree.json` | **自动调用** `app-relationship-tree` skill 生成（见 Step 1.0） |
| 多模态模型可用 | 尝试读取一张图片 | "当前环境不支持多模态，无法执行视觉对比" |

> **hdc 路径备注**：DevEco Studio 自带 hdc 通常位于
> `/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc`，
> 可用 `HDC=$(find /Applications/DevEco-Studio.app -name hdc | head -1)` 动态获取。

> **hdc 连接备注**：远程模拟器需要先连接：`hdc tconn 127.0.0.1:5557`。

---

## 3. 输入

| 输入 | 来源 | 说明 |
|------|------|------|
| `app-relationship-tree.json` | `spec/app-relationship-tree.json` | **首选**页面清单 + 导航关系 + 功能依赖图 |
| `feature-index.md` | `spec/baseline/feature-index.md` | 功能清单 + 优先级（备选，当 app-relationship-tree.json 不存在时使用） |
| `features/F-xxx.md` | `spec/baseline/features/` | 每个功能的涉及页面列表 |
| `ui/page_NNNN.md` | `spec/baseline/ui/` | 每个页面的 Android Activity + ArkTS 页面路径 |
| `ui-manifest.md` | `spec/baseline/ui-manifest.md` | 页面清单 + 状态 |
| `app.json5` | HarmonyOS 项目 | bundleName |
| `AndroidManifest.xml` | Android 项目 | package 名 + Activity 列表 |
| `ui_interaction_log.json` | 项目根目录 | 验证进度持久化（如存在则读取，断点续跑） |

---

## 4. 执行流程

### Phase 1: 准备

**Step 1.0: 确保 app-relationship-tree.json 存在（前置 Skill 调用）**

```
IF NOT exists("spec/app-relationship-tree.json"):
  打印: "⚠️ app-relationship-tree.json 不存在，自动调用前置 skill 生成..."
  
  调用 app-relationship-tree skill:
    该 skill 会自动探测可用数据源（page spec / graph-builder 产件 / ArkTS 源码），
    按 7 Phase 流水线生成完整关系树。
    
    典型执行路径:
      Phase 1: 探测数据源
      Phase 2: 从 design_ref.md + page spec 生成 features + dependency_graph
      Phase 3: 从 80 个 page_NNNN.md 聚合 navigation + state_variables
      Phase 4: 从 ArkTS 源码并行提取 sub_components（4 Agent 批次）
      Phase 5: 提取 Fragment 深层结构
      Phase 6: 交叉校验
      Phase 7: 写入 spec/app-relationship-tree.json
    
    预计耗时: ~10 分钟
  
  IF 生成失败:
    中止并提示: "app-relationship-tree.json 生成失败，请检查数据源（至少需要 spec/baseline/ui/ 或 ArkTS 源码）"
  ELSE:
    打印: "✓ app-relationship-tree.json 已生成（{total_pages} 页, {total_components} 组件）"
    继续 Step 1.1

ELSE:
  打印: "✓ app-relationship-tree.json 已存在，直接使用"
  
  # 可选：检查是否过期（如果源码有大量变更）
  TREE_DATE = app-relationship-tree.json.app.generated_at
  RECENT_CHANGES = git diff --name-only --since={TREE_DATE} -- 'entry/src/main/ets/'
  IF RECENT_CHANGES > 10 files:
    提示用户: "关系树生成于 {TREE_DATE}，之后有 {N} 个源文件变更，是否需要重新生成？"
```

**Step 1.1: 验证前置条件**

逐项检查 Section 2 中的条件。全部通过后继续。

**Step 1.2: 构建页面截图队列**

从 `app-relationship-tree.json` 构建（Step 1.0 已确保文件存在）：

```
1. 读取 pages 列表和 dependency_graph.layers
2. 按层级排序: Foundation → Auth → Monetize → Core AI → Extended → Shell
3. 每层内按页面名称字母序排列
4. 使用 pages[].sub_components 中的 trigger/target 信息辅助确定导航路径
5. 使用 features[].pages 确定每个页面的优先级（P0/P1/P2）
```

**Step 1.2.5: 页面可达性预分类（必选）**

对队列中每个页面，判断可达性并分类：

```
FOR EACH page IN queue:
  1. grep 页面代码是否包含 login/token 检查:
     grep -l "LoginPage\|isLogin\|checkLogin\|token" {page}.ets
  2. 检查 app-relationship-tree.json 中的依赖关系:
     - 依赖 F002(Auth) 的功能所属页面 → login_walled
  3. 检查页面是否需要前序参数:
     grep "RouterUtils.getParamByName\|context.pathInfo.param" {page}.ets
     - 有参数依赖且无默认值 → data_dependent
  4. 分类结果:
     - public: 无需登录、无需参数，可直接导航到达
     - login_walled: 需要登录才能访问
     - data_dependent: 需要前序页面传参（detail 页、result 页等）

处理策略:
  - public 页面: 执行完整 Phase 2（截图 → 对比 → 修复）
  - login_walled 页面: 仅执行 Phase 1.5 代码扫描，status 标记为 "skip"，reason = "login_required"
  - data_dependent 页面: 仅执行 Phase 1.5 代码扫描，status 标记为 "skip"，reason = "requires_params"
```

**Step 1.3: 创建输出目录与进度文件**

```bash
mkdir -p spec/visual-verify/screenshots/android
mkdir -p spec/visual-verify/screenshots/harmony
```

初始化或恢复进度文件 `spec/visual-verify/progress.json`：

- **若文件不存在**：创建初始结构，`queue_remaining` 填入全部待检页面（按层级排序）
- **若文件已存在**：直接读取，**跳过** `pages` 中 `status` 为 `pass`/`skip`/`blocked` 的页面，仅处理 `queue_remaining` 中的页面

```json
{
  "last_updated": "<ISO8601>",
  "project": "<bundleName>",
  "max_rounds_per_page": 5,
  "pages": {},
  "queue_remaining": ["Index", "HomePage", ...],
  "reachability": {
    "public": ["Index", "HomePage", "MineSettingPage", ...],
    "login_walled": ["CreateCoinPage", "WebMemberCenterPage", ...],
    "data_dependent": ["VideoDetailsPage", "ChatPaintDetailsPage", ...]
  }
}
```

> **断点续跑规则**：每次执行 Phase 2 前先读 `progress.json`，已有结论的页面直接跳过，不重复截图。同时读取 `ui_interaction_log.json`（如存在），其中 `fixes_applied` 和 `page_status` 可作为辅助跳过依据。

---

### Phase 1.5: 批量代码扫描预修复（必选，在逐页截图前执行）

在进入逐页截图之前，先对所有 `.ets` 文件执行一轮批量 grep 扫描，修复高频通用问题。**此阶段效率远高于逐页截图发现问题**（实测：5 分钟发现 15+ 问题 vs 逐页截图 2 小时发现 3-4 个问题）。

**扫描项：**

| # | 扫描目标 | grep 命令 | 修复方法 | 严重级别 |
|---|---------|----------|---------|---------|
| 1 | 标题栏缺少状态栏避让 | `grep -rn "\.height(56)" --include="*.ets"` 且同一 Builder 中无 `padding.*top.*42` 和无 `marginTop` | 添加 `.padding({ top: 42 })` | HIGH |
| 2 | 英文占位符文本 | `grep -rn "Text('.*[A-Za-z].*')" --include="*.ets"` 排除资源引用和变量 | 替换为中文或 LoadingProgress | HIGH |
| 3 | 可见 TODO 文本 | `grep -rn "Text('TODO\|Text(\`TODO" --include="*.ets"` | 替换为合适的占位 UI | HIGH |
| 4 | 缺少 NavDestination 包裹 | `build()` 后直接是 `Column()`/`Stack()`/`Row()` 而非 `NavDestination()` 的页面（排除 Index、SplashPage） | 用 NavDestination 包裹，添加 `.hideTitleBar(true)` 和 `.onReady()` | HIGH |
| 5 | aboutToAppear 中读取路由参数 | `grep -rn "aboutToAppear" --include="*.ets"` 中包含 `getParamByName\|pathInfo` | 迁移到 `NavDestination.onReady` 回调中 | MEDIUM |
| 6 | 使用已知 broken 的 RouterUtils.pop() | `grep -rn "RouterUtils.pop\|RouterUtils\.pop" --include="*.ets"` | 替换为 `this.pathStack.pop()` | HIGH |

**执行流程：**

```
FOR EACH scan_item IN scan_list:
  1. 执行 grep 扫描
  2. 对每个命中结果，读取上下文确认是否真正需要修复
  3. 应用修复
  4. 记录到 scan_fix_log

扫描完成后:
  1. 统一执行编译验证（hmos_fix_build_errors）
  2. 输出扫描修复摘要:
     "Phase 1.5 批量扫描: 扫描 N 个文件，发现 M 个问题，修复 K 个"
  3. 将修复记录写入 ui_interaction_log.json 的 fixes_applied
```

---

### Phase 2: 单页面截图 → 对比 → 修复闭环

**仅对 Step 1.2.5 分类为 `public` 的页面执行。对页面队列中每个页面，依次执行以下完整闭环，前一页收敛后再处理下一页：**

---

#### Step 2.0: 导航到目标页面（导航链路模式）

采用从首页逐步导航的方式到达目标页面，而非直接跳转。这种方式同时验证了导航链路的正确性。

**Android 端导航：**

```bash
# 强制停止 App，排除上次残留状态
adb -s {device} shell am force-stop {package}
sleep 1

# 重新冷启动到主入口
adb -s {device} shell am start -n "{package}/{launcher_activity}" -W
sleep 5  # 等待 Splash + 初始化完成

# 逐层 dismiss 启动弹窗（循环检查，最多 5 次）
for i in 1 2 3 4 5; do
  CURRENT=$(adb -s {device} shell dumpsys activity top | grep "mResumedActivity" | head -1)
  if echo "$CURRENT" | grep -q "{target_activity}"; then
    break  # 已到达目标页面
  fi
  adb -s {device} shell input keyevent KEYCODE_BACK
  sleep 1
done

# 按导航路径逐步点击到达目标页面
# 坐标从 dumpsys 或 uiautomator dump 获取
```

**HarmonyOS 端导航（导航链路模式）：**

```bash
# 强制停止 App
hdc shell aa force-stop {bundleName}
sleep 1

# 冷启动到主入口
hdc shell aa start -a EntryAbility -b {bundleName}
sleep 9  # 等待 Splash 消失（根据 splash_wait_seconds 配置）

# Step 2.0.5: 布局分析 — 获取精确坐标（必选）
hdc shell uitest dumpLayout
# 解析返回的 layout JSON，提取目标元素的 bounds
# 计算中心点坐标 = ((left + right) / 2, (top + bottom) / 2)
# ⚠️ 禁止使用目测坐标，必须从 dumpLayout 获取

# 按导航路径逐步点击到达目标页面
# 示例：首页 → 我的 tab → 设置图标 → 目标设置子页
hdc shell uitest uiInput click {tab_x} {tab_y}        # 切换 tab
sleep 1
hdc shell uitest dumpLayout                              # 重新获取布局
# 解析新布局，获取下一个点击目标的坐标
hdc shell uitest uiInput click {target_x} {target_y}   # 点击目标
sleep 2
```

**导航路径确定规则：**

```
1. 从 app-relationship-tree.json 读取页面所属功能域和导航关系
2. 确定从首页到目标页面的最短导航路径
3. 常见路径模式:
   - 首页工具格子 → 功能页: 点击对应工具图标
   - 我的页子页: tab切换到"我的" → 点击对应入口
   - 设置子页: 我的 → 设置图标 → 点击对应设置项
   - 详情页: 先导航到列表页 → 点击某一项（data_dependent 页面通常跳过）
4. 每次导航前必须执行 dumpLayout 获取精确坐标
```

**返回键：**

```bash
# HarmonyOS 返回键
hdc shell uitest uiInput keyEvent Back

# Android 返回键
adb shell input keyevent KEYCODE_BACK
```

---

#### Step 2.1: 截图

**Android 端：**

```bash
adb -s {device} shell screencap -p "/sdcard/vv_{page_id}.png"
adb -s {device} pull "/sdcard/vv_{page_id}.png" \
  "spec/visual-verify/screenshots/android/{page_id}.png"
adb -s {device} shell rm "/sdcard/vv_{page_id}.png"
```

**HarmonyOS 端（注意：必须用 `.jpeg` 后缀，`snapshot_display` 不支持 `.png`）：**

```bash
hdc shell snapshot_display -f "/data/local/tmp/vv_{page_id}.jpeg"
hdc file recv "/data/local/tmp/vv_{page_id}.jpeg" \
  "spec/visual-verify/screenshots/harmony/{page_id}.jpeg"
hdc shell rm "/data/local/tmp/vv_{page_id}.jpeg"
```

**截图完整性验证：**

```
android_ok = exists AND size > 10KB
harmony_ok = exists AND size > 10KB
如两端任一缺失 → retry once，仍失败则 skip 并记录
```

---

#### Step 2.1.5: 崩溃检测（每次截图后必须执行）

截图后立即检测应用是否崩溃：

```bash
# HarmonyOS 崩溃检测
FOREGROUND=$(hdc shell aa dump -a 2>/dev/null | grep "mission name" | head -1)
if ! echo "$FOREGROUND" | grep -q "{bundleName}"; then
  # 应用已崩溃，回到了桌面或其他应用
  echo "CRASH DETECTED on page: {page_id}"
  
  # 记录崩溃
  status = "blocked"
  reason = "app_crash"
  
  # 重新启动应用
  hdc shell aa start -a EntryAbility -b {bundleName}
  sleep 9
  
  # 跳过当前页面，进入下一页
  continue
fi

# Android 崩溃检测
CURRENT=$(adb -s {device} shell dumpsys activity top | grep "mResumedActivity" | head -1)
if ! echo "$CURRENT" | grep -q "{package}"; then
  echo "CRASH DETECTED on Android page: {page_id}"
  # 同上处理
fi
```

---

#### Step 2.2: 多模态对比

将两端截图同时传给多模态模型，使用以下 prompt：

```
你是一个 Android→HarmonyOS 迁移 UI 对比专家。请对比以下两张截图：

左图：Android 原始应用的「{页面名称}」页面
右图：HarmonyOS 迁移后的「{页面名称}」页面

请区分两类问题后，输出 JSON：

【迁移 Bug】：代码实现错误，必须修复。常见表现：
- 元素消失（可能是 layoutWeight 在无固定高度父容器中撑高/收缩）
- 元素尺寸异常（可能是 ImageFit.Contain 在无固定高度 Stack 中按原始像素展开）
- 组件宽度撑满而非收缩（Android wrap_content → ArkTS 中需 Row 包裹）
- 内容被裁剪消失（clip(true) 与 borderRadius 组合问题）
- 颜色/字号明显错误
- 按钮样式不一致（圆角、描边、渐变、背景色）
- 组件位置偏移（元素间距、对齐方式）
- 尺寸比例失调

【平台差异】：HarmonyOS 与 Android 的设计规范差异，无需修复。常见表现：
- 状态栏、导航栏样式/高度不同
- 字体渲染方式细微差异
- 系统默认图标风格不同
- dp 与 vp 之间的细微尺寸差异（±10% 以内）

输出格式：
{
  "overall_similarity": 0.85,
  "differences": [
    {
      "category": "layout" | "color" | "font" | "spacing" | "component" | "icon" | "missing" | "layout_bug",
      "severity": "high" | "medium" | "low",
      "is_migration_bug": true | false,
      "description": "具体描述，包含在哪里、有什么不同",
      "root_cause_hint": "可能的 ArkTS 代码原因（如 layoutWeight 撑高、ImageFit.Contain 无高度约束等）",
      "suggested_fix": {
        "file": "entry/src/main/ets/...",
        "change": "具体改法",
        "property": "属性名",
        "current_value": "当前值",
        "expected_value": "目标值"
      }
    }
  ],
  "missing_elements": ["..."],
  "extra_elements": ["..."],
  "scroll_needed": true | false
}

分析维度（全部 8 项都必须检查）：
1. 布局结构：元素是否全部可见，顺序是否一致，有无内容被推出屏幕
2. 组件类型：列表/卡片/按钮/输入框等是否对应
3. 颜色：背景色、文字色、主题色是否一致
4. 字体大小：标题、正文、辅助文字的相对大小关系
5. 间距：padding、margin、元素间距
6. 图标：图标样式和位置
7. 缺失/多余元素
8. scroll_needed：HarmonyOS 页面是否需要滚动才能看完整内容（若 true，提示重新截图）
```

---

#### Step 2.3: 差异分类

将差异按可自动修复性分类：

| 类别 | 说明 | 处理方式 |
|------|------|---------|
| `auto_fixable` | `is_migration_bug=true` 且有明确 file + property + expected_value | 自动修改代码 |
| `layout_bug` | 元素消失/尺寸异常，需先读代码确认根因再修 | 读源码 → 定位 → 修复 |
| `needs_investigation` | 缺失元素，需分析代码才知道怎么加 | 记录，人工处理 |
| `design_difference` | `is_migration_bug=false`，平台规范差异 | 记录到报告，不修改 |
| `dynamic_content` | 运行时数据差异（列表内容/时间戳不同） | 忽略 |

---

#### Step 2.4: 修复

**对 `auto_fixable` 和 `layout_bug` 差异：**

1. 读取目标 `.ets` 文件，理解当前实现
2. 对 `layout_bug` 类别，优先排查以下常见根因（见 Section 8 速查表）
3. 应用修改，记录到修复日志
4. 调用 `hmos_fix_build_errors` 确保编译通过

修复规则：
- 字体大小：修改 `.fontSize(N)`
- 颜色：修改 `.fontColor()` / `.backgroundColor()`
- 间距：修改 `.padding()` / `.margin()`
- 组件尺寸：修改 `.width()` / `.height()`
- 缺失组件：根据 Android spec 补充
- 对齐方式：修改 `.alignItems()` / `.justifyContent()`
- 按钮样式：修改 `.borderRadius()` / `.border()` / `.linearGradient()`
- 组件位置：修改 `.margin()` / `.position()` / `.offset()`

---

#### Step 2.5: 重新截图验证（单页收敛判断）

```
修复后重新执行:
  Step 2.0（导航到目标页）→ Step 2.1（截图）→ Step 2.1.5（崩溃检测）→ Step 2.2（对比）

round += 1

MAX_ROUNDS = progress.json.max_rounds_per_page || 5  （可配置，默认 5）

IF round >= MAX_ROUNDS:
  status = "partial"
  停止，写入进度，进入下一页
ELIF 本轮无 high 差异（is_migration_bug=true）:
  status = "pass"
  收敛，写入进度，进入下一页
ELIF 本轮 auto_fixable+layout_bug 数量 == 上轮:
  status = "partial"
  无改善，停止（避免死循环），写入进度，进入下一页
ELSE:
  继续 Step 2.4
```

**每页结束时立即写入 `progress.json`**（无论 pass/partial/skip/blocked）：

```json
"MineSettingPage": {
  "status": "pass",
  "reachability": "public",
  "last_updated": "2026-04-13T07:00:00Z",
  "similarity": 0.91,
  "rounds": 2,
  "issues_fixed": 3,
  "issues_remaining": 0,
  "navigation_path": "Home → Mine tab → Settings icon",
  "notes": "ServiceItem layoutWeight→width, title padding"
}
```

`status` 取值：
| 值 | 含义 |
|----|------|
| `pass` | 无 high 级迁移 bug，收敛 |
| `partial` | 达到最大轮次，仍有 medium/low 问题未修 |
| `skip` | 页面为 login_walled / data_dependent，仅做了代码扫描 |
| `blocked` | 应用崩溃、截图失败、导航无法到达 |

---

### Phase 3: 清理与报告

**Step 3.1: 生成报告**

写入 `spec/visual-verify/report.md`：

```markdown
# 视觉对比验证报告

- 执行时间: YYYY-MM-DD HH:mm
- 处理页面数: N
- 收敛状态: CONVERGED / PARTIAL / NOT_CONVERGED

## Phase 1.5 批量扫描摘要

| 扫描项 | 命中数 | 修复数 | 详情 |
|--------|--------|--------|------|
| 标题栏 padding 缺失 | X | X | ... |
| 英文占位符文本 | X | X | ... |
| 可见 TODO 文本 | X | X | ... |
| 缺少 NavDestination | X | X | ... |
| aboutToAppear 参数读取 | X | X | ... |
| RouterUtils.pop() | X | X | ... |

## 页面可达性分类

| 分类 | 页面数 | 处理方式 |
|------|--------|---------|
| public | X | 完整截图对比 |
| login_walled | Y | 仅代码扫描 |
| data_dependent | Z | 仅代码扫描 |

## 截图对比总览

| 页面 ID | 页面名称 | 可达性 | 总体相似度 | high Bug | medium | low | 轮次 | 状态 |
|---------|---------|--------|-----------|---------|--------|-----|------|------|
| Index | 首页 | public | 92% | 0 | 1 | 2 | 2 | ✅ PASS |
| MineSettingPage | 设置页 | public | 85% | 0 | 2 | 1 | 3 | ✅ PASS |
| CreateCoinPage | 金币页 | login_walled | - | - | - | - | - | ⏭️ SKIP |

## 逐页详情

### {page_id}: {页面名称}

- 可达性: public
- 导航路径: Home → Mine tab → Settings icon → {page}
- Android 截图: screenshots/android/{page_id}.png
- HarmonyOS 截图: screenshots/harmony/{page_id}.jpeg

#### 差异清单（仅迁移 Bug）

| # | 类别 | 严重度 | 描述 | 根因 | 状态 |
|---|------|--------|------|------|------|
| 1 | layout_bug | high | 菜单列表文字不可见 | layoutWeight(1) 无高度约束 | ✅ 已修复 |

#### 平台差异（已忽略）

- 状态栏字体颜色略有差异（系统级）

#### 修复记录

| 轮次 | 修改文件 | 修改内容 |
|------|---------|---------|
| 1 | MineSettingPage.ets | padding top: 0 → 42 |

## 崩溃页面

| 页面 | 导航路径 | 崩溃时机 | 可能原因 |
|------|---------|---------|---------|
| RefundProgressPage | Settings → 一键退款 | 页面加载时 | RouterUtils.getParamByName in aboutToAppear |
```

---

## 5. 门控

```
视觉对比门控:
  │
  ├─ 所有 public P0 页面 overall_similarity >= 80% AND is_migration_bug high 差异 == 0 → PASS
  ├─ public P0 页面有 high 迁移 Bug 但已修复且重测通过 → PASS
  ├─ public P0 页面有 high 迁移 Bug 且未修复 → FAIL
  ├─ login_walled / data_dependent 页面不参与门控（仅报告代码扫描结果）
  └─ P1 页面不阻塞门控，仅报告
```

---

## 6. 与 a2h-verify 的集成

本 skill 由 a2h-verify CHECK-7 调用：

```
a2h-verify CHECK-7:
  │
  ├─ arkts-visual-verify 可用？
  │   ├─ 是 → 调用本 skill，将报告合并到 verify-report.md
  │   └─ 否 → CHECK-7: DEFERRED（保持现有行为）
  │
  └─ 本 skill 返回:
      ├─ PASS → CHECK-7: PASS
      ├─ PARTIAL → CHECK-7: PASS (附 warnings)
      └─ FAIL → CHECK-7: FAIL（触发回环）
```

---

## 7. 命令速查表

### HarmonyOS 模拟器命令

| 操作 | 正确命令 | ❌ 错误命令 |
|------|---------|-----------|
| 截图 | `hdc shell snapshot_display -f /data/local/tmp/x.jpeg`（必须 `.jpeg`） | `snapshot_display -f x.png`（不支持 png） |
| 点击 | `hdc shell uitest uiInput click {x} {y}` | `hdc shell uinput -T ...`（不存在）/ `input tap`（不存在） |
| 返回键 | `hdc shell uitest uiInput keyEvent Back` | `input keyevent KEYCODE_BACK`（不存在） |
| 滑动 | `hdc shell uitest uiInput swipe {x1} {y1} {x2} {y2} {speed}` | `input swipe`（不存在） |
| 布局分析 | `hdc shell uitest dumpLayout` | `uiautomator dump`（Android 命令） |
| 启动应用 | `hdc shell aa start -a EntryAbility -b {bundleName}` | 无 `-W` 等待选项 |
| 强制停止 | `hdc shell aa force-stop {bundleName}` | `am force-stop`（Android 命令） |
| hdc 路径 | `$(find /Applications/DevEco-Studio.app -name hdc \| head -1)` | 直接 `hdc`（可能不在 PATH） |
| aa start 传参 | `--ps key value`（string 参数） | `-e key value`（旧语法/Android 语法） |

### Android 模拟器命令

| 操作 | 命令 |
|------|------|
| 截图 | `adb shell screencap -p /sdcard/x.png` |
| 点击 | `adb shell input tap {x} {y}` |
| 返回键 | `adb shell input keyevent KEYCODE_BACK` |
| 布局分析 | `adb shell uiautomator dump /sdcard/ui.xml && adb pull /sdcard/ui.xml` |
| 启动 Activity | `adb shell am start -n "{package}/{activity}" -W` |
| 强制停止 | `adb shell am force-stop {package}` |

### 坐标获取规范（必须遵守）

```
⚠️ 禁止使用目测坐标。所有点击坐标必须通过以下流程获取：

1. 执行 dumpLayout / uiautomator dump
2. 解析 JSON/XML，找到目标元素的 bounds
3. bounds 格式: [left, top][right, bottom]
4. 中心点 = ((left + right) / 2, (top + bottom) / 2)
5. 使用中心点坐标执行 click

原因: 目测坐标偏差通常 50-100px，导致点击到错误元素或空白区域，
      浪费大量时间重试。dumpLayout 获取坐标是零成本操作。
```

---

## 8. ArkTS 常见隐形 Layout Bug 速查表

遇到"元素消失"、"组件过高/过矮"、"内容被截断"时，优先排查以下根因：

| 症状 | 根因 | 修复方法 |
|------|------|---------|
| 子元素内容消失，但父容器背景可见 | `layoutWeight(1)` 用在无固定高度的父 Column/Row 中，导致子元素高度为 0 或无限撑高 | 去掉 `layoutWeight(1)`，改用 `.width('100%')` 或明确 `.height()` |
| 背景图撑开整个页面，把下方内容推出屏幕 | `ImageFit.Contain` 在无固定高度的 `Stack` 中按图片原始像素展开（尤其跨密度：base/media 图片未做密度适配） | 给 Stack 加 `.height(N)`，并将图片改为 `ImageFit.Cover` |
| `wrap_content` 宽度的 chip/标签变成全宽 | ArkTS `Column` 子元素默认拉伸到父宽度；需用 `Row` 包裹才能触发收缩行为 | 把 chip 的 `Text` 包进 `Row() { Text(...) }.width('100%')` |
| `clip(true)` + `borderRadius` 导致内容消失 | `clip(true)` 在某些布局上下文中裁掉子节点内容 | 去掉 `clip(true)`，仅保留 `borderRadius` 即可实现圆角 |
| 页面内容需要滚动才能看到，但初始截图为空 | `Scroll` 容器默认从顶部开始，但内容超高时菜单项在屏幕外 | 检查是否有组件意外撑高（优先检查 `layoutWeight` 和无约束 Image） |
| 图片显示为空白/很小 | 资源路径错误，或图片资源在 `base/media` 但需要密度适配版本 | 确认 `$r('app.media.xxx')` 资源存在；大尺寸图片考虑添加 `mdpi/hdpi/xhdpi` 版本 |
| 按钮/元素被空容器遮挡不可见 | 空 Grid/List/Scroll 等容器即使无内容也会占据 layoutWeight 分配的空间，遮挡后续元素 | 在空数据时隐藏容器：`if (list.length > 0) { Grid() { ... } }` |
| 返回按钮点击无效 | 页面未包裹 NavDestination，pathStack 为默认空值 | 用 NavDestination 包裹 build 内容，在 onReady 中获取 pathStack |
| 页面加载时崩溃 | aboutToAppear 中调用 RouterUtils.getParamByName 但 pathStack 尚未初始化 | 将参数读取迁移到 NavDestination.onReady 回调中 |
| 标题栏与状态栏重叠 | 标题栏 Row 缺少 `padding({ top: 42 })` 或等效的状态栏高度避让 | 添加 `.padding({ top: 42 })` 或使用 `$r('app.float.dimen_page_marginTop')` |

---

## 9. 使用示例

```
用户: 截图对比一下
用户: 视觉验证
用户: 检查 UI 一致性
用户: 对比一下迁移前后的效果
用户: 跑一下视觉对比
用户: 你觉得这个页面和安卓差多少
```

---

## 10. 局限性

| 局限 | 说明 |
|------|------|
| 登录墙 | 需要登录的页面（login_walled）仅做代码扫描，无法截图对比。需登录后手动验证或提供测试账号 |
| 数据依赖 | 需要前序页面传参的页面（data_dependent）无法直接导航到达，仅做代码扫描 |
| 静态页面为主 | 截图的是页面默认状态，无法覆盖交互中状态（如播放中、展开菜单） |
| 需要模拟器 | 两端模拟器必须已运行且应用已安装 |
| 多模态依赖 | 需要多模态模型能力，纯文本模型无法执行 |
| 动态内容差异 | 列表数据、时间戳等运行时差异会被忽略 |
| 平台设计差异 | 状态栏、导航栏等系统 UI 差异标记为 design_difference 不修复 |
| 导航链路依赖 | 采用导航链路模式，深层嵌套页面可能导航路径较长，耗时增加 |
