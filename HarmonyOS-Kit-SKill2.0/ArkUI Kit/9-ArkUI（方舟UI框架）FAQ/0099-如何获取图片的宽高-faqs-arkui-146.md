# 如何获取图片的宽高

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-146

---

通过Image组件的[onComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#oncomplete)事件，图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。参考代码如下：



```csharp
1. Image($r('app.media.startIcon'))
2.  .width(200)
3.  .height(200)
4.  .objectFit(ImageFit.Contain)
5.  .onComplete((event) => {
6.  let imageWidth = event?.width;
7.  let imageHeight = event?.height;
8.  console.info('imageWidth:'+imageWidth,'imageHeight:'+imageHeight);
9.  })

```


[ObtainTheWidthAndHeightOfTheImage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ObtainTheWidthAndHeightOfTheImage.ets#L24-L32)



**参考链接**



[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)
