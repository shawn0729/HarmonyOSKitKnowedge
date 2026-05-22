# Tabs 对齐模式

## 触发场景

当用户要求自定义页签对齐、左对齐页签、可滚动页签或自定义 tab bar 布局时使用。

## 模式

使用外部布局承载自定义 tab bar：

```text
Column
  Row / Scroll / Row -> custom tab bar
  Tabs              -> content area
```

左对齐和横向可滚动页签可使用：

```typescript
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
```

## 迁移方式

- 使用 `FlexAlign.Start` 实现左对齐。
- 页签可能超出可用宽度时，使用 `ScrollDirection.Horizontal`。
- 自定义 tab bar 布局应独立于 `TabContent` 内容布局。
- 如果自定义 tab bar 替代默认 `Tabs` 栏，在 `Tabs` 上设置 `.barHeight(0)`。

## 质量门禁

- tab bar 有稳定的宽度约束。
- 页签较多时可以横向滚动。
- 对齐由外部 tab bar 布局控制，不依赖无关的内容样式。
- 自定义页签点击仍然调用 `controller.changeIndex(index)`。
