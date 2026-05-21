---
name: app-relationship-tree
description: 多源聚合生成 app-relationship-tree.json（页面关系树）。从 android-ui-graph-builder 产件（Screen/Component/Navigation/Containment JSON）、a2h-spec 产件（page_NNNN.md）、design_ref.md、以及目标端 ArkTS 源码中提取并融合信息，输出统一的关系树。当用户说"生成关系树"、"页面关系"、"组件关系"、"navigation tree"时触发。
---

# app-relationship-tree — 多源聚合页面关系树生成器

## 1. 定位

本 skill **不是从零扫描源码**，而是**聚合已有产件**来生成 `app-relationship-tree.json`。

在 Android→HarmonyOS 迁移流水线中，上游 skill 已经分析过 Android 源码并产出了结构化数据。本 skill 的职责是把这些分散的、格式不统一的产件融合为一棵完整的关系树。

```
┌─────────────────────────────────────────────────────────┐
│                    上游产件（输入）                        │
│                                                         │
│  ① android-ui-graph-builder 产件（最结构化）              │
│     Screen.json ─── 每个 Activity/Fragment 的元数据       │
│     Component.json ─── 每个 UI 组件的完整属性树            │
│     Navigation_Edge.json ─── 页面间跳转边                 │
│     Containment_Edge.json ─── 组件父子嵌套边              │
│                                                         │
│  ② a2h-spec 产件（最覆盖全面）                            │
│     spec/baseline/ui/page_NNNN.md × N                   │
│       ## navigation ─── inbound/outbound 跳转            │
│       ## state interface ─── 状态变量                     │
│       ## conversion decisions ─── 组件映射决策            │
│       ## page structure ─── 布局层次描述                  │
│                                                         │
│  ③ design_ref.md（宏观架构）                              │
│     PlantUML 导航图 ─── 主干流程（~30条边）                │
│     模块划分 ─── 功能域聚类参考                            │
│                                                         │
│  ④ 目标端 ArkTS 源码（如迁移已完成）                       │
│     pages/*.ets ─── build() 中的实际 UI 组件              │
│     components/*.ets ─── Fragment 级组件                  │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
              ┌──────▼──────┐
              │ 本 Skill     │
              │ 多源聚合      │
              │ + 交叉校验    │
              └──────┬──────┘
                     │
                     ▼
        spec/app-relationship-tree.json
```

**核心原则：每个字段从最权威的数据源提取，多源交叉验证，不重复发明轮子。**

---

## 2. 数据源优先级矩阵

不同字段应从不同数据源提取。下表定义了每个字段的**首选源**和**备选源**：

| 输出字段 | 首选数据源 | 备选数据源 | 说明 |
|---------|-----------|-----------|------|
| **`app` 元信息** | 项目配置文件 (`oh-package.json5`, `module.json5`, `build.gradle`) | — | 直接读配置 |
| **`features` 功能域** | `design_ref.md` PlantUML + page spec 的 module 字段 | android-ui-graph-builder Screen.json 的 package 聚类 | 需要语义理解，LLM 做 |
| **`dependency_graph`** | 从 features 的 import/跳转关系推导 | design_ref.md 的分层描述 | 拓扑排序 |
| **`pages[].navigation`** | **`page_NNNN.md` 的 `## navigation` 段** | Navigation_Edge.json | page spec 更全面，graph-builder 的 navigation 可能漏边 |
| **`pages[].state_variables`** | **`page_NNNN.md` 的 `## state interface` 段** | 扫描 ArkTS 源码的 @State/@Local | page spec 已整理好类型和来源 |
| **`pages[].builders`** | 扫描 ArkTS 源码的 @Builder | — | 只有源码有 |
| **`pages[].sub_components`** | **扫描 ArkTS `.ets` 源码** | Component.json + Containment_Edge.json 反推 | ArkTS 源码最准确（已迁移的组件） |
| **`pages[].sub_components`**（迁移前） | **Component.json + Containment_Edge.json** | `page_NNNN.md` 的 `## page structure` | 迁移前没有 ArkTS 源码，用 graph-builder 产件 |
| **`fragments[]`** | 扫描 ArkTS 组件源码 | Screen.json (type=Fragment) + Component.json | 同上 |
| **`pages[].description`** | `page_NNNN.md` 的 `## page structure` Description | Screen.json 的 name + type | page spec 有人类可读描述 |

### 关键判断：迁移前 vs 迁移后

```
if ArkTS 源码存在 (pages/*.ets):
    sub_components → 从 ArkTS 源码提取（Phase 4A）
    builders → 从 ArkTS 源码提取
    state_variables → 优先 page spec，用 ArkTS 补充 decorator 信息
else:
    sub_components → 从 Component.json + Containment_Edge.json 转换（Phase 4B）
    builders → 不适用
    state_variables → 从 page spec 提取
```

---

## 3. 输入清单

### 3.1 必选输入（至少满足一组）

**组 A — 有 a2h-spec 产件（推荐）：**

| 输入 | 路径模式 | 说明 |
|------|---------|------|
| page spec 文件 | `spec/baseline/ui/page_NNNN_*.md` | 每页一个，包含 navigation/state/structure |
| design_ref.md | `spec/ref/design_ref.md` | 架构概览 + PlantUML 导航图 |

**组 B — 有 android-ui-graph-builder 产件：**

| 输入 | 路径模式 | 说明 |
|------|---------|------|
| Screen.json | `outputs/Screen.json` 或用户指定 | 页面元数据 |
| Component.json | `outputs/Component.json` | 组件属性 |
| Navigation_Edge.json | `outputs/Navigation_Edge.json` | 导航边 |
| Containment_Edge.json | `outputs/Containment_Edge.json` | 嵌套边 |

**组 C — 有目标端源码（迁移后补全 sub_components）：**

| 输入 | 路径模式 | 说明 |
|------|---------|------|
| ArkTS 页面文件 | `entry/src/main/ets/pages/*.ets` | 目标端页面 |
| ArkTS 组件文件 | `entry/src/main/ets/components/*.ets` | 目标端 Fragment |

> 三组可以任意组合。覆盖越多，输出越完整。只有组 A 也能生成可用的关系树。

### 3.2 可选输入

| 输入 | 路径模式 | 说明 |
|------|---------|------|
| spec.md | `spec/ref/spec_ref.md` 或 `spec/ref/meizhaoAI_spec.md` | 业务需求规格，辅助功能域划分 |
| feature-index.md | `spec/baseline/feature-index.md` | 功能清单 + 优先级 |
| 已有的 app-relationship-tree.json | `spec/app-relationship-tree.json` | 增量更新模式 |

---

## 4. 输出 Schema

### 4.1 整体结构

```jsonc
{
  "app": { /* 元信息 */ },
  "features": [ /* 功能域列表 */ ],
  "dependency_graph": { /* 分层依赖图 */ },
  "fragments": [ /* Fragment/子组件定义 */ ],
  "pages": [ /* 所有页面 */ ]
}
```

### 4.2 `app` — 应用元信息

```jsonc
{
  "name": "美照AI",
  "package": "com.mzsmli.czocsi",
  "platform": "HarmonyOS (ArkTS)",       // 或 "Android"
  "migrated_from": "Android",            // 可选
  "total_pages": 81,
  "total_features": 16,
  "total_components": 3,                 // Fragment 数量
  "generated_at": "2026-04-13"
}
```

### 4.3 `features[i]` — 功能域

```jsonc
{
  "id": "F001",
  "name": "App Launch & Navigation",
  "module": "app",
  "priority": "P0",                      // P0 > P1 > P2
  "pages": ["SplashPage", "HomePage"],
  "dependencies": ["F014", "F015"],
  "layer": 5,
  "extended_features": [...]             // 可选：子功能域
}
```

### 4.4 `dependency_graph`

```jsonc
{
  "layers": [
    { "layer": 0, "name": "Foundation", "features": ["F015", "F012"] },
    { "layer": 1, "name": "Auth+Feed",  "features": ["F002", "F014"] }
  ]
}
```

### 4.5 `fragments[i]`

```jsonc
{
  "name": "HomeFragmentComponent",
  "file": "components/HomeFragmentComponent.ets",
  "host_page": "HomePage",
  "host_tab_index": 0,
  "feature_ids": ["F001", "F014"],
  "state_variables": [
    { "name": "currentMenuPage", "type": "number", "decorator": "@State" }
  ],
  "builders": ["DotIndicator", "MenuItemCell"],
  "callbacks_to_parent": ["onDeleteModeChanged"],
  "sub_components": [ /* 同 page.sub_components */ ],
  "gestures": [
    { "type": "swipe", "component": "Swiper", "action": "switch menu page" }
  ]
}
```

### 4.6 `pages[i]`

```jsonc
{
  "name": "HSVFXPreviewPage",
  "file": "pages/HSVFXPreviewPage.ets",
  "priority": "P0",
  "feature_ids": ["F004"],
  "description": "AI特效预览页，展示处理前后对比和模板选择",
  "components": ["HSVFXViewModel"],
  "state_variables": [
    { "name": "toolType", "type": "string", "decorator": "@Local" }
  ],
  "builders": ["TitleBar", "ComparisonCard"],
  "navigation": {
    "inbound": [
      { "source": "HomePage", "trigger": "click (AI特效)", "params": "toolType" }
    ],
    "outbound": [
      { "target": "AlbumsPage", "trigger": "click (立即体验)", "type": "pushPath" }
    ]
  },
  "sub_components": [ /* 见 4.7 */ ],
  "gestures": [
    { "type": "scroll", "component": "Grid", "direction": "vertical" }
  ]
}
```

### 4.7 `sub_components[i]` Schema

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 组件语义名（TitleBar, BackButton） |
| `type` | string | 是 | 组件类型：Row / Column / Stack / Image / Text / Button / Grid / List / Swiper / Web / Video / TextInput / TextArea / Slider / Checkbox / Progress / Dialog / CustomComponent |
| `description` | string | 是 | 简要中文描述 |
| `trigger` | string | 否 | `click` / `swipe` / `scroll` / `long_press` / `input` / `pinch` / `pull` / `auto` |
| `target` | string | 否 | 触发后导航到的目标页面名 |
| `action` | string | 否 | 触发后执行的动作（非导航场景） |
| `visible_when` | string | 否 | 条件可见性表达式 |
| `items` | array | 否 | Grid/List/Swiper 中的子项 |
| `interactions` | array | 否 | 多交互场景（如登录/未登录跳不同页面） |

---

## 5. 执行流程

```
Phase 1: 探测 — 检查哪些数据源可用
    ↓
Phase 2: 骨架 — 从 page spec + design_ref 提取 features + dependency_graph
    ↓
Phase 3: 页面 — 从 page spec 聚合 navigation + state_variables
    ↓
Phase 4: 组件 — 从 ArkTS 源码（4A）或 graph-builder 产件（4B）提取 sub_components
    ↓
Phase 5: Fragment — 提取 Fragment 深层结构
    ↓
Phase 6: 融合 — 多源交叉验证 + 补全
    ↓
Phase 7: 输出 — 写入 spec/app-relationship-tree.json
```

---

### Phase 1: 探测可用数据源

逐项检测，记录可用性：

```python
sources = {}

# 组 A: a2h-spec 产件
page_specs = glob("spec/baseline/ui/page_*.md")
sources["page_specs"] = page_specs  # 可能 0 或 80 个
sources["design_ref"] = exists("spec/ref/design_ref.md")
sources["spec_ref"] = exists("spec/ref/spec_ref.md") or exists("spec/ref/meizhaoAI_spec.md")

# 组 B: android-ui-graph-builder 产件
for f in ["Screen.json", "Component.json", "Navigation_Edge.json", "Containment_Edge.json"]:
    sources[f] = find_file(f)  # 在 outputs/ 或 mnt/user-data/ 或用户指定路径

# 组 C: 目标端 ArkTS 源码
sources["arkts_pages"] = glob("entry/src/main/ets/pages/*.ets")
sources["arkts_components"] = glob("entry/src/main/ets/components/*.ets")

# 判断模式
if sources["arkts_pages"]:
    sub_components_mode = "4A_arkts_source"
elif sources["Component.json"]:
    sub_components_mode = "4B_graph_builder"
else:
    sub_components_mode = "4C_page_spec_only"  # 最粗粒度
```

打印探测结果：
```
=== 数据源探测 ===
[✓] page spec 文件: 80 个
[✓] design_ref.md: 存在
[✗] Screen.json: 未找到
[✗] Component.json: 未找到
[✓] ArkTS 页面文件: 81 个
[✓] ArkTS 组件文件: 3 个
→ sub_components 提取模式: 4A (ArkTS 源码)
→ navigation 提取模式: page spec 聚合
```

---

### Phase 2: 骨架 — features + dependency_graph

**Step 2.1: 读取 design_ref.md 中的 PlantUML 导航图**

```
提取 @startuml ... @enduml 块中的 --> 关系
SplashActivity --> HomeActivity : 非首次
HomeFragment --> AiPaintChatActivity : AI绘画
...
```

这提供了**主干流程**，但不完整（~30 条边）。

**Step 2.2: 从 page spec 提取 module 信息**

```
# 每个 page_NNNN.md 的 traceability 段有:
# - Module: aipaint / aivideo / pay / common_mz / app / album
# 按 module 聚类 → 初步功能域
```

**Step 2.3: 功能域聚合规则**

```
1. 相同 module 的页面 → 同一功能域候选
2. PlantUML 中有直接关系的页面 → 相关功能域
3. 页面名前缀相同 → 子功能域（AI*, Video*, Coin*）
4. 最终由 LLM 做语义聚合，生成 features[] 和 dependency_graph
```

**Step 2.4: 优先级标注**

```
P0: page spec 中 Priority 字段为 P0 的页面所在功能域
P1: Priority 为 P1
P2: Priority 为 P2 或无标注
```

**Step 2.5: 依赖分层**

拓扑排序规则：如果 Feature A 的页面跳转到 Feature B 的页面，则 A 依赖 B，A.layer > B.layer。

---

### Phase 3: 页面 — 从 page spec 聚合

对每个 `page_NNNN.md` 文件提取：

**Step 3.1: 基本信息**

```markdown
# page_0012: AiPaintChatActivity
## traceability
- ArkTS target: `entry/src/main/ets/pages/AiPaintChatPage.ets`   ← name = "AiPaintChatPage"
- Module: aipaint                                                  ← feature_ids 参考
- Priority: P0 | Batch: 2                                         ← priority
```

**Step 3.2: navigation**

```markdown
## navigation
| trigger | target page | type |
|---------|-------------|------|
| Back button | previous page | router.back() |              ← outbound
| Image click in chat | ChatPaintDetailsPage | router.pushUrl | ← outbound
```

转换为：
```json
{
  "navigation": {
    "inbound": [],   // 从其他页面的 outbound 反向推导
    "outbound": [
      { "target": "ChatPaintDetailsPage", "trigger": "click (Image in chat)", "type": "pushUrl" }
    ]
  }
}
```

**Step 3.3: state_variables**

```markdown
## state interface
| @State variable | type | data source | related feature |
| fromType | number | router params | 0=create, 1=fix |
| chatMessages | Array<PaintChatMessage> | API SSE streaming | Message list data |
```

转换为：
```json
{
  "state_variables": [
    { "name": "fromType", "type": "number", "decorator": "@State" },
    { "name": "chatMessages", "type": "Array<PaintChatMessage>", "decorator": "@State" }
  ]
}
```

> **decorator 补全规则**：page spec 中统一写 `@State`，但如果有 ArkTS 源码可用，从源码中读取实际的 decorator（可能是 `@Local`、`@Prop`、`@StorageLink` 等 V2 装饰器）。

**Step 3.4: description**

从 `## page structure` 的 **Description** 行提取。

**Step 3.5: 如果有 android-ui-graph-builder 的 Navigation_Edge.json**

交叉补全：page spec 的 navigation 可能标注了 `TODO`，用 Navigation_Edge.json 补全具体的 target 和 mechanism。

---

### Phase 4A: sub_components — 从 ArkTS 源码提取（迁移已完成时）

**这是最耗时的阶段，使用并行分批处理。**

**Step 4A.1: 分批策略**

```
pages = glob("entry/src/main/ets/pages/*.ets")
batch_size = ceil(len(pages) / 4)
# 4 个并行 Agent，每批 ~20 个文件
```

**Step 4A.2: Agent Prompt 模板**

```
读取以下 N 个 ArkTS 页面文件，提取每个页面的 sub_components。

文件路径: {project_root}/entry/src/main/ets/pages/
页面列表: {page_list}

对每个页面，从 build() 和 @Builder 方法中提取所有可见 UI 组件，返回 JSON：

{
  "PageName1": [
    {
      "name": "组件语义名",
      "type": "ArkUI组件类型",
      "description": "中文描述",
      "trigger": "click|swipe|scroll|long_press|input|pinch|pull",
      "target": "目标页面名",
      "action": "动作描述",
      "visible_when": "条件表达式"
    }
  ]
}

规则：
1. 必须读取每个文件的完整内容，不可跳过
2. name 使用语义名（TitleBar, BackButton），不用 Row1, Column2
3. Dialog 也记录为 sub_component，type 为 "Dialog" 或 "CustomDialog"
4. trigger 判断：onClick→click, SwipeGesture→swipe, LongPressGesture→long_press,
   TextInput/TextArea→input, Slider→scroll, Swiper→swipe, Refresh→pull
5. visible_when：仅当组件被 if(condition) 包裹时记录
6. 只返回 JSON，不要解释文字
```

**Step 4A.3: trigger 类型判断规则**

| ArkTS 源码模式 | trigger 值 |
|---------------|-----------|
| `.onClick(() => { ... })` | `click` |
| `.gesture(SwipeGesture(...))` | `swipe` |
| `.gesture(LongPressGesture(...))` | `long_press` |
| `.gesture(PinchGesture(...))` | `pinch` |
| `Swiper` 组件 | `swipe`（隐含） |
| `TextInput` / `TextArea` | `input`（隐含） |
| `Slider` | `scroll`（隐含） |
| `Refresh` 组件 | `pull`（隐含） |
| `List` / `Grid` / `Scroll` | `scroll`（隐含，当内容可能超屏） |
| `Checkbox` / `Toggle` | `click`（隐含） |
| 页面自动跳转（timer / onAppear） | `auto` |

---

### Phase 4B: sub_components — 从 graph-builder 产件转换（迁移前）

当没有 ArkTS 源码时，从 Component.json + Containment_Edge.json 生成 sub_components。

**Step 4B.1: 构建 Screen → Component 树**

```python
# 从 Containment_Edge.json 构建父子关系
for edge in containment_edges:
    parent_children[edge["parent"]].append(edge["child"])

# 从 Screen.json 获取每个 screen 的根组件
for screen in screens:
    root_component = find_root(screen["id"], containment_edges)
    tree = build_tree(root_component, parent_children, components_by_id)
```

**Step 4B.2: Component → sub_component 转换**

```python
def convert_component(comp, nav_edges):
    sc = {
        "name": comp["android_id"] if comp["android_id"] != "none"
               else f"{comp['class_short']}",
        "type": android_to_arkui_type(comp["class_short"]),
        "description": infer_description(comp),
    }
    # trigger: 检查 behavior_attrs.onClick 或关联的 Navigation_Edge
    nav = find_nav_by_source_component(comp["id"], nav_edges)
    if nav:
        sc["trigger"] = "click"
        sc["target"] = extract_page_name(nav["to"])
    elif comp["behavior_attrs"].get("onClick") not in [None, "unknown"]:
        sc["trigger"] = "click"

    # visible_when: 检查 behavior_attrs.visibility
    if comp.get("behavior_attrs", {}).get("visibility") == "gone":
        sc["visible_when"] = "条件控制（默认隐藏）"

    return sc
```

**Step 4B.3: Android → ArkUI 组件类型映射**

| Android class_short | ArkUI type |
|-------------------|-----------|
| LinearLayout (horizontal) | Row |
| LinearLayout (vertical) | Column |
| ConstraintLayout | Column (简化) |
| FrameLayout | Stack |
| RelativeLayout | Stack |
| RecyclerView | List / Grid / WaterFlow |
| ScrollView | Scroll |
| ViewPager2 | Swiper |
| ImageView | Image |
| TextView | Text |
| EditText | TextInput / TextArea |
| Button | Button / Text |
| CheckBox | Checkbox |
| SeekBar | Slider |
| ProgressBar | Progress |
| WebView | Web |
| VideoView | Video |
| Toolbar | Row (TitleBar) |

**Step 4B.4: 限制**

graph-builder 产件能提供组件**结构**但缺少：
- 语义化的 name（只有 android_id 或 class_short）
- 中文 description
- 精确的 trigger（clickable_elements 可能为空）
- visible_when 的具体条件表达式

这些需要 LLM 根据上下文推断或标注为 "TODO"。

---

### Phase 4C: sub_components — 仅从 page spec 推断（最粗粒度）

当既没有 ArkTS 源码也没有 graph-builder 产件时，从 `page_NNNN.md` 的以下段落推断：

```markdown
## page structure
**Layout hierarchy**: ConstraintLayout root: ViewPager2(content) + Group(bottom tab) + ...

## conversion decisions
| Android widget | ArkTS component | Notes |
| TitleBar (com.hjq.bar) | Custom Row (TitleBarBuilder) | Back button + centered title |
| RecyclerView (rv_paint_chat) | List + ForEach | Chat message list |
```

从 conversion decisions 表格的每行生成一个 sub_component：
```json
{
  "name": "ChatList",           // 从 Notes 推断
  "type": "List",               // 从 ArkTS component 列
  "description": "Chat message list"  // 从 Notes 列
}
```

> 这是最粗粒度的模式，sub_components 数量少、缺少 trigger/target/visible_when。但足够生成骨架供后续补全。

---

### Phase 5: Fragment — 深层结构

**Step 5.1: 识别 Fragment**

```
来源 1: ArkTS 组件目录中文件名含 "Fragment" 的 .ets 文件
来源 2: Screen.json 中 type === "Fragment" 的条目
来源 3: page spec 中 traceability 提到 Fragment 的页面
```

**Step 5.2: 提取**

对每个 Fragment，执行与 Phase 4 相同的 sub_components 提取，额外提取：

- `host_page`: grep Fragment 文件名在哪个页面的 import/build 中出现
- `host_tab_index`: 如果宿主有 Tab/Swiper，确定对应索引
- `callbacks_to_parent`: 扫描 `@Event`、`@Link`、`@Prop` 反向传递
- `gestures[]`: 组件级手势

---

### Phase 6: 融合与校验

**Step 6.1: inbound 自动补全**

```python
# 从所有页面的 outbound 反向推导 inbound
for page in pages:
    for out in page["navigation"]["outbound"]:
        target = find_page(out["target"])
        if target:
            target["navigation"]["inbound"].append({
                "source": page["name"],
                "trigger": out["trigger"]
            })
```

**Step 6.2: 多源交叉验证**

当同时有 page spec 和 Navigation_Edge.json 时：

```
for each page:
    spec_targets = {out.target for out in page_spec.navigation.outbound}
    graph_targets = {edge.to for edge in nav_edges if edge.from == screen_id}

    only_in_spec = spec_targets - graph_targets
    only_in_graph = graph_targets - spec_targets

    if only_in_spec:
        INFO: "page spec 有但 graph-builder 没有: {only_in_spec}"
        # 保留（page spec 通常更全面，因为 graph-builder 可能漏掉动态导航）

    if only_in_graph:
        INFO: "graph-builder 有但 page spec 没有: {only_in_graph}"
        # 补充到结果中
```

**Step 6.3: target 有效性验证**

```
for each page:
    for each outbound target:
        if target not in all_page_names:
            WARN: "未知目标页: {target}"
    for each sub_component with target:
        if sc.target not in all_page_names:
            WARN: "组件 {sc.name} 引用了未知页面: {sc.target}"
```

**Step 6.4: 孤儿页面检测**

```
for each page:
    if page.navigation.inbound is empty and page.name != "Index":
        WARN: "孤儿页面: {page.name}"
```

**Step 6.5: Feature 覆盖度**

```
all_featured_pages = union(features[*].pages)
uncovered = all_page_names - all_featured_pages
if uncovered:
    WARN: "未归入任何功能域: {uncovered}"
```

---

### Phase 7: 输出

**Step 7.1: 组装**

```python
result = {
    "app": app_meta,               # Phase 1
    "features": features,          # Phase 2
    "dependency_graph": dep_graph,  # Phase 2
    "fragments": fragments,        # Phase 5
    "pages": pages                 # Phase 3 + 4
}
```

**Step 7.2: 写入**

```
路径: spec/app-relationship-tree.json
编码: UTF-8, ensure_ascii=False
缩进: 2 spaces
```

**Step 7.3: 摘要**

```
=== app-relationship-tree.json 生成完成 ===
数据源: page_spec(80) + design_ref + ArkTS_source(81+3)
页面: 81 | 功能域: 16 | Fragment: 3
组件总数: 595 | 导航边: 142
trigger 分布: click=380, scroll=45, swipe=28, input=32, ...
校验: 孤儿页面=0, 未知target=0, 未覆盖页面=0
```

---

## 6. 增量更新模式

当 `spec/app-relationship-tree.json` 已存在时：

```bash
# 检测 ArkTS 源码变更
git diff --name-only HEAD~N -- 'entry/src/main/ets/pages/' 'entry/src/main/ets/components/'
```

- 仅对变更文件重新执行 Phase 4（sub_components 提取）
- 保留未变更页面的现有数据
- 全量重新执行 Phase 6（校验），因为导航关系可能受影响
- 更新 `app.generated_at`

---

## 7. 并行策略

| 阶段 | 并行方式 | 预期耗时 |
|------|---------|---------|
| Phase 1 (探测) | 串行 glob | 5s |
| Phase 2 (骨架) | 串行，读 design_ref + page specs | 1-2min |
| Phase 3 (页面聚合) | 串行，遍历 80 个 page spec | 2-3min |
| Phase 4A (ArkTS sub_components) | **4 个并行 Agent**，每批 ~20 页 | 3-5min |
| Phase 4B (graph-builder 转换) | Python 脚本，串行 | 30s |
| Phase 5 (Fragment) | 串行（通常 <5 个） | 1-2min |
| Phase 6 (融合校验) | 串行 | 15s |
| Phase 7 (输出) | 串行 | 5s |
| **总计** | | **~8-12min** |

---

## 8. 常见陷阱

| 陷阱 | 说明 | 应对 |
|------|------|------|
| page spec 的 Activity 名 ≠ ArkTS 的页面名 | `AiPaintChatActivity` → `AiPaintChatPage` | 用 page spec 的 `ArkTS target` 字段做映射 |
| page spec navigation 中有 TODO | `TODO: startPortfolio()` | 标记为 `"target": "TODO"` 或从 Navigation_Edge.json 补全 |
| graph-builder 的 clickable_elements 为空 | 脚本未能从源码提取 | 不依赖此字段，用 page spec 的 navigation 段替代 |
| 动态导航目标 | `pushPath({ name: variable })` | 标注为 `"target": "dynamic({variable})"` |
| 条件导航 | if(isLoggedIn) → A else → B | 使用 `interactions` 数组 |
| Fragment 嵌套 | Fragment A 内嵌 Fragment B | 在 A 的 sub_components 中记录 B |
| 多 Tab 页面 | Tabs/Swiper 切换不同内容 | 每个 Tab 内容标注 `visible_when: "tabIndex === N"` |
| page spec 的 state variable 缺少 decorator 细节 | 统一写 @State | 如有 ArkTS 源码，读取实际的 @Local/@Prop/@StorageLink 覆盖 |
| Screen.json 中 Fragment 的 parent_activity | 可能为 "unknown" | 用 page spec 的 traceability 中 Fragment 信息补全 |

---

## 9. 质量检查清单

- [ ] 每个 page 都有 `sub_components`（不允许空数组）
- [ ] 每个有返回按钮的页面都有 BackButton sub_component
- [ ] 所有 `navigation.outbound.target` 都能在 pages 列表中找到
- [ ] 所有 `sub_components[].target` 都能在 pages 列表中找到
- [ ] `features[].pages` 的并集覆盖所有页面
- [ ] `dependency_graph.layers` 包含所有 feature ID
- [ ] `app.total_pages` === `pages.length`
- [ ] inbound 与 outbound 双向一致
- [ ] JSON 有效，UTF-8，中文正常
