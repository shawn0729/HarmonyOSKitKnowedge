---
name: arkts-ui-alignment
description: 帮助将 Android UI 设计迁移到 ArkTS/HarmonyOS 的等价实现。当用户需要匹配 Android Material Design 视觉效果、找到 Android 布局组件的 ArkTS 等价物、使用 SymbolGlyph 图标体系时触发。
---

# ArkTS UI Alignment — Android UI 迁移对齐

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定 Android 到 ArkTS 的视觉映射、布局约束和资源归属，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于界面结构对齐、组件等价替换、布局还原和样式迁移；入口路径 `references/harmonyos-sdk/arkui/routing.md`。
- Image Kit：用于图片显示一致性、视觉资源适配和图像质量校验；入口路径 `references/harmonyos-sdk/image-kit/routing.md`。

## API 版本

本 skill 基于 **API 12+**（HarmonyOS 5.0.0+）。UI 相关导入：

- ArkUI 组件：内置，无需额外导入
- SymbolGlyph：内置，资源引用 `$r('sys.symbol.xxx')`
- 弹窗：`import { promptAction } from '@kit.ArkUI'`

遇到版本兼容性或其他不确定的 ArkTS 知识点，参阅 arkts-knowledge-verifier skill。

---

## Android → ArkTS 组件映射表

| Android 元素 | ArkTS 组件 | 备注 |
|-------------|-----------|------|
| `BottomNavigationView` | 自定义 `Row` + `@Builder tabBarItem` | 不用 `Tabs` 在 Navigation 内部 |
| `BottomSheetDialogFragment` | `NavDestination` (全屏) 或 `Sheet` | 视需求选择 |
| `DrawerLayout` | `SideBarContainer` | 侧边栏 |
| `RecyclerView` | `List` + `LazyForEach` | 虚拟列表 |
| `ViewPager2` | `Swiper` | 翻页 |
| `CoordinatorLayout` | `Stack` + 自定义手势 | 需手动实现 |
| `CardView` | `Column` + `borderRadius` + `shadow` | 卡片 |
| `FloatingActionButton` | `Button` + 绝对定位 | FAB |
| `ProgressBar` (Linear) | `Progress({ type: ProgressType.Linear })` | 进度条 |
| `ProgressBar` (Circular) | `Progress({ type: ProgressType.Ring })` | 进度环 |
| `Toolbar` / `ActionBar` | `NavDestination` 标题栏 | 自动 |
| `AlertDialog` | `AlertDialog.show()` | 弹窗 |
| `PopupMenu` | `Menu` + `MenuItem` | 菜单 |
| `Snackbar` | `promptAction.showToast()` | 轻提示 |
| `ImageView` + Glide | `Image(url)` 或 `@ohos/imageknife` | 图片加载 |

> 详细映射 + 代码示例见 `references/layout-mapping.md`

---

## SymbolGlyph 图标体系

### 已验证可用名称（22 个）

以下名称经 DevEco Studio 编译验证，可安全使用：

```
house, list_bullet, envelope, square_grid_2x2, line_3_horizontal,
play_fill, pause_fill, arrow_down, checkmark, plus, trash,
magnifyingglass, chevron_right, chevron_left, lock, clock, gearshape,
arrow_left, arrow_right, forward_fill, backward_fill, speaker_wave_2_fill
```

### 已验证不存在 + 替代方案

| 猜测名称 | 替代方案 |
|---------|---------|
| `tray_arrow_down` | `envelope` |
| `dot_3_horizontal` / `ellipsis` | `line_3_horizontal` |
| `chart_bar` | `square_grid_2x2` |

### 使用规范

```typescript
// 标准用法
SymbolGlyph($r('sys.symbol.house'))
  .fontSize(22)
  .fontColor([Color.Black])

// 条件颜色（选中/未选中）
SymbolGlyph($r('sys.symbol.play_fill'))
  .fontSize(20)
  .fontColor(this.isActive ? [Color.Black] : ['#99182431'])
```

**规则**：
- 统一使用 `SymbolGlyph`，不混用 Unicode emoji
- `fontColor` 参数是**数组**：`[Color.Black]` 不是 `Color.Black`
- 不确定的名称标注 `[待验证]`，在 DevEco Studio 中编译确认

---

## 颜色系统映射

| Material 语义 | HarmonyOS 色值 | 用途 |
|-------------|---------------|------|
| primaryColor | `#007DFF` | 品牌蓝、主操作按钮 |
| surface | `#FAFAFA` | 卡片/面板背景 |
| background | `#FFFFFF` | 页面背景 |
| onSurface | `#182431` | 深色主文字 |
| onSurfaceVariant | `#99182431` | 次要文字（60% 不透明度） |
| divider | `#E0E0E0` | 分割线 |
| error | `#E84026` | 错误提示 |
| disabled | `#66182431` | 禁用态文字 |
| overlay | `#1A000000` | 蒙层/阴影（10% 黑） |
| pillBg | `#1F000000` | 药丸指示器背景（12% 黑） |

### 系统颜色资源

```typescript
// 推荐使用系统语义色（随深色模式自动切换）
$r('sys.color.ohos_id_color_text_primary')     // 主文字
$r('sys.color.ohos_id_color_text_secondary')   // 次要文字
$r('sys.color.ohos_id_color_background')       // 背景色
```

---

## 间距系统

采用 **4vp 基数**，保持视觉一致性：

| 级别 | 值 | 用途 |
|------|---|------|
| xs | 4vp | 紧凑间距 |
| sm | 8vp | 列表项内间距 |
| md | 12vp | 组件间距 |
| lg | 16vp | 区域间距、标准 padding |
| xl | 20vp | 大区域间距 |
| xxl | 24vp | 页面边距 |

```typescript
// 示例
Row() { ... }
  .padding({ left: 16, right: 16, top: 8, bottom: 8 })
  .margin({ top: 12 })
```

---

## Tab 栏方案

### 问题：Tabs 在 Navigation 内部

`Tabs` 放在 `Navigation` 内部时，`NavDestination` 子页面会覆盖整个区域（包括 Tab 栏）。

### 解决方案：自定义 Tab 栏放在 Navigation 外部

```typescript
Column() {
  // 内容区（Navigation 占满剩余空间）
  Navigation(this.navPathStack) {
    // Tab 内容根据 currentTabIndex 切换
    if (this.currentTabIndex === 0) { HomeComponent() }
    else if (this.currentTabIndex === 1) { QueueComponent() }
    // ...
  }
  .navDestination(this.routerMap)
  .mode(NavigationMode.Stack)
  .layoutWeight(1)

  // MiniPlayer（Navigation 外部，不被覆盖）
  if (this.isPlayerVisible && !this.isFullPlayerVisible) {
    MiniPlayerArea()
  }

  // 自定义 Tab 栏（Navigation 外部，不被覆盖）
  if (!this.isFullPlayerVisible) {
    CustomTabBar()
  }
}
```

---

## 药丸指示器 Tab 样式

Material 3 风格的底部 Tab 栏（药丸形背景指示选中态）：

```typescript
@Builder
tabBarItem(index: number, title: Resource, icon: Resource) {
  Column() {
    // 药丸形背景
    Column() {
      SymbolGlyph(icon)
        .fontSize(22)
        .fontColor(this.currentTabIndex === index ?
          [Color.Black] : ['#99182431'])
    }
    .width(48)
    .height(28)
    .borderRadius(14)
    .backgroundColor(this.currentTabIndex === index ?
      '#1F000000' : '#00000000')
    .justifyContent(FlexAlign.Center)

    Text(title)
      .fontSize(10)
      .fontColor(this.currentTabIndex === index ?
        '#182431' : '#99182431')
      .margin({ top: 2 })
  }
  .layoutWeight(1)
  .justifyContent(FlexAlign.Center)
  .height('100%')
  .onClick(() => { this.currentTabIndex = index; })
}
```

> 完整代码见 `references/visual-patterns.md`

---

## 封面图 + Fallback 模式

网络图片 + 文字首字母占位符：

```typescript
if (this.coverUrl.length > 0) {
  Image(this.coverUrl)
    .width(40).height(40)
    .borderRadius(6)
    .objectFit(ImageFit.Cover)
} else {
  Column() {
    Text(this.title.length > 0 ?
      this.title.charAt(0).toUpperCase() : '?')
      .fontSize(18)
      .fontWeight(FontWeight.Bold)
      .fontColor(Color.White)
  }
  .width(40).height(40)
  .borderRadius(6)
  .backgroundColor('#BDBDBD')
  .justifyContent(FlexAlign.Center)
}
```

---

## 常见错误

### 1. Emoji vs SymbolGlyph 混用
```typescript
// ❌ emoji 大小不可控
Text('📋').fontSize(22)  // 实际渲染大小不确定

// ✓ SymbolGlyph 大小精确可控
SymbolGlyph($r('sys.symbol.list_bullet'))
  .fontSize(22)
  .fontColor([Color.Black])
```

### 2. 使用不存在的 symbol 名称
```typescript
// ❌ 编译报 Unknown resource name
SymbolGlyph($r('sys.symbol.tray_arrow_down'))

// ✓ 使用已验证的名称或查阅清单
SymbolGlyph($r('sys.symbol.envelope'))
```

### 3. Tabs 在 Navigation 内部
```typescript
// ❌ NavDestination 会覆盖 Tab 栏
Navigation() {
  Tabs() { ... }  // Tab 栏被子页面覆盖
}

// ✓ Tab 栏放在 Navigation 外部
Column() {
  Navigation() { ... }.layoutWeight(1)
  CustomTabBar()  // 始终可见
}
```

---

## 生成检查清单

- [ ] Android 组件已查对照表找到 ArkTS 等价物
- [ ] 图标统一使用 SymbolGlyph（不使用 emoji）
- [ ] Symbol 名称来自已验证清单
- [ ] 颜色使用 HarmonyOS 色值映射
- [ ] 间距使用 4vp 基数
- [ ] Tab 栏放在 Navigation 外部
- [ ] 封面图有 fallback 占位
- [ ] 没有使用 `any` 类型
- [ ] 导入使用 `@kit.*` 格式

---

## 跨 Skill 协作

| 需要什么 | 读取哪里 |
|---------|---------|
| UI 组件详细模板 | `arkts-component-builder/SKILL.md` |
| 导航方案 | `arkts-navigation-builder/SKILL.md` |
| 状态管理 | `arkts-state-manager/SKILL.md` |
| 动画效果 | `arkts-animation-builder/SKILL.md` |
| 业务功能模式 | `arkts-pattern-library/SKILL.md` |
| 验证 API | `arkts-knowledge-verifier/SKILL.md` |

> 完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

- `references/layout-mapping.md` — Android→ArkTS 组件映射详细版 + 代码示例 + 单位转换
- `references/visual-patterns.md` — 药丸 Tab 栏 + 封面 fallback + MiniPlayer + SymbolGlyph + 阴影卡片
- 遇到版本兼容性或其他不确定的 ArkTS 知识点，参阅 **arkts-knowledge-verifier** skill
