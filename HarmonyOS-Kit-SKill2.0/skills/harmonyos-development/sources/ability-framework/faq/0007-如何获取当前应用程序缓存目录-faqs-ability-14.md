# 如何获取当前应用程序缓存目录

使用Context.cacheDir获取应用程序的缓存目录。代码示例如下：



```typescript
1. import { common } from '@kit.AbilityKit';
2.
3. @Entry
4. @Component
5. export struct GetCacheDirectoryView {
6.  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7.  @State cachePath: string = '';
8.
9.  build() {
10.  Column() {
11.  Text(this.cachePath)
12.  .margin({ bottom: 24 })
13.  Button() {
14.  Text('Get the application cache directory address')
15.  }
16.  .onClick(() => {
17.  const applicationContext = this.context.getApplicationContext();
18.  // Get the application file path
19.  const cacheDir = applicationContext.cacheDir;
20.  this.cachePath = cacheDir + '/test.txt';
21.  })
22.  .width(300)
23.  .height(50)
24.  }
25.  .justifyContent(FlexAlign.Center)
26.  .width('100%')
27.  .height('100%')
28.  }
29. }

```


[GetCacheDirectoryView.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetCacheDirectoryView.ets#L21-L49)



**参考链接**



[获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)
