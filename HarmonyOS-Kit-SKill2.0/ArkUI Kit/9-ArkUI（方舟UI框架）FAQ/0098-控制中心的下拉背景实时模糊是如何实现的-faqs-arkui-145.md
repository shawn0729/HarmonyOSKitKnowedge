# 控制中心的下拉背景实时模糊是如何实现的

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-145

---

实时模糊，就是通过状态变量实时改变模糊值。实现模糊可以通过组件的通用属性[backdropBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backdropblur)来设置组件的模糊效果。参考代码如下：



```scss
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackGroundBlur {
5.  private imageSize: number = 150;
6.
7.  build() {
8.  Column() {
9.  // backdropBlur Only blur radius and grayscale parameters can be set
10.  Stack() {
11.  Image($r('app.media.startIcon'))
12.  .width(this.imageSize)
13.  .height(this.imageSize)
14.  Column()
15.  .width(this.imageSize)
16.  .height(this.imageSize)
17.  .backdropBlur(20, { grayscale: [30, 50] })
18.  }
19.  }
20.  .width('100%')
21.  .padding({ top: 5 })
22.  }
23. }

```


[ImplementDropdownBackgroundBlurring.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementDropdownBackgroundBlurring.ets#L21-L43)



**参考链接**



[图像效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect)
