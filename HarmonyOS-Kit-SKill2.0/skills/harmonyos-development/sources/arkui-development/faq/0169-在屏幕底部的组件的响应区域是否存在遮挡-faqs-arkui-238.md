# 在屏幕底部的组件的响应区域是否存在遮挡

---

**问题现象**



创建窗口并加载自定义键盘后，发现底部按钮下半部分无法响应点击事件。



**解决措施**



底部遮挡区域的高度为20像素，可以通过on('avoidAreaChange')事件获取。开发者可以定义一个点击区域来测试点击事件是否能够触发。以下为代码示例：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  build() {
5.  Column() {
6.  Column() {
7.  }
8.  .width('100%')
9.  .height(5) // 5px click range
10.  .backgroundColor(Color.Red)
11.  .onClick(() => {
12.  console.log("Trigger click event")
13.  })
14.  }
15.  .height('100%')
16.  .width('100%')
17.  .justifyContent(FlexAlign.End)
18.  }
19. }

```


[BottomOfScreenObstruction.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BottomOfScreenObstruction.ets#L21-L39)



**参考链接**



[on('avoidAreaChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#onavoidareachange9)
