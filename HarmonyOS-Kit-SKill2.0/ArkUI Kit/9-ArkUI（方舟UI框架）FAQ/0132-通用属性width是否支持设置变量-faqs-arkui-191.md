# 通用属性width是否支持设置变量

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191

---

通用属性width支持设置变量。



```scss
1. @Entry
2. @Component
3. struct Page1 {
4.  @State message: string = 'Hello';
5.  @State widthNum: number = 300;
6.
7.  build() {
8.  Row() {
9.  Column() {
10.  Text(this.message)
11.  .fontSize(50)
12.  .fontWeight(FontWeight.Bold)
13.  .width(this.widthNum)
14.  .backgroundColor(Color.Blue)
15.  }
16.  .width('100%')
17.  }
18.  .height('100%')
19.  }
20. }

```


[DoesWidthSupportSettingVariables.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DoesWidthSupportSettingVariables.ets#L21-L40)



效果如下所示：



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/cGH94RmlRKWkVGAFYk2AHg/zh-cn_image_0000002194158632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T064747Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AB1952402064C5B9863A0AB7D563495148DE98CEE4A395009FE0C15901667EC "点击放大")
