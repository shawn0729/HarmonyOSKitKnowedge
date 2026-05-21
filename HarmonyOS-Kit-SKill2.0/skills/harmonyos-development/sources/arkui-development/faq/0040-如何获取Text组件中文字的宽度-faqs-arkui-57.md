# 如何获取Text组件中文字的宽度

---

使用@ohos.measure中的measureText()方法计算指定文本单行布局下的宽度。具体可参考如下代码：



```typescript
1. @Entry
2. @Component
3. struct IndexTest {
4.  @State textWidth: number = this.getUIContext().getMeasureUtils().measureText({
5.  textContent: "Hello World",
6.  fontSize: '50px'
7.  })
8.
9.  build() {
10.  Row() {
11.  Column() {
12.  Text(`The width of 'Hello World': ${this.textWidth}`)
13.  }
14.  .width('100%')
15.  }
16.  .height('100%')
17.  }
18. }

```


[GetTextWidth.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTextWidth.ets#L21-L38)



**参考链接**



[@ohos.measure (文本计算)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-measure)
