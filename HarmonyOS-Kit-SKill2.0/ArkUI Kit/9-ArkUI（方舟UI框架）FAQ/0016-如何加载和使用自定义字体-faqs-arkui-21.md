# 如何加载和使用自定义字体

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21

---

1. 字体管理中[@ohos.font (注册自定义字体)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。
2. 设置对应文本的字体家族。可参考以下代码：
  
  
  

```typescript
1. // xxx.ets
2. import { Font } from '@kit.ArkUI';
3.
4. @Entry
5. @Component
6. struct FontExample {
7.  @State message: string = 'Hello World';
8.
9.  aboutToAppear() {
10.  // Register in black font
11.  let font: Font = this.getUIContext().getFont()
12.  font.registerFont({
13.  familyName: 'Condensed_Black', // Registered font name
14.  familySrc: '/font/Sans_Condensed_Black.ttf' // The font folder is at the same level as the pages directory
15.  })
16.
17.  // Register in black oblique font
18.  font.registerFont({
19.  familyName: 'Condensed_Black_Italic', // Registered font name
20.  familySrc: '/font/Sans_Condensed_Black_Italic.ttf' // The font folder is at the same level as the pages directory
21.  })
22.  }
23.
24.  build() {
25.  Column() {
26.  Text(this.message)
27.  .align(Alignment.Center)
28.  .fontSize(50)
29.  .fontFamily('Condensed_Black') // Use black font
30.  Text(this.message)
31.  .align(Alignment.Center)
32.  .fontSize(50)
33.  .fontFamily('Condensed_Black_Italic') // Use black oblique font
34.  Text(this.message)
35.  .align(Alignment.Center)
36.  .fontSize(50)
37.  }
38.  .width('100%')
39.  .margin({ top: 30 })
40.  }
41. }

```
  [LoadingAndUsingCustomFonts.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadingAndUsingCustomFonts.ets#L21-L61)



效果如图所示：



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xguF_tpOSSCNgzsuLxmTlQ/zh-cn_image_0000002194158888.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T063241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CABDD0B448A9D56D9B8C60CE6C5DB7D76BC1207170920C2F860F872D40E17053 "点击放大")
