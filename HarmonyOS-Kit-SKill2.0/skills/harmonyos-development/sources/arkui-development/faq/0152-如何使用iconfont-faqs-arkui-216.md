# 如何使用iconfont

---

使用iconfont时，开发者需先获取字体库的ttf文件，再通过 `font.registerFont` 接口注册。在 `Text` 上使用对应的 unicode 编码即可。参考代码如下：



```cangjie
1. import { Font } from '@kit.ArkUI'
2. @Entry
3. @Component
4. struct UseIconFont {
5.  // Assuming 0000 is the Unicode for the specified icon, developers actually need to obtain Unicode from the ttf file of the registered iconFont
6.  @State unicode: string = '\u0000';
7.  aboutToAppear(): void {
8.  let font: Font = this.getUIContext().getFont();
9.  font.registerFont({
10.  familyName: 'iconfont',
11.  familySrc: 'xxx.ttf'
12.  })
13.  }
14.  build() {
15.  Row() {
16.  Column() {
17.  Text(this.unicode)
18.  .fontSize(50)
19.  .fontWeight(FontWeight.Bold)
20.  .fontFamily('iconfont')
21.  }
22.  .width('100%')
23.  }
24.  .height('100%')
25.  }
26. }

```


[UsingIconfont.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UsingIconfont.ets#L21-L46)



**参考链接**



[registerFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)
