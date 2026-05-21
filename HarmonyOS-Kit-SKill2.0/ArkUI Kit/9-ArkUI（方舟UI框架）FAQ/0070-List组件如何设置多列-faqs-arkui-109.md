# List组件如何设置多列

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-109

---

以列模式为例(listDirection为Axis.Vertical):lanes用于决定List组件在交叉轴方向上的列数。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct ListLanesExample {
4.  @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'];
5.  @State alignListItem: ListItemAlign = ListItemAlign.Start;
6.
7.  build() {
8.  Column() {
9.  List({ space: 20, initialIndex: 0 }) {
10.  ForEach(this.arr, (item: string) => {
11.  ListItem() {
12.  Text('' + item)
13.  .width('100%')
14.  .height(100)
15.  .fontSize(16)
16.  .textAlign(TextAlign.Center)
17.  .borderRadius(10)
18.  .backgroundColor(0xFFFFFF)
19.  }
20.  .border({ width: 2, color: Color.Green })
21.  }, (item: string) => item)
22.  }
23.  .height(300)
24.  .width('90%')
25.  .border({ width: 3, color: Color.Red })
26.  .lanes({ minLength: 40, maxLength: 40 })
27.  .alignListItem(this.alignListItem)
28.
29.  Button('Click to change alignListItem:' + this.alignListItem).onClick(() => {
30.  if (this.alignListItem == ListItemAlign.Start) {
31.  this.alignListItem = ListItemAlign.Center;
32.  } else if (this.alignListItem == ListItemAlign.Center) {
33.  this.alignListItem = ListItemAlign.End;
34.  } else {
35.  this.alignListItem = ListItemAlign.Start;
36.  }
37.  })
38.  }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
39.  }
40. }

```


[ListSettingMultipleColumns.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListSettingMultipleColumns.ets#L21-L62)
