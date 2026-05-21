# 自定义组件是否能通过容器保存

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-228

---

自定义组件是 struct 而非 class，因此无法直接存储在容器中。可以通过将自定义组件封装在 Builder 函数中，利用 Builder 的封装来实现存储。



参考代码如下：



```typescript
1. @Component
2. struct ComA {
3.  build() {
4.  Text('ComA').fontSize(50).fontWeight(FontWeight.Bold)
5.  }
6. }
7.
8. @Component
9. struct ComB {
10.  build() {
11.  Text('ComB').fontSize(50).fontWeight(FontWeight.Bold)
12.  }
13. }
14.
15. @Component
16. struct ComC {
17.  build() {
18.  Text('ComC').fontSize(50).fontWeight(FontWeight.Bold)
19.  }
20. }
21.
22. //if else logical branch writing
23. @Builder
24. function buildCom(param: string) {
25.  if (param == 'ComA') {
26.  ComA()
27.  } else if (param == 'ComB') {
28.  ComB()
29.  } else if (param == 'ComC') {
30.  ComC()
31.  }
32. }
33.
34. @Builder
35. function buildComA() {
36.  ComA()
37. }
38.
39. @Builder
40. function buildComB() {
41.  ComB()
42. }
43.
44. @Builder
45. function buildComC() {
46.  ComC()
47. }
48.
49. //Encapsulate in container through map
50. let map: Map<string, WrappedBuilder<[]>> = new Map();
51. map.set('ComA', wrapBuilder(buildComA));
52. map.set('ComB', wrapBuilder(buildComB));
53. map.set('ComC', wrapBuilder(buildComC));
54.
55. @Component
56. struct Page12 {
57.  @State message: string = 'Hello World';
58.  @State arr: string[] = ['ComA', 'ComB', 'ComC'];
59.
60.  build() {
61.  Column() {
62.  ForEach(this.arr, (item: string) => {
63.  //Retrieve based on the key during use
64.  map.get(item)?.builder()
65.  })
66.  }
67.  .justifyContent(FlexAlign.Center)
68.  .width('100%')
69.  .height('100%')
70.  }
71. }

```


[CanCustomComponentsBeSavedInContainers.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CanCustomComponentsBeSavedInContainers.ets#L21-L92)



**参考链接：**



[@BuilderParam装饰器：引用@Builder函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam)
