---
name: a2h-spec
description: Android→ArkTS 迁移第一步：三阶段 Spec 生成（数据准备 + UI 清单 + 功能 Spec）。支持三源数据（view.xml + meta.json + 源码 layout XML）、confidence 三级评级、双模式数据准备。即使用户只说"分析这个项目"或"开始迁移"，也应触发。V1 后说"功能缺失"或"有 bug"时，内部委托给 spec-evolver。
---

# a2h-spec

## 1. 定位

Pipeline 层第一步，**用户唯一的 Spec 入口**。

本 skill 直接执行三阶段分析（Phase A 调用 android-ui-graph-builder 的 Python 脚本做确定性提取，Phase B/C 直接生成 Spec）。用户只需要说"分析项目"或"开始迁移"，本 skill 自动判断当前阶段（初始/增量），执行对应流程。

```
用户
  │
  ▼
a2h-spec（Pipeline 层 — 路由 + 分析 + 生成）
  │
  ├─ 初始迁移 → 三阶段直接执行:
  │   ├─ Phase A: 三源数据准备（双模式：批量前置 + 按需触发）
  │   ├─ Phase B: UI 清单生成（ui-manifest + 分页 spec + 页面状态生命周期）
  │   └─ Phase C: 功能 Spec 生成（总分结构：index + base + 按功能分文件）
  │
  └─ 增量演进 → spec-evolver（Domain 层）
```

**核心原则**：a2h-spec 直接执行所有分析和生成工作。UI 数据来自三源（view.xml + meta.json + 源码 layout XML），Feature 数据来自源码静态分析。

---

## 2. 智能路由

启动时自动检查 `spec/baseline/` 目录是否存在：

```
spec/baseline/ 存在？
  │
  ├─ 不存在 → 初始迁移流程（Section 3）
  │   直接执行 Phase A → Phase B → Phase C
  │
  └─ 已存在 → 增量演进流程（Section 4）
      委托: spec-evolver
```

判断细节：
- `spec/baseline/ui-manifest.md` + `spec/baseline/feature-index.md` 两个文件都存在 → baseline 已完成
- 只有部分文件存在 → 提示用户 baseline 不完整，建议重新生成
- 完全不存在 → 初始迁移

---

## 3. 初始迁移流程

当 `spec/baseline/` 不存在时执行此流程。共三个阶段，顺序执行。

### 3.0 前置：确认源码路径

- 询问用户 Android 项目的源码路径（如果未提供）
- 验证路径有效性：检查 `AndroidManifest.xml` 或 `build.gradle` 是否存在
- 记录源码根路径 `$ANDROID_SRC`，后续所有相对路径以此为基准
- 检查 `spec/ref/` 是否已有参考文档（`*_spec.md` 和 `*_design.md`）
  - 如果有 → 记录 `$REF_SPEC` 和 `$REF_DESIGN` 路径，Phase B/C 分析时参考并执行交叉验证
  - 如果没有 → 询问用户选择：
    - **选项 A【推荐】**: 自动生成 — 调度 `a2h-android-analyzer` agent 从 Android 源码分析生成参考文档
    - **选项 B**: 手动放置 — 用户自行将参考文档放入 `spec/ref/` 后继续
    - **选项 C**: 跳过 — 不生成参考文档（不影响核心流程，仅缺少 Phase B/C 交叉验证）
  - 如果用户选择 A → 调度 agent 生成参考文档：
    ```
    Spawn agent `a2h-android-analyzer`,
      prompt: "分析 Android 项目并生成参考文档。
        android_source_dir: $ANDROID_SRC
        output_dir: spec/ref/
        project_name: {从 AndroidManifest 提取的 package 短名}"
    )
    ```
    等待完成后，记录 `$REF_SPEC` 和 `$REF_DESIGN` 路径，继续 Phase A

### 3.0b 风格配置

- 扫描 skills 目录中所有 SKILL.md 的 frontmatter，筛选 `type: style` 的条目
- 提取去重后的 `style-set` 值列表
- 根据发现结果决定交互方式：
  - 无风格 skills → 自动设为 `style_set = none`，不询问
  - 有 1 个风格集 → 询问用户："检测到 **{style-set-name}** 风格，是否使用？(Y/n)"
    - Y → `style_set = {style-set-name}`
    - n → `style_set = none`
  - 有多个风格集 → 列表供用户选择，默认 `none`
- 记录 `$STYLE_SET` 变量，后续 Phase A/B/C 输出中携带此字段

### Phase A: 数据准备【双模式】

Phase A 负责为每个 Android 页面准备三源数据（view.xml + meta.json + 源码 layout XML），并标记 confidence 评级。

#### 批量模式（a2h-spec 阶段触发）

这是初始迁移时的标准执行模式。

**Step A1: 提取页面清单**

1. 读取 `$ANDROID_SRC/app/src/main/AndroidManifest.xml`
2. 提取所有 `<activity>` 声明，记录：
   - Activity 全限定类名
   - `android:label`
   - `intent-filter`（判断是否为 launcher Activity）
   - `android:theme`
3. 定位每个 Activity 的 Java/Kotlin 源码文件

**Step A2: 逐页分析**

**Step A2a: 确定性骨架生成（脚本）**

对每个 Activity/Fragment，先运行确定性脚本生成 meta.json 骨架：

```bash
python3 .agents/skills/android-ui-graph-builder/scripts/synthesize_meta_json.py \
  $ANDROID_SRC \
  --activity {fully_qualified_class_name} \
  --page-id {page_id} \
  --output spec/baseline/ui-snapshots/{page_dir}/meta.json \
  --mode scaffold \
  --package {package}
```

脚本自动提取：`layout_sources`、`menu_sources`、`fragment_tags`、`style_sources`、`recycler_item_layouts`、`navigation_targets`。
LLM 需补充的字段以默认占位值标记（`label=""`、`confidence="medium"`、`dynamic_menus={}`、`navigation_mode="UNKNOWN"` 等）。

**Step A2b: LLM 语义分析（在脚本骨架基础上补充）**

读取脚本生成的 meta.json 骨架，验证确定性字段是否正确，并补充以下语义字段：

对每个 Activity/Fragment 执行以下分析：

```
Activity 源码
  │
  ├─ setContentView(R.layout.xxx) → 定位 layout XML 路径
  │
  ├─ Fragment 加载关系:
  │   ├─ FragmentTransaction.replace/add → 定位子 Fragment
  │   ├─ ViewPager + FragmentPagerAdapter → 定位分页 Fragment
  │   └─ Navigation Component → nav_graph.xml → 定位 NavHostFragment
  │
  └─ 导航关系:
      ├─ Intent(this, XxxActivity::class) → 页面跳转
      ├─ NavController.navigate(R.id.xxx) → Navigation 跳转
      ├─ startActivity / startActivityForResult → 系统/外部跳转
      └─ Fragment 回退栈操作
```

**扩展分析项（增强 UI 还原精度）**：

对每个 Activity/Fragment 额外执行以下分析：

```
├─ 动态菜单分析:
│   ├─ BottomNavigationView.getMenu().add() → 运行时动态添加的菜单项
│   ├─ menu.clear() + 循环 add → 可配置菜单（记录 max items、overflow 逻辑）
│   ├─ setOnItemSelectedListener → 菜单点击事件处理
│   ├─ ListPopupWindow / PopupMenu → overflow "More" 弹窗（记录宽度、Gravity、内容项）
│   └─ onCreateOptionsMenu() → inflates res/menu/*.xml（记录到 menu_sources）
│
├─ BottomSheet 行为分析:
│   ├─ BottomSheetBehavior 子类 → 自定义行为类名（如 LockableBottomSheetBehavior）
│   ├─ setPeekHeight() / @dimen/ 引用 → peek 高度
│   ├─ setState() 调用点 → 状态切换逻辑（COLLAPSED/EXPANDED/HIDDEN）
│   ├─ setHideable() → 是否可隐藏
│   └─ addBottomSheetCallback() → 滑动回调（记录 onSlide 行为）
│
├─ RecyclerView Adapter item layout 追踪:
│   ├─ Adapter.onCreateViewHolder() → inflate(R.layout.xxx) → 记录 item layout 名
│   ├─ getItemViewType() → 多类型 item layout 映射
│   └─ 记录到 meta.json.recycler_item_layouts
│
├─ Fragment TAG 常量提取:
│   ├─ 扫描 public static final String TAG = "xxx"
│   ├─ 记录 Fragment 类名 → TAG 常量值的映射
│   └─ 后续所有导航引用必须使用 TAG 而非类名（如 InboxFragment.TAG = "NewEpisodesFragment"）
│
└─ 导航模式分析:
    ├─ DrawerLayout.setDrawerLockMode() → drawer 是否被锁定及条件
    ├─ BottomNavigationView.setVisibility(GONE/VISIBLE) → 底部导航显隐条件
    └─ 互斥判断：底部导航启用时 drawer 锁定，drawer 启用时底部导航隐藏
```

对每个页面记录：
- Activity/Fragment 类名
- layout XML 文件路径列表（`layout_sources`）
- 样式/主题文件路径列表（`style_sources`）：从 layout XML 的 `style="@style/xxx"` 和 Activity 的 `android:theme` 溯源
- Fragment 加载关系
- 导航关系（跳转目标 + 触发方式）
- 可交互元素（按钮、列表项、输入框等）
- menu 相关文件路径列表（`menu_sources`）：从 onCreateOptionsMenu 和 layout XML 的 app:menu 属性溯源
- Fragment TAG 常量映射（`fragment_tags`）：{类名: TAG值}
- 动态菜单配置（`dynamic_menus`）：底部导航的 buildMenu 逻辑、max items、overflow 弹窗类型
- BottomSheet 配置（`bottom_sheet_config`）：行为类、peek 高度、状态列表、是否可锁定
- RecyclerView item layouts（`recycler_item_layouts`）：adapter 类名 → item layout 列表映射
- 导航模式（`navigation_mode`）：底部导航和 drawer 的互斥/共存关系

**Step A3: 检查 ui-snapshots 数据**

对每个页面检查 `spec/baseline/ui-snapshots/page_NNNN_XxxActivity/` 目录：

| 检查项 | 存在 | 缺失时处理 | confidence |
|--------|------|-----------|-----------|
| `view.xml`（UIAutomator dump） | 标记 high | 从 layout XML 合成简化版 view.xml | medium |
| `meta.json` | 读取并扩展 | 从源码分析自动生成 | 按 view.xml 情况 |
| `screenshot.png` | 记录存在 | 不影响 confidence | — |
| 部分 layout XML 缺失 | — | 标记该页面 | low |

**合成 view.xml（当无 UIAutomator dump 时）**：

使用确定性脚本从 layout XML 生成近似的 UIAutomator 格式 view.xml：

1. 确认 meta.json 中 `layout_sources` 已填充（来自 Step A2 分析结果）
2. 调用合成脚本：
   ```bash
   python3 .agents/skills/android-ui-graph-builder/scripts/synthesize_view_xml.py \
     $ANDROID_SRC \
     --layouts "{meta.json.layout_sources 逗号拼接}" \
     --menus "{meta.json.menu_sources 逗号拼接}" \
     --resolve-strings \
     --resolve-styles \
     --output spec/baseline/ui-snapshots/page_NNNN_XxxActivity/view.xml \
     --package {AndroidManifest 中的 package 属性}
   ```
3. 脚本输出结果处理：
   - 成功 → 在 meta.json 中标记 `"view_xml_synthesized": true`，confidence 维持 `medium`
   - 失败 → confidence 降为 `low`，meta.json 标记 `"view_xml_synthesized": false`，记录失败原因，不阻塞后续 Phase
4. view.xml 合成后，运行 enrich 模式补充 `clickable_elements`（从 view.xml 提取）：
   ```bash
   python3 .agents/skills/android-ui-graph-builder/scripts/synthesize_meta_json.py \
     $ANDROID_SRC \
     --activity {fully_qualified_class_name} \
     --page-id {page_id} \
     --output spec/baseline/ui-snapshots/{page_dir}/meta.json \
     --mode enrich \
     --existing spec/baseline/ui-snapshots/{page_dir}/meta.json \
     --view-xml spec/baseline/ui-snapshots/{page_dir}/view.xml \
     --package {package}
   ```

合成版 view.xml 特征：
- 根元素 `<hierarchy synthesized="true">` 标识为合成版
- `bounds` 属性始终为空（无运行时坐标数据）
- `class` 为全限定类名，`resource-id` 为 `{package}:id/{name}` 格式
- `clickable`/`enabled`/`scrollable` 等从 XML 属性取值，无则用 Android 默认值
- 递归处理 `<include>` 和 `<merge>` 标签

扩展/生成 meta.json 字段：

```json
{
  "page_id": "page_0001_MainActivity",
  "label": "从 android:label 或源码注释推断的页面描述",
  "activity": "com.example.app.MainActivity",
  "auto_generated": true,
  "confidence": "high | medium | low",
  "layout_sources": [
    "app/src/main/res/layout/activity_main.xml",
    "app/src/main/res/layout/fragment_home.xml"
  ],
  "style_sources": [
    "app/src/main/res/values/styles.xml",
    "app/src/main/res/values/themes.xml",
    "app/src/main/res/values/colors.xml"
  ],
  "click_path": [],
  "came_from": null,
  "trigger_element": null,
  "clickable_elements": [
    {
      "class": "android.widget.Button",
      "resource_id": "com.example:id/btn_submit",
      "text": "Submit",
      "content_desc": "Submit button",
      "bounds": "[100,200][300,250]",
      "children_items": []
    }
  ],
  "navigation_targets": {
    "btn_settings": "SettingsActivity",
    "btn_profile": "ProfileFragment"
  },
  "menu_sources": ["app/src/main/res/menu/home.xml"],
  "fragment_tags": {"InboxFragment": "NewEpisodesFragment", "AllEpisodesFragment": "EpisodesFragment"},
  "dynamic_menus": {
    "bottom_nav": {
      "build_method": "BottomNavigation.buildMenu()",
      "max_visible_items": 4,
      "has_more_overflow": true,
      "more_popup_type": "ListPopupWindow",
      "configurable": true
    }
  },
  "bottom_sheet_config": {
    "behavior_class": "LockableBottomSheetBehavior",
    "peek_height_dimen": "external_player_height",
    "states": ["COLLAPSED", "EXPANDED", "HIDDEN"],
    "lockable": true
  },
  "recycler_item_layouts": [
    {"adapter": "NavListAdapter", "layouts": ["nav_listitem", "nav_section_item"]}
  ],
  "navigation_mode": "MUTUALLY_EXCLUSIVE"
}
```

**confidence 三级评级与 Agent 行为策略**：

| 级别 | 数据来源 | Agent 行为 |
|------|---------|-----------|
| `high` | 有真机 UIAutomator dump（view.xml） + 截图 | 完全信任，精确还原所有细节 |
| `medium` | 从源码 layout XML 静态合成 view.xml | 结构信任，动态内容（列表高度、运行时 visibility 等）保守处理 |
| `low` | 部分 layout 缺失或高度动态页面 | 标注 TODO，不强行猜测，等待人工补充 |

**源码映射可靠性规则**：

`layout_sources` 填充规则：
- **必须**包含主 layout（来自 `setContentView` / `inflate`）
- **必须**包含所有 `<include>` 传递引用的 layout
- 路径**必须**相对于 `$ANDROID_SRC`（如 `app/src/main/res/layout/activity_main.xml`）
- 生成后逐路径验证：确认 `$ANDROID_SRC/{path}` 实际存在
- 不存在的路径 → 从列表移除并输出警告

`style_sources` 填充规则：
- 始终包含「标准三件套」（如果存在）：`values/styles.xml`, `values/themes.xml`, `values/colors.xml`
- 包含 layout XML 中 `style="@style/xxx"` 引用的具体文件
- 包含 Activity 在 AndroidManifest 中声明的 `android:theme` 对应文件
- 包含 `values-night/` 等变体目录下的对应文件（如果存在）

验证步骤（meta.json 写入前必须执行）：
1. 逐路径检查 `$ANDROID_SRC/{path}` 是否存在
2. 路径不存在 → 从列表移除 + 输出警告（不降级 confidence）
3. 所有路径验证完毕后写入 meta.json

**Step A4: 输出准备报告**

输出格式：
```
## Phase A: 数据准备完成

### 页面清单（共 N 个页面）
| 序号 | Activity/Fragment | confidence | view.xml | meta.json | screenshot |
|------|------------------|-----------|----------|-----------|------------|
| 0001 | MainActivity     | high      | ✓ dump      | ✓ 已扩展  | ✓          |
| 0002 | HomeFragment     | medium    | ✓ 合成(脚本) | ✗→生成    | ✗          |
| 0003 | LoginActivity    | low       | ✗ 合成失败   | ✗→生成    | ✗          |

### 数据质量摘要
- high: X 页面（有 UIAutomator dump）
- medium: Y 页面（从源码合成）
- low: Z 页面（部分 layout 缺失）

### 建议
- Z 个 low confidence 页面建议在真机上运行 UIAutomator dump 提高数据质量
- 是否继续进入 Phase B？
```

#### 按需模式（a2h-execute Stage 3 切片执行时触发）

当 a2h-execute 的 Stage 3（Feature Slices）执行到某个切片时，如果发现目标页面的 ui-snapshots 数据缺失：

1. 自动对该单个页面执行上述 Step A2 + Step A3
2. 增量更新 `spec/baseline/ui-manifest.md`（新增页面条目 + confidence 标记）
3. 增量生成对应的 `spec/baseline/ui/page_NNNN.md`
4. 继续切片执行，无需中断整个 Pipeline

按需模式必须完成以下全部产出后才返回：
- [ ] `meta.json` — 含 `layout_sources`, `style_sources`（已验证路径存在）
- [ ] `view.xml` — 合成版（调用 `synthesize_view_xml.py`）
- [ ] `ui-manifest.md` 增量更新 — 新页面条目 + confidence 标记 + status: `pending`
- [ ] `ui/page_NNNN.md` 增量生成 — 分页 spec
- [ ] `menu_sources` — 从 onCreateOptionsMenu 和 app:menu 属性提取
- [ ] `fragment_tags` — 从源码 TAG 常量提取
- [ ] `dynamic_menus` — 动态菜单构建逻辑分析
- [ ] `bottom_sheet_config` — BottomSheet 行为配置
- [ ] `recycler_item_layouts` — Adapter item layout 追踪

按需模式的触发条件：
- `a2h-execute` Stage 3 Step 3a（UI 补充）检查到目标页面 status 不是 `converted`
- 且 `ui-snapshots/page_NNNN/` 目录不存在或数据不完整

---

### Phase B: UI 清单

Phase B 基于 Phase A 的页面清单和三源数据，生成结构化的 UI Spec 文档。

**Step B1: 生成 ui-manifest.md**

在 `spec/baseline/ui-manifest.md` 生成 UI 总览文档（控制在 200 行以内）：

```markdown
# UI Manifest

## 全局约定
- 导航架构: Navigation + NavPathStack（单 Navigation 容器 + NavDestination 子页面）
- 设计令牌: 主色 $r('app.color.accent_light')，文字色 $r('app.color.text_primary')
- 命名规范: 页面 XxxPage.ets，组件 XxxComponent.ets
- 图标方案: SVG 资源 $r('app.media.ic_xxx')

## 页面清单
| 序号 | Android | ArkTS 产出 | 优先级 | confidence | 状态 |
|------|---------|-----------|--------|-----------|------|
| 0001 | MainActivity | MainPage.ets | P0 | high | pending |
| 0002 | HomeFragment | HomePage.ets | P0 | high | pending |
| 0003 | QueueFragment | QueuePage.ets | P0 | medium | pending |
| ... |

### 页面状态生命周期
pending → converted → verified
- pending: 待转换
- converted: UI 已转换，等待验证
- verified: 编译通过 + 切片级功能验证通过
- skipped: 本轮不转换（V2 范围外）

## 转换批次
- Batch 1 (P0): 0001-0005 (App Shell + Home + 核心列表页)
- Batch 2 (P0): 0006-0010 (播放器 + 订阅 + 搜索)
- Batch 3 (P1): 0011-0016 (下载 + 统计 + 设置)
- Batch 4 (P2): 0017-0023 (次要页面)

## 共享组件
| 组件 | 用于页面 | Android 来源 |
|------|---------|-------------|
| ExternalPlayerBar | MainPage | external_player_fragment.xml |
| NavDrawer | MainPage | nav_list.xml |
| EpisodeListItem | Queue, Inbox, AllEpisodes | ... |
```

全局约定的推导逻辑：
- **导航架构**：从 AndroidManifest.xml 的 Activity 数量 + Navigation Component 使用情况推断。单 Activity + NavHost → NavPathStack，多 Activity → 评估是否合并
- **设计令牌**：从 `styles.xml` / `themes.xml` / `colors.xml` 提取主色、文字色、背景色
- **命名规范**：Activity → Page，Fragment → Page 或 Component（依据是否独立导航）
- **图标方案**：扫描 `res/drawable*` 目录，确定图标格式（SVG/PNG/VectorDrawable）

优先级分配规则：
- P0：Launcher Activity + 其直接 Fragment + 核心业务页面
- P1：次级功能页面（设置、搜索、下载管理等）
- P2：辅助页面（关于、许可证、同步设置等）

**Step B2: 生成分页 UI Spec**

对每个页面生成 `spec/baseline/ui/page_NNNN_XxxActivity.md`（每文件控制在 100 行以内）：

```markdown
# page_0001: MainActivity

## 溯源
- Android Activity: de.danoeh.antennapod.activity.MainActivity
- 源码布局: app/src/main/res/layout/main.xml
- UI 快照: ui-snapshots/page_0001_MainActivity/
- 输出文件: entry/src/main/ets/pages/MainPage.ets

## 页面结构
- 根布局: DrawerLayout → SideBarContainer
- 内容区: CoordinatorLayout → Stack
- 底部导航: BottomNavigationView → Tabs (4 tabs + More popup)
- 外部播放器: ExternalPlayerFragment → ExternalPlayerBar

## 转换决策
| Android 组件 | ArkUI 组件 | 决策理由 |
|-------------|-----------|---------|
| DrawerLayout | SideBarContainer(Overlay) | 官方侧边栏容器 |
| BottomNavigationView | Tabs(BarPosition.End) | 底部 Tab 标准实现 |
| CoordinatorLayout | Stack(Alignment.Bottom) | 叠加布局 + 底部对齐 |

## 状态接口（供 Feature Pipeline 对接）
| @State 变量 | 类型 | 数据来源 | 关联功能 |
|------------|------|---------|---------|
| isPlaying | boolean | PlaybackService | F001-playback |
| episodeTitle | string | PlaybackService.currentItem | F001-playback |
| currentTabIndex | number | 本地 UI 状态 | — |
| sideBarShow | boolean | 本地 UI 状态 | — |

## 导航关系
| 触发 | 目标页面 | 类型 |
|------|---------|------|
| Tab: Home | page_0002_HomeFragment | Tab 切换 |
| Tab: Queue | page_0003_QueueFragment | Tab 切换 |
| Tab: More | BottomNavigationMorePopup | 弹出菜单 |
| ExternalPlayerBar 点击 | AudioPlayerPage | 页面跳转 |
| 侧边栏: Settings | PreferencePage | 页面跳转 |
```

分页 Spec 的生成逻辑：
- **溯源**：从 Phase A 的分析结果直接提取
- **页面结构**：读取 view.xml（或合成版）的层级树，提取主要 ViewGroup 结构，对应到 ArkUI 组件
- **转换决策**：对每个关键 Android 组件，记录选择的 ArkUI 替代方案和理由
- **状态接口**：扫描源码中的成员变量、LiveData/Flow 订阅、SharedPreferences 读取，预定义 @State 变量
- **导航关系**：从 Phase A Step A2 的导航分析结果提取

**Step B2.5: 参考文档交叉验证（条件执行）**

仅当 `$REF_SPEC` 存在时执行此步骤。如果用户在 3.0 前置步骤中选择了"跳过"，则跳过本步。

1. 读取 `$REF_SPEC` 的以下章节：
   - §5 核心能力 → 提取所有交互流程中涉及的页面名和导航路径
   - §7 用户界面行为规格 → 提取所有屏幕、视图模式、手势、对话框
   - §11 平台行为规格 → 提取通知、Widget、Tile 等系统集成页面

2. 读取 `$REF_DESIGN` 的以下章节（如果存在）：
   - §7 屏幕清单与导航 → 提取完整页面清单和导航图
   - §8 用户交互规格 → 提取手势和对话框目录

3. 交叉比对 `ui-manifest.md` + 分页 spec：

   | 比对维度 | ref 来源 | 比对目标 | 处理策略 |
   |---------|---------|---------|---------|
   | 页面覆盖 | spec §7.1 + design §7.1 | ui-manifest.md 页面清单 | P0 级缺失自动补充，P1/P2 仅报告 |
   | 导航路径 | spec §7.1 + design §7.2 | 分页 spec 导航关系表 | 补充到对应分页 spec |
   | 对话框 | spec §7.4 | 分页 spec 状态接口 | 仅报告缺失 |
   | 系统集成页面 | spec §11.3 (Widget/Tile) | ui-manifest.md | 仅报告缺失 |

4. 输出 UI 覆盖率报告（附加到 Step B3 审批摘要中）：
   ```
   ### 参考文档交叉验证结果
   - ref 页面/屏幕总数: N 个
   - 已覆盖: M 个
   - 未覆盖: K 个（列出名称 + 建议优先级）
   - ref 导航路径总数: X 条
   - 已覆盖: Y 条
   - 缺失: Z 条（列出）
   - ref 对话框总数: A 个
   - 已覆盖: B 个
   - 缺失: C 个（列出）
   ```

5. 自动补充规则：
   - P0 级缺失页面 → 自动添加到 ui-manifest.md 页面清单 + 生成分页 spec
   - P1/P2 级缺失 → 仅在报告中列出，由用户在审批时决定是否补充
   - 已自动补充的页面在报告中标注 `[已自动补充]`

**Step B3: 人工审批 Gate**

输出摘要等待审批：

```
## Phase B: UI 清单生成完成

- 页面总数: N 个（P0 × a, P1 × b, P2 × c）
- 分批计划: M 个批次
- confidence 分布: high × X, medium × Y, low × Z
- 全局约定: 导航架构 = NavPathStack, 主色 = ...
- 共享组件: K 个

请审阅 spec/baseline/ui-manifest.md 和 spec/baseline/ui/ 目录。
确认后进入 Phase C（功能 Spec 生成）。
```

<HARD-GATE>
Phase B 审批通过后才能进入 Phase C。
用户必须明确说"确认"、"通过"、"继续"等肯定性语句。
如果用户有修改意见，先修改 ui-manifest.md / 分页 spec，重新请求审批。
</HARD-GATE>

---

### Phase C: 功能 Spec

Phase C 分析 Android 源码的非 UI 部分，生成功能层 Spec。

**Step C1: 源码分析**

扫描 Android 源码的以下层次：

| 分析目标 | 扫描策略 | 产出 |
|---------|---------|------|
| 数据模型 (Entity/POJO) | 扫描 `@Entity`, `data class`, POJO 模式 | 实体清单 + 字段定义 + 关系 |
| 数据库 (Room/SQLite) | 扫描 `@Dao`, `@Database`, `SQLiteOpenHelper`, ContentProvider | 表结构 + 查询方法 + 迁移 |
| 服务层 (Service) | 扫描 `Service`, `IntentService`, `JobService` | 服务清单 + 生命周期 + 接口 |
| 网络 (Retrofit/OkHttp) | 扫描 `@GET/@POST`, `OkHttpClient`, `HttpURLConnection` | API 端点 + 请求/响应模型 |
| 事件 (EventBus/LiveData/Flow) | 扫描 `@Subscribe`, `LiveData`, `StateFlow`, `SharedFlow` | 事件清单 + 发布者/订阅者 |
| 偏好设置 (SharedPreferences) | 扫描 `getSharedPreferences`, `PreferenceManager` | 偏好键值清单 + 类型 |
| 权限 | AndroidManifest.xml `<uses-permission>` | 权限清单 + 使用场景 |
| 第三方库 | `build.gradle` dependencies | 依赖清单 + HarmonyOS 替代方案 |

**Step C2: 生成 feature-index.md**

在 `spec/baseline/feature-index.md` 生成功能总览文档（控制在 200 行以内）：

```markdown
# Feature Index

## 领域模型概览
核心实体: Feed, FeedItem, FeedMedia, Queue, DownloadTask, PlaybackState
关系: Feed 1:N FeedItem 1:1 FeedMedia, Queue 1:N FeedItem

## 功能清单
| ID | 功能 | 优先级 | 依赖 | 涉及页面 | 状态 |
|----|------|--------|------|---------|------|
| F001 | 音频播放 | P0 | base | AudioPlayerPage, MainPage(MiniBar) | pending |
| F002 | 订阅管理 | P0 | base | SubscriptionPage, FeedDetailPage | pending |
| F003 | 下载管理 | P1 | F001 | DownloadsPage | pending |
| ... |

## 依赖图
base → F001(播放) → F003(下载)
base → F002(订阅) → F005(搜索)
base → F004(队列) → F001(播放)
F001 + F002 → F007(统计)

## 执行顺序（拓扑排序）
1. feature-base (水平)
2. F001, F002 (可并行)
3. F004 (依赖 F001)
4. F003, F005 (可并行)
5. F006, F007 (可并行)
```

功能拆分原则：
- 一个功能 = 一个用户可感知的完整能力（如"播放"、"订阅"、"下载"）
- 功能之间通过明确接口（Service 方法、Event）解耦
- 每个功能关联到它涉及的页面（来自 Phase B 的页面清单）
- 优先级与页面优先级对齐：P0 页面的核心功能 = P0 功能

**Step C3: 生成 feature-base.md**

在 `spec/baseline/feature-base.md` 生成共享基础设施 Spec：

```markdown
# Feature Base: 共享基础设施

## 数据模型
所有实体定义 (Feed, FeedItem, FeedMedia, ...)
- 字段清单、类型、默认值
- 实体间关系（1:1, 1:N, M:N）

## 数据库
- 建表 SQL / RDB schema
- 索引定义
- 初始数据 / 迁移策略
- DAO 接口定义

## 网络层
- HttpClient 封装（基于 @ohos.net.http 或三方库）
- API endpoint 定义
- 请求拦截器 / 认证
- 错误处理策略

## 事件系统
- EventHub 事件名常量
- 发布/订阅模式封装
- 典型事件流

## 偏好设置
- SharedPreferences → @ohos.data.preferences 键值映射
- 类型定义
- 默认值

## 权限声明
- module.json5 权限配置
- 运行时权限请求逻辑

## 公共组件库
- Toolbar / ActionBar 通用组件
- TabBar 通用组件
- Card / ListItem 通用组件
- 作为 Agent UI 还原的样式锚点，确保跨页面风格一致
```

**Step C4: 生成按功能拆分的 Spec**

对每个功能生成 `spec/baseline/features/F00x-xxx.md`（每文件控制在 300 行以内）：

```markdown
# F001: 音频播放

## 范围
涉及页面: AudioPlayerPage, MainPage(ExternalPlayerBar)
依赖: feature-base (Models, DB)

## 数据流
PlaybackService → @State in AudioPlayerPage / ExternalPlayerBar
  ├─ 播放状态 (playing/paused/stopped)
  ├─ 进度 (position/duration)
  └─ 当前曲目 (title/author/cover)

## 服务层
PlaybackService (singleton):
  - play(feedItemId: number): void
  - pause(): void
  - seekTo(ms: number): void
  - getCurrentItem(): FeedItem | undefined
  - onStateChange: callback

## 状态管理
AppStorage keys: currentPlaybackState, currentEpisodeId

## 对接点（与 UI 页面的接口）
AudioPlayerPage:
  - @State isPlaying ← PlaybackService.isPlaying
  - @State playPosition ← PlaybackService.currentPosition
  - onPlayPause() → PlaybackService.togglePlayPause()

ExternalPlayerBar:
  - @State episodeTitle ← PlaybackService.currentItem.title
  - @State isPlaying ← PlaybackService.isPlaying
  - onBarClicked() → NavPathStack.push('AudioPlayerPage')

## 验收标准
- [ ] 点击播放按钮开始/暂停播放
- [ ] 进度条实时更新
- [ ] ExternalPlayerBar 显示当前曲目信息
- [ ] 后台播放不中断
```

每个功能 Spec 必须包含：
- **范围**：涉及的页面和依赖
- **数据流**：从数据源到 UI 的完整链路
- **服务层**：Service / Repository 的接口定义
- **状态管理**：AppStorage / @State 键名和类型
- **对接点**：与 UI 页面的 @State 变量对应关系（引用 Phase B 分页 Spec 的状态接口）
- **验收标准**：可验证的功能检查项

**Step C4.5: 参考文档交叉验证（条件执行）**

仅当 `$REF_SPEC` 或 `$REF_DESIGN` 存在时执行。如果用户在 3.0 前置步骤中选择了"跳过"，则跳过本步。

1. 读取 `$REF_SPEC` 的以下章节：
   - §2 领域术语 → 提取所有术语，对比 feature-base.md 数据模型命名
   - §5 核心能力 → 提取所有业务规则和功能域，对比 features/ 目录的功能覆盖
   - §6 数据约束 → 提取所有实体和字段约束，对比 feature-base.md 数据模型
   - §8 偏好设置行为规格 → 提取所有偏好键和行为影响，对比 feature-base.md 偏好设置章节
   - §9 文件格式与数据交换 → 提取所有数据交换规格，对比 features/ 导入导出功能
   - §11 平台行为规格 → 提取通知、Widget、Tile 等，对比是否有对应 feature

2. 读取 `$REF_DESIGN` 的以下章节（如果存在）：
   - §3.5 Storage/Database → 对比 feature-base.md 数据库表定义
   - §4 接口设计 → 对比 features/ 服务层接口方法
   - §5 数据模型 → 对比 feature-base.md 实体定义（字段级别）
   - §10 偏好设置目录 → 对比 feature-base.md 偏好键清单

3. 五维度交叉比对：

   | 维度 | ref 来源 | 比对目标 | 自动修复 |
   |------|---------|---------|---------|
   | 功能覆盖 | spec §5 各能力 | feature-index 功能清单 | **仅报告**（不自动创建 feature 文件） |
   | 数据模型 | spec §6 + design §5 | feature-base 实体定义 | **自动追加**缺失实体/字段到 feature-base.md |
   | 偏好设置 | spec §8 + design §10 | feature-base 偏好章节 | **自动追加**缺失 key 到 feature-base.md |
   | 服务接口 | design §4 | features/ 服务层定义 | **仅报告** |
   | 业务规则 | spec §5 各规则 | features/ 验收标准 | **自动追加**缺失验收标准到对应 feature 文件 |

4. 输出功能覆盖率报告（附加到 Step C5 审批摘要中）：
   ```
   ### 参考文档交叉验证结果

   #### 功能覆盖
   - ref 核心能力: N 个
   - 已覆盖: M 个（列出 feature ID ↔ ref 能力对应关系）
   - 未覆盖: K 个（列出能力名 + 建议新增的 feature ID）

   #### 数据模型覆盖
   - ref 实体: X 个
   - 已覆盖: Y 个
   - 缺失实体: (列出) [已自动追加]
   - 缺失字段: (列出 实体.字段) [已自动追加]

   #### 偏好设置覆盖
   - ref 偏好键: A 个
   - 已覆盖: B 个
   - 缺失键: C 个 (列出) [已自动追加]

   #### 服务接口覆盖
   - ref 接口方法: P 个
   - 已覆盖: Q 个
   - 缺失: R 个 (列出)

   #### 业务规则覆盖
   - ref 业务规则: S 条
   - 已覆盖（有对应验收标准）: T 条
   - 缺失: U 条 (列出) [已自动追加验收标准]
   ```

5. 自动追加规则：
   - 仅追加到**已存在**的文件，不创建新 feature spec 文件
   - 追加的内容在目标文件中标注 `<!-- 由交叉验证自动追加 -->`
   - 缺失的功能（完整 feature 级别缺失）仅在报告中列出，由用户在审批时决定是否补充

**Step C5: 人工审批 Gate**

输出摘要等待审批：

```
## Phase C: 功能 Spec 生成完成

- 功能总数: N 个（P0 × a, P1 × b, P2 × c）
- 领域模型: X 个实体, Y 个关系
- 依赖图深度: Z 层
- 执行顺序: M 个并行组
- 基础设施: 数据库 X 表, 网络 Y 端点, 事件 Z 个

请审阅 spec/baseline/feature-index.md 和 spec/baseline/features/ 目录。
确认后调用 a2h-plan 生成执行计划。
```

<HARD-GATE>
Phase C 审批通过后才能进入 a2h-plan。
用户必须明确确认。如果用户有修改意见，先修改相关 spec 文件，重新请求审批。
</HARD-GATE>

---

## 4. 增量演进流程

当 `spec/baseline/` 已存在时，委托 `arkts-spec-evolver` 执行。

<HARD-GATE>
所有涉及代码变更的流程（含全流程模式），必须经过两道用户确认门禁：
  Gate 1: spec 生成后 → 用户确认 spec
  Gate 2: plan 生成后 → 用户确认 plan
两道门禁通过后才可进入 execute 阶段。绝对禁止跳过任何一道门禁。
</HARD-GATE>

spec-evolver 支持 7 种工作模式，a2h-spec 根据用户意图自动选择：

| 用户意图 | 路由到的模式 | 说明 |
|---------|------------|------|
| "XX功能缺失" | create | 只生成 spec，等待用户确认 |
| "这个有 bug" | create | bugfix 类型，只生成 spec |
| "XX功能缺失，生成spec并实现" | create+plan+execute+verify | 全流程，自动在 Gate 1 和 Gate 2 暂停等待确认 |
| "修复 bug 并验证" | create+plan+execute+verify | 同上，两道门禁不可跳过 |
| "检查下还缺什么" | audit | 审计模式 |
| "查看 spec 状态" | status | 状态查询 |
| "为 F-xxx 生成计划" | plan | 为已有 spec 生成计划 |
| "执行 spec/features/..." | execute | 执行已审批的计划（需 status=planned） |
| "验证 F-xxx" | verify | 验证已完成的变更 |

---

## 5. 产出清单

### 初始迁移产出

| 阶段 | 产出 | 路径 | 说明 |
|------|------|------|------|
| Phase A | UI 快照数据 | `spec/baseline/ui-snapshots/page_NNNN_XxxActivity/` | 三源数据（view.xml + meta.json + screenshot.png） |
| Phase B | UI 总览 | `spec/baseline/ui-manifest.md` | 页面清单 + 全局约定 + 状态生命周期（≤200 行） |
| Phase B | UI 分页 Spec | `spec/baseline/ui/page_NNNN_XxxActivity.md` | 每页溯源 + 结构 + 状态接口 + 导航（≤100 行/文件） |
| Phase C | 功能总览 | `spec/baseline/feature-index.md` | 功能清单 + 依赖图 + 执行顺序（≤200 行） |
| Phase C | 基础设施 Spec | `spec/baseline/feature-base.md` | 数据模型 + DB + 网络 + 事件 + 偏好 + 公共组件库 |
| Phase C | 功能分 Spec | `spec/baseline/features/F00x-xxx.md` | 每功能自包含 Spec（≤300 行/文件） |

### 完整目录结构

```
spec/
├── baseline/                               ← 初始迁移基线（V1 后只读）
│   ├── ui-manifest.md                      ← 【UI 总】页面清单 + 全局约定
│   ├── ui/                                 ← 【UI 分】每页一个 spec
│   │   ├── page_0001_MainActivity.md
│   │   ├── page_0002_HomeFragment.md
│   │   └── ...
│   ├── ui-snapshots/                       ← 三源原始数据
│   │   ├── page_0001_MainActivity/
│   │   │   ├── view.xml
│   │   │   ├── meta.json
│   │   │   └── screenshot.png
│   │   └── ...
│   ├── feature-index.md                    ← 【功能 总】功能清单 + 依赖图
│   ├── feature-base.md                     ← 【功能 基础】共享基础设施
│   └── features/                           ← 【功能 分】每功能一个 spec
│       ├── F001-playback.md
│       ├── F002-subscription.md
│       └── ...
├── features/                               ← V1 后增量功能
├── bugfixes/                               ← V1 后 bug 修复
└── optimizations/                          ← V1 后优化
```

### 增量演进产出

| 阶段 | 产出 | 路径 |
|------|------|------|
| 增量功能 | 增量 spec | `spec/features/F0xx-xxx.md` |
| Bug 修复 | bugfix spec | `spec/bugfixes/B0xx-xxx.md` |
| 优化 | 优化 spec | `spec/optimizations/O0xx-xxx.md` |

### Style Configuration

Spec 输出文档（`ui-manifest.md`、`feature-index.md`）顶部追加 `Style Configuration` 节：

```yaml
## Style Configuration
style_set: none          # 或 wfhc-standard 等
```

此字段由 3.0b 步骤确定，a2h-plan / a2h-execute / a2h-verify 读取此字段决定是否加载风格 skills。
`style_set` 缺失时视为 `none`（向后兼容）。

---

## 6. 门控

### 初始迁移门控

```
Phase A（数据准备）
  │ 输出: 准备报告（页面清单 + confidence 评级）
  │ 自动进入 Phase B（无需审批）
  ▼
Phase B（UI 清单）
  │ 输出: ui-manifest.md + 分页 spec
  │ ★ Gate B: 用户审批 UI 清单
  ▼
Phase C（功能 Spec）
  │ 输出: feature-index.md + feature-base.md + features/
  │ ★ Gate C: 用户审批功能 Spec
  ▼
a2h-plan（生成执行计划）
```

Phase A 到 Phase B 自动衔接（数据准备报告仅供参考，不阻塞）。
Phase B 和 Phase C 各有独立审批门控。

### 增量演进门控

```
spec-evolver → spec 生成 → ★ Gate 1 → plan 生成 → ★ Gate 2 → execute
```

---

## 7. 触发 Prompt 示例

### 初始迁移

```
分析这个 Android 项目
```

```
开始迁移
```

```
生成迁移方案
```

```
帮我分析下迁移难度
```

### 增量演进

```
XX 功能缺失，需要补全
```

```
列表滚动有 bug，修复一下
```

### 审计

```
检查下 spec 和代码的差距
```

### 查看状态

```
查看所有增量 spec 的状态
```

---

## 8. 与 Domain Skill 的关系

a2h-spec **直接执行分析和生成**，Phase A 调用 android-ui-graph-builder 的 Python 脚本做确定性数据提取：

```
a2h-spec（直接执行分析）
  │
  ├─ 初始迁移:
  │   ├─ Phase A: 扫描 AndroidManifest + 调用 synthesize_meta_json.py / synthesize_view_xml.py
  │   ├─ Phase B: 直接生成 ui-manifest + 分页 spec
  │   └─ Phase C: 直接分析源码 + 生成 feature spec
  │
  └─ 增量演进:
      └─ arkts-spec-evolver — 7 种模式的增量 spec 管理
```

### 使用的 Domain Skill

| Skill | 用途 |
|-------|------|
| `android-ui-graph-builder` | Phase A 调用其 Python 脚本（synthesize_meta_json.py, synthesize_view_xml.py）做确定性数据提取 |
| `android-ui-graph-query` | 可选：查询 UI 图谱上下文，供 a2h-activity-converter 使用 |
| `arkts-spec-evolver` | 增量演进：V1 后的 bug 修复、功能补全、优化 |

---

## 9. 三源数据原则

a2h-spec Phase A 准备的三源数据是整个 v2 架构的基础。三源数据的核心原则：

**结构以 view.xml 为准，样式以源码为准，语义以 meta.json 为准。**

| 信息类型 | view.xml | meta.json | 源码 layout XML |
|---------|----------|-----------|----------------|
| 视图层级结构 | **主**（运行时真实层级） | — | 辅（静态定义） |
| bounds 坐标/尺寸 | **主**（精确像素） | — | — |
| 可见性状态 | **主**（运行时真实） | — | 辅（默认值） |
| 文本内容 | 有（运行时值） | 有（语义补充） | 有（默认值/resource ref） |
| 颜色/字体/样式 | **无** | — | **主**（完整样式定义） |
| 主题/Style 继承 | **无** | — | **主**（themes.xml + styles.xml） |
| Drawable/图标引用 | **无** | 部分（icon 字段） | **主**（`@drawable/ic_home`） |
| 资源名 | **无** | — | **主**（`@string/home_label`） |
| 导航目标 | **无** | **主**（navigation_targets） | — |
| 点击路径/页面关系 | **无** | **主**（click_path, came_from） | — |
| Activity/Fragment 映射 | **无** | **主**（activity 字段） | — |

a2h-activity-converter 消费顺序：
1. 读 meta.json → 理解"这个页面是什么、能做什么"
2. 读 view.xml → 构建精确的视图层级树
3. 读源码 layout XML + styles.xml + themes.xml → 补充样式、颜色、资源引用
4. 交叉验证：view.xml 层级 vs 源码 layout 层级，以 view.xml 为准，源码补充样式
5. 读 screenshot.png（如有）→ 最终视觉校验

---

## 10. 大型项目支持

| 项目规模 | 页面数 | Phase A 策略 | Phase B/C 策略 |
|---------|--------|-------------|---------------|
| 小 | <10 | 全量批量 | 单文件 feature-index 足够 |
| 中 | 10-30 | 全量批量 | 2-3 个 feature 组 |
| 大 | 30-100 | 批量 + 按需混合 | 按模块分组 feature |
| 超大 | 100+ | 按模块拆分子项目 | 每模块独立 feature-index |

上下文窗口管理：
- `ui-manifest.md` 控制在 200 行 → 全局视图始终可加载
- 每个 `ui/page_NNNN.md` 控制在 100 行 → converter agent 可附带加载
- `feature-index.md` 控制在 200 行 → 全局功能视图始终可加载
- 每个 `features/F00x.md` 控制在 300 行 → 单 agent 可完整加载
- `ui-snapshots` 数据由 agent 按需读取，不预加载
