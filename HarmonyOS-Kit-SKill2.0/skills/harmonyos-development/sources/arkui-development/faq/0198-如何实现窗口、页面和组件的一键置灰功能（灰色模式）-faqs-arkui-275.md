# 如何实现窗口、页面和组件的一键置灰功能（灰色模式）

---

**实现窗口的一键置灰**



可以通过窗口的[setWindowGrayScale()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowgrayscale12)接口实现窗口的一键置灰。



**实现组件/页面一键置灰**



可以通过[grayscale()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#grayscale)方法添加灰度效果，实现页面和组件的一键置灰功能。



grayscale()接收一个number类型的参数，定义灰度转换比例。参数范围0.0-1.0，其中0.0表示无变化，1.0表示完全灰度，中间值呈线性变化。



示例如下：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  @State grayscaleValue: number = 0;
5.
6.  build() {
7.  Column({ space: 20 }) {
8.  Image($r("app.media.app_icon"))
9.  .height(100)
10.  Row({ space: 20 }) {
11.  Button("Set Gray")
12.  .onClick(() => {
13.  this.grayscaleValue = 1; // Set grayscale to 100%
14.  })
15.  Button("Restore")
16.  .onClick(() => {
17.  this.grayscaleValue = 0; // Set grayscale to 0%
18.  })
19.  }
20.  }
21.  .width("100%")
22.  .height("100%")
23.  .backgroundColor('#fcd473')
24.  .padding(10)
25.  .grayscale(this.grayscaleValue)
26.  }
27. }

```


[ImplementUnifiedPageGrayingFunction.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementUnifiedPageGrayingFunction.ets#L21-L47)
