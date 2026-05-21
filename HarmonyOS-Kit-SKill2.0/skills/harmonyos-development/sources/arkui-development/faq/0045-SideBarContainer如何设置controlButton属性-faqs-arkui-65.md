# SideBarContainer如何设置controlButton属性

---

SideBarContainer组件提供侧边栏显示和隐藏功能。通过controlButton属性设置侧边栏控制按钮。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct SideBarContainerExample {
4.  normalIcon: Resource = $r("app.media.icon")
5.  selectedIcon: Resource = $r("app.media.icon")
6.  @State arr: number[] = [1, 2, 3]
7.  @State current: number = 1
8.
9.  build() {
10.  SideBarContainer(SideBarContainerType.Embed) {
11.  Column() {
12.  ForEach(this.arr, (item: number, index) => {
13.  Column({ space: 5 }) {
14.  Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
15.  Text("Index0" + item)
16.  .fontSize(25)
17.  .fontColor(this.current === item ? '#0A59F7' : '#999')
18.  .fontFamily('source-sans-pro,cursive,sans-serif')
19.  }
20.  .onClick(() => {
21.  this.current = item
22.  })
23.  })
24.  }.width('100%')
25.  .justifyContent(FlexAlign.SpaceEvenly)
26.  .backgroundColor('#19000000')
27.
28.  Column() {
29.  Text('SideBarContainer content text1').fontSize(25)
30.  Text('SideBarContainer content text2').fontSize(25)
31.  }
32.  .margin({ top: 50, left: 20, right: 30 })
33.  }
34.  .sideBarWidth(150)
35.  .minSideBarWidth(50)
36.  .controlButton({
37.  left: 32,
38.  top: 32,
39.  width: 32,
40.  height: 32,
41.  icons: { shown: $r("app.media.icon"),
42.  hidden: $r("app.media.icon"),
43.  switching: $r("app.media.icon") }
44.  })
45.  .maxSideBarWidth(300)
46.  .onChange((value: boolean) => {
47.  console.info('status:' + value)
48.  })
49.  }
50. }

```


[SideBarContainerSetControlButton.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SideBarContainerSetControlButton.ets#L21-L70)



**参考链接**



[SideBarContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer)
