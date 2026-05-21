# 如何设置分组列表的圆角和间距

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-28

---

通过[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)中的ListItemGroupStyle设置分组列表的圆角，List的[space](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#%E6%8E%A5%E5%8F%A3)设置间距。可参考如下代码：



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemGroupExample {
5.  private timeTable: TimeTable[] = [
6.  { projects: ['language'] },
7.  { projects: ['mathematics', 'English'] },
8.  { projects: ['physics', 'chemistry', 'biology'] },
9.  { projects: ['the fine arts', 'music', 'sport'] }
10.  ]
11.
12.  build() {
13.  Column() {
14.  List({ space: 20 }) { // Set the spacing of the grouping list
15.  ForEach(this.timeTable, (item: TimeTable) => {
16.  ListItemGroup({ style: ListItemGroupStyle.CARD }) { // Set the rounded corners of the grouping list
17.  ForEach(item.projects, (project: string) => {
18.  ListItem() {
19.  Text(project)
20.  .width("100%")
21.  .height(100)
22.  .fontSize(20)
23.  .textAlign(TextAlign.Center)
24.  .backgroundColor(0xFFFFFF)
25.  }
26.  }, (item: string) => item)
27.  }
28.  })
29.  }
30.  .width('90%')
31.  .sticky(StickyStyle.Header | StickyStyle.Footer)
32.  .scrollBar(BarState.Off)
33.  }
34.  .width('100%')
35.  .height('100%')
36.  .backgroundColor(0xDCDCDC)
37.  .padding({ top: 5, bottom: 5 })
38.  }
39. }
40.
41. interface TimeTable {
42.  projects: string[];
43. }

```


[SetRoundedCornersAndSpacing.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetRoundedCornersAndSpacing.ets#L21-L63)
