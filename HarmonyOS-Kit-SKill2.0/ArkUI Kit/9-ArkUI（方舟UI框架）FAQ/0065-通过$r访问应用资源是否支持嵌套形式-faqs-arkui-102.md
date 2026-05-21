# 通过$r访问应用资源是否支持嵌套形式

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102

---

$r当前不支持嵌套。第二个参数需使用ResourceManager获取应用资源的字符串。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct Page16 {
4.  context = this.getUIContext();
5.
6.  build() {
7.  Row() {
8.  Column() {
9.  Text($r('app.string.EntryAbility1_label2',
10.  this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility_label'))))// path: resources\base\element\string.json
11.  .fontSize(50)
12.  .fontWeight(FontWeight.Bold)
13.  }
14.  .width('100%')
15.  }
16.  .height('100%')
17.  }
18. }

```


[ResourceNesting.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResourceNesting.ets#L21-L38)



**参考链接**



[ResourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#resourcemanager)
