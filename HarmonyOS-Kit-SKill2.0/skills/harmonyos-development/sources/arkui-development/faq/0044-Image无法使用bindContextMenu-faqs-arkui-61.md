# Image无法使用bindContextMenu

---

Image组件默认启用长按拖拽功能，会与bindContextMenu的长按弹出菜单冲突，需显式设置draggable(false)来禁用拖拽。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  @Builder
5.  menuBuilder() {
6.  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7.  Button('Test ContextMenu1')
8.  Divider().strokeWidth(2).margin(5).color(Color.Black)
9.  Button('Test ContextMenu2')
10.  Divider().strokeWidth(2).margin(5).color(Color.Black)
11.  Button('Test ContextMenu3')
12.  }
13.  .width(200)
14.  .height(160)
15.  }
16.
17.  build() {
18.  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
19.  Column() {
20.  Image($r('app.media.icon'))
21.  .draggable(false)
22.  .width('100vp')
23.  }
24.  .bindContextMenu(this.menuBuilder, ResponseType.LongPress)
25.  .onDragStart(() => {
26.  // Close menu when dragging
27.  this.getUIContext().getContextMenuController().close()
28.  })
29.
30.  }
31.  .width('100%')
32.  .height('100%')
33.  }
34. }

```


[ImageCanNotUseBindContextMenu.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageCanNotUseBindContextMenu.ets#L21-L54)



**参考链接**



[菜单控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu)，[Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)
