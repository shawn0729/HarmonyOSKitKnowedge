# Tabs 切换诊断

## 触发场景

当用户描述以下问题时使用：

- 点击自定义页签后内容不切换。
- Tabs 内容切换了，但外部 tab 样式没有同步。
- 滑动 Tabs 后选中态错误。
- `TabsController` 似乎不生效。

## 检查顺序

1. 确认 `TabsController` 是稳定的组件字段，不是在 `build()` 中创建的局部变量。
2. 确认自定义页签点击时调用 `this.controller.changeIndex(index)`。
3. 确认同一次点击也会更新用于自定义页签样式的选中下标。
4. 确认 `Tabs` 接收同一个 controller：`Tabs({ controller: this.controller })`。
5. 确认 `onContentWillChange` 更新选中下标并返回 `true`。
6. 确认自定义页签和 `TabContent` 按相同顺序生成。
7. 如果不应显示默认页签栏，确认使用了 `.barHeight(0)`。

## 常见错误形态

```typescript
.onClick(() => {
  this.selectedIndex = index;
})
```

问题：这只改变了自定义页签样式，不会切换 `Tabs` 内容。

## 修复形态

```typescript
.onClick(() => {
  this.controller.changeIndex(index);
  this.selectedIndex = index;
})
```

同时要保持内容切换反向同步选中态：

```typescript
.onContentWillChange((currentIndex: number, comingIndex: number) => {
  this.selectedIndex = comingIndex;
  return true;
})
```

## 禁止做法

- 不要在 `build()` 中创建新的 `TabsController`。
- 不要为 tab 样式和内容下标维护两套互相独立的选中状态。
- 除非存在替代默认栏的自定义 tab bar，否则不要隐藏默认栏。
