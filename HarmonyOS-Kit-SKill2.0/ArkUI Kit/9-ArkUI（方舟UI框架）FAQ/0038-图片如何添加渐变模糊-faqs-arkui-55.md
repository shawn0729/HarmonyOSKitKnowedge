# 图片如何添加渐变模糊

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-55

---

组件通用样式属性linearGradientBlur可以为当前组件添加线性渐变模糊效果。以下为参考代码：



```typescript
1. @Entry
2. @Component
3. struct ImageExample1 {
4.  privateResource1: Resource = $r('app.media.icon');
5.  @State imageSrc: Resource = this.privateResource1;
6.
7.  build() {
8.  Column() {
9.  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
10.  Row({ space: 5 }) {
11.  Image(this.imageSrc)
12.  .linearGradientBlur(60, {
13.  fractionStops: [[0, 0], [0, 0.33], [1, 0.66], [1, 1]],
14.  direction: GradientDirection.Bottom
15.  })
16.  }
17.  }
18.  }
19.  }
20. }

```


[ImageAddGradientBlur.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageAddGradientBlur.ets#L21-L40)



**参考链接**



[linearGradientBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#lineargradientblur12)
