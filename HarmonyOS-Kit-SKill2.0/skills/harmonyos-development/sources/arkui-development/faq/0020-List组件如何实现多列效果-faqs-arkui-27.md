# List组件如何实现多列效果

---

设置[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件的lanes属性，以实现交叉轴上的多列布局。示例代码如下：



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListExample {
5.  @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
6.
7.  build() {
8.  Column() {
9.  List() {
10.  ForEach(this.arr, (item: string) => {
11.  ListItem() {
12.  Row() {
13.  Text(item)
14.  .fontColor(Color.Red)
15.  .fontSize(40)
16.  }
17.  }
18.  .width('100%')
19.  .border({
20.  width: 1,
21.  color: Color.Black,
22.  radius: 5
23.  })
24.  })
25.  }
26.  .lanes(3)
27.  .alignListItem(ListItemAlign.Center)
28.  }
29.  .padding({ top: 30 })
30.  }
31. }

```


[ListImplementsMultiColumnEffect.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListImplementsMultiColumnEffect.ets#L21-L51)



效果如图所示：



![](../../_assets/images/c2b3455b9366e475cd1521f4.webp "点击放大")
