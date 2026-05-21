# 如何监听屏幕旋转

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-66

---

可以使用媒体查询接口监听屏幕旋转。参考代码如下：



```typescript
1. import { mediaquery, UIContext } from '@kit.ArkUI';
2. const context = AppStorage.get("context") as UIContext;
3. let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen for landscape screen events
4. function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
5.  if (mediaQueryResult.matches) {
6.  // do something here
7.  } else {
8.  // do something here
9.  }
10. }
11. listener.on('change', onPortrait) // Register callback
12. listener.off('change', onPortrait) // Unregister callback

```


[ListenForScreenRotation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListenForScreenRotation.ets#L21-L32)



**参考链接**



[@ohos.mediaquery (媒体查询)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery)
