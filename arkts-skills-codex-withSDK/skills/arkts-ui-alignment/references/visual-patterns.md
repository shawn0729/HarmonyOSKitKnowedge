# 视觉模式参考

> 药丸 Tab 栏、封面 fallback、MiniPlayer、SymbolGlyph、阴影卡片。

---

## 药丸 Tab 栏完整代码

Material 3 风格底部导航栏（来自 AntennaPod Index.ets）：

```typescript
@Component
struct Index {
  @StorageLink('currentTabIndex') currentTabIndex: number = 0;

  @Builder
  tabBarItem(index: number, title: Resource, icon: Resource) {
    Column() {
      // 药丸形灰色背景（选中态）
      Column() {
        SymbolGlyph(icon)
          .fontSize(22)
          .fontColor(this.currentTabIndex === index ?
            [Color.Black] : ['#99182431'])
      }
      .width(48)
      .height(28)
      .borderRadius(14)  // 药丸形
      .backgroundColor(this.currentTabIndex === index ?
        '#1F000000' : '#00000000')  // 选中时 12% 黑色
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)

      // 标签文字
      Text(title)
        .fontSize(10)
        .fontColor(this.currentTabIndex === index ?
          '#182431' : '#99182431')
        .margin({ top: 2 })
    }
    .layoutWeight(1)  // 等分宽度
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .onClick(() => {
      this.currentTabIndex = index;
    })
  }

  build() {
    Column() {
      // 内容区
      Navigation(this.navPathStack) {
        if (this.currentTabIndex === 0) { HomeComponent() }
        else if (this.currentTabIndex === 1) { QueueComponent() }
        else if (this.currentTabIndex === 2) { InboxComponent() }
        else if (this.currentTabIndex === 3) { SubscriptionComponent() }
        else { MoreComponent() }
      }
      .navDestination(this.routerMap)
      .hideTitleBar(true)
      .mode(NavigationMode.Stack)
      .layoutWeight(1)

      // 自定义 Tab 栏 — Navigation 外部
      Row() {
        this.tabBarItem(0, $r('app.string.tab_home'), $r('sys.symbol.house'))
        this.tabBarItem(1, $r('app.string.tab_queue'), $r('sys.symbol.list_bullet'))
        this.tabBarItem(2, $r('app.string.tab_inbox'), $r('sys.symbol.envelope'))
        this.tabBarItem(3, $r('app.string.tab_subscriptions'),
          $r('sys.symbol.square_grid_2x2'))
        this.tabBarItem(4, $r('app.string.tab_more'),
          $r('sys.symbol.line_3_horizontal'))
      }
      .width('100%')
      .height(56)
      .backgroundColor(Color.White)
      .border({ width: { top: 0.5 }, color: '#E0E0E0' })
    }
  }
}
```

### 关键设计点

- `layoutWeight(1)` 让每个 tab 等分宽度
- `borderRadius(14)` + `height(28)` 实现药丸形
- `'#1F000000'` = 12% 不透明黑色，作为选中指示器
- Tab 栏放在 `Column` 最底部，不被 `Navigation` 的子页面覆盖
- 使用 `@StorageLink` 而非 `@State`，支持其他组件修改 Tab 索引

---

## 封面图 + Fallback 模式

网络图片 + 文字首字母占位符（来自 AntennaPod Index.ets）：

```typescript
// 完整封面组件（含 fallback）
@Builder
coverImage(coverUrl: string, feedTitle: string,
  size: number, radius: number) {
  if (coverUrl.length > 0) {
    // 有图片 URL → 显示网络图片
    Image(coverUrl)
      .width(size)
      .height(size)
      .borderRadius(radius)
      .objectFit(ImageFit.Cover)
  } else {
    // 无图片 → 文字首字母占位符
    Column() {
      Text(feedTitle.length > 0 ?
        feedTitle.charAt(0).toUpperCase() : '?')
        .fontSize(size * 0.45)
        .fontWeight(FontWeight.Bold)
        .fontColor(Color.White)
    }
    .width(size)
    .height(size)
    .borderRadius(radius)
    .backgroundColor('#BDBDBD')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

// 使用：
this.coverImage(this.currentCoverUrl, this.currentFeedTitle, 40, 6)
```

### 大尺寸封面（FullPlayer）

```typescript
if (this.coverUrl.length > 0) {
  Image(this.coverUrl)
    .width(280)
    .height(280)
    .borderRadius(16)
    .objectFit(ImageFit.Cover)
    .shadow({ radius: 16, color: '#33000000', offsetY: 8 })
} else {
  Column() {
    Text(this.feedTitle.charAt(0).toUpperCase())
      .fontSize(80)
      .fontWeight(FontWeight.Bold)
      .fontColor(Color.White)
  }
  .width(280)
  .height(280)
  .borderRadius(16)
  .backgroundColor('#BDBDBD')
  .justifyContent(FlexAlign.Center)
}
```

---

## MiniPlayer 完整代码

底部浮动播放条（来自 AntennaPod Index.ets）：

```typescript
// MiniPlayer — 在 Tab 栏上方，Navigation 外部
if (this.isPlayerVisible && !this.isFullPlayerVisible) {
  Column() {
    // 进度条
    Progress({
      value: this.getProgressPercent(),
      total: 100,
      type: ProgressType.Linear
    })
    .height(2)
    .width('100%')
    .color('#007DFF')
    .backgroundColor('#E0E0E0')

    // 播放信息栏
    Row() {
      // 封面图（含 fallback）
      if (this.currentCoverUrl.length > 0) {
        Image(this.currentCoverUrl)
          .width(40).height(40)
          .borderRadius(6)
          .objectFit(ImageFit.Cover)
          .margin({ right: 10 })
      } else {
        Column() {
          Text(this.currentFeedTitle.length > 0 ?
            this.currentFeedTitle.charAt(0).toUpperCase() : '?')
            .fontSize(18)
            .fontWeight(FontWeight.Bold)
            .fontColor(Color.White)
        }
        .width(40).height(40)
        .borderRadius(6)
        .backgroundColor('#BDBDBD')
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
        .margin({ right: 10 })
      }

      // 标题和副标题
      Column() {
        Text(this.currentEpisodeTitle.length > 0 ?
          this.currentEpisodeTitle : 'No episode playing')
          .fontSize(14)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        if (this.currentFeedTitle.length > 0) {
          Text(this.currentFeedTitle)
            .fontSize(12)
            .fontColor('#99000000')
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
        }
      }
      .layoutWeight(1)
      .alignItems(HorizontalAlign.Start)

      // 播放/暂停按钮
      Column() {
        SymbolGlyph(this.isPlaying ?
          $r('sys.symbol.pause_fill') : $r('sys.symbol.play_fill'))
          .fontSize(20)
          .fontColor(['#333333'])
      }
      .width(36).height(36)
      .borderRadius(18)
      .backgroundColor('#E8E8E8')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .margin({ left: 8 })
      .onClick(() => {
        PlaybackController.getInstance().playPause();
      })
    }
    .padding({ left: 12, right: 16, top: 8, bottom: 8 })
    .width('100%')
  }
  .width('100%')
  .backgroundColor('#FAFAFA')
  .shadow({ radius: 4, color: '#1A000000', offsetY: -2 })
  .onClick(() => {
    this.navPathStack.pushPathByName(RouteName.FULL_PLAYER, new Object());
  })
}
```

### MiniPlayer 关键设计

- **位置**：在 `Navigation` 和 Tab 栏之间
- **条件显示**：`isPlayerVisible && !isFullPlayerVisible`
- **进度条**：`Progress` Linear 类型，高度 2vp
- **点击展开**：推送 FullPlayer NavDestination
- **阴影**：`offsetY: -2` 向上投影，与 Tab 栏分离

---

## SymbolGlyph 完整用法

```typescript
// 基础用法
SymbolGlyph($r('sys.symbol.house'))
  .fontSize(22)
  .fontColor([Color.Black])

// 条件颜色
SymbolGlyph($r('sys.symbol.play_fill'))
  .fontSize(20)
  .fontColor(this.isActive ? ['#007DFF'] : ['#99182431'])

// 在按钮中使用
Button() {
  SymbolGlyph($r('sys.symbol.plus'))
    .fontSize(18)
    .fontColor([Color.White])
}
.width(48).height(48)
.borderRadius(24)
.backgroundColor('#007DFF')

// 在列表项中使用
Row() {
  SymbolGlyph($r('sys.symbol.chevron_right'))
    .fontSize(16)
    .fontColor(['#CCCCCC'])
}
```

---

## 阴影卡片模式

```typescript
Column() {
  // 卡片内容
  Row() {
    Image(coverUrl).width(60).height(60).borderRadius(8)
    Column() {
      Text(title).fontSize(16).fontWeight(FontWeight.Medium)
      Text(subtitle).fontSize(12).fontColor('#99000000')
    }.layoutWeight(1).margin({ left: 12 })
  }
  .padding(16)
}
.width('100%')
.borderRadius(12)
.backgroundColor(Color.White)
.shadow({ radius: 4, color: '#1A000000', offsetY: 2 })
.margin({ left: 16, right: 16, top: 8 })
```

---

## 圆形头像 / 圆形图片

```typescript
Image(avatarUrl)
  .width(48)
  .height(48)
  .borderRadius(24)  // 宽高的一半 = 圆形
  .objectFit(ImageFit.Cover)
```

---

## 分割线

```typescript
// 水平分割线
Divider()
  .height(0.5)
  .color('#E0E0E0')
  .margin({ left: 16, right: 16 })

// 或使用 border
Column() { ... }
  .border({ width: { bottom: 0.5 }, color: '#E0E0E0' })
```
