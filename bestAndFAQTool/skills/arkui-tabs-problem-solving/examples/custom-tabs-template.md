# 自定义 Tabs 模板

## 触发场景

当用户需要自定义 ArkUI tab bar、自定义页签内容、隐藏默认页签栏、页签对齐或横向滚动时使用。

## 必要组成

- `@State focusIndex` 或 `@State selectedIndex`
- 一个 `TabsController`
- 一个自定义 tab builder
- 自定义页签点击时调用 `controller.changeIndex(index)`
- `Tabs({ controller: this.controller })`
- 替代默认页签栏时使用 `.barHeight(0)`
- 使用 `.onContentWillChange(...)` 同步选中态

## 模板

```typescript
@Entry
@Component
struct CustomTabsExample {
  @State selectedIndex: number = 0;
  private controller: TabsController = new TabsController();

  private tabs: string[] = ['page0', 'page1'];

  @Builder
  tabBuilder(title: string, index: number) {
    Column({ space: 8 }) {
      Text(title)
        .fontSize(18)
      // 如果项目没有页签图标，替换该资源或删除 Image。
      Image($r('app.media.startIcon'))
        .width(20)
        .height(20)
    }
    .width(100)
    .height(60)
    .borderRadius({ topLeft: 10, topRight: 10 })
    .backgroundColor(index === this.selectedIndex ? '#ffffffff' : '#ffb7b7b7')
    .onClick(() => {
      this.controller.changeIndex(index);
      this.selectedIndex = index;
    })
  }

  build() {
    Column() {
      Row({ space: 6 }) {
        Scroll() {
          Row() {
            ForEach(this.tabs, (title: string, index: number) => {
              this.tabBuilder(title, index)
            })
          }
          .justifyContent(FlexAlign.Start)
        }
        .align(Alignment.Start)
        .scrollable(ScrollDirection.Horizontal)
        .scrollBar(BarState.Off)
        .width('80%')
      }
      .width('100%')

      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        ForEach(this.tabs, (title: string, index: number) => {
          TabContent() {
            Text(`${title} content`)
              .height(300)
              .width('100%')
              .fontSize(30)
          }
        })
      }
      .barHeight(0)
      .animationDuration(100)
      .onContentWillChange((currentIndex: number, comingIndex: number) => {
        this.selectedIndex = comingIndex;
        return true;
      })
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .height('100%')
  }
}
```

## 迁移方式

- 如果每个页签需要标题、图标、角标或内容元数据，把 `tabs: string[]` 替换成用户的 tab 数据模型。
- 尽量从同一个数据源生成自定义页签和 `TabContent`。
- 如果用户的自定义页签不需要图标，删除 `Image($r('app.media.startIcon'))`。
- 只有外部自定义 tab bar 完全替代默认页签栏时，才保留 `.barHeight(0)`。
