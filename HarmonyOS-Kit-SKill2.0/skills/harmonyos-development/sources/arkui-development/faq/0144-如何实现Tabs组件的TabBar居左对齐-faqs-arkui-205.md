# 如何实现Tabs组件的TabBar居左对齐

---

系统提供的Tabs组件的TabBar仅支持居中对齐。可以通过自定义方式实现：使用Scroll和Row组件实现一个页签，在onClick事件中通过修改索引值和Tabs组件的索引联动，实现切换效果，同时将Tabs的barHeight置为0。具体实现可参考如下示例代码：



```cangjie
1. // xxx.ets
2. @Entry
3. @Component
4. struct TabsExample {
5.  @State tabArray: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
6.  @State focusIndex: number = 0;
7.  private controller: TabsController = new TabsController();
8.
9.  build() {
10.  Column() {
11.  // Use custom tab components
12.  Scroll() {
13.  Row() {
14.  ForEach(this.tabArray, (item: number, index: number) => {
15.  Row({ space: 20 }) {
16.  Text('tab' + item)
17.  .fontWeight(index === this.focusIndex ? FontWeight.Bold : FontWeight.Normal)
18.  }
19.  .padding({ left: 10, right: 10 })
20.  .onClick(() => {
21.  this.controller.changeIndex(index);
22.  this.focusIndex = index;
23.  })
24.  })
25.  }
26.  }
27.  .align(Alignment.Start)
28.  .scrollable(ScrollDirection.Horizontal)
29.  .scrollBar(BarState.Off)
30.  .width('100%')
31.
32.  //The tabs component hides the tab bar
33.  Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
34.  ForEach(this.tabArray, (item: number, index: number) => {
35.  TabContent() {
36.  Text('I am the page ' + item + " the content")
37.  .fontSize(30)
38.  }
39.  })
40.  }.barHeight(0)
41.  }
42.  .height('100%')
43.  .width('100%')
44.  }
45. }

```


[ImplementTabBarAlignmentToTheLeft.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementTabBarAlignmentToTheLeft.ets#L21-L65)
