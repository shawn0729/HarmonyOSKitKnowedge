# 如何去除Tabs组件两侧的蒙层

---

Tabs组件的fadingEdge属性表示页签超过容器宽度时是否渐隐消失，默认值为true，设置为false时则直接截断显示，不产生任何渐变效果。



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsOpaque {
5.  @State message: string = 'Hello World';
6.  private controller: TabsController = new TabsController();
7.  @State selfFadingFade: boolean = false; // Does the tab gradually disappear when it exceeds the width of the container? The default value is true.
8.
9.
10.  build() {
11.  Column() {
12.  Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
13.  TabContent() {
14.  Column().width('100%').height('100%').backgroundColor(Color.Pink)
15.  }.tabBar('pink')
16.
17.
18.  TabContent() {
19.  Column().width('100%').height('100%').backgroundColor(Color.Yellow)
20.  }.tabBar('yellow')
21.
22.
23.  TabContent() {
24.  Column().width('100%').height('100%').backgroundColor(Color.Blue)
25.  }.tabBar('blue')
26.
27.
28.  TabContent() {
29.  Column().width('100%').height('100%').backgroundColor(Color.Green)
30.  }.tabBar('green')
31.
32.
33.  TabContent() {
34.  Column().width('100%').height('100%').backgroundColor(Color.Green)
35.  }.tabBar('green')
36.
37.
38.  TabContent() {
39.  Column().width('100%').height('100%').backgroundColor(Color.Green)
40.  }.tabBar('green')
41.
42.
43.  TabContent() {
44.  Column().width('100%').height('100%').backgroundColor(Color.Green)
45.  }.tabBar('green')
46.
47.
48.  TabContent() {
49.  Column().width('100%').height('100%').backgroundColor(Color.Green)
50.  }.tabBar('green')
51.  }
52.  .vertical(false)
53.  .scrollable(true)
54.  .barMode(BarMode.Scrollable)
55.  .barHeight(80)
56.  .animationDuration(400)
57.  .onChange((index: number) => {
58.  console.info(index.toString());
59.  })
60.  .fadingEdge(this.selfFadingFade)
61.  .height('30%')
62.  .width('100%')
63.  }
64.  .padding({ top: '24vp', left: '24vp', right: '24vp' })
65.  }
66. }

```


[RemoveTabsComponentMask.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RemoveTabsComponentMask.ets#L21-L86)



**参考链接**



[属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#%E5%B1%9E%E6%80%A7)



[示例5（设置TabBar渐隐）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#%E7%A4%BA%E4%BE%8B5%E8%AE%BE%E7%BD%AEtabbar%E6%B8%90%E9%9A%90)
