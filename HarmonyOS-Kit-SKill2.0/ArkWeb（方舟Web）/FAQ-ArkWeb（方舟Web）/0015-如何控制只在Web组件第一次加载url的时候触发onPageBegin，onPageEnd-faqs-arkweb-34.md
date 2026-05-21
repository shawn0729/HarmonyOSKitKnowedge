# 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd

使用onAppear事件控制仅在首次加载URL时触发onPageBegin和onPageEnd，参考代码如下：



```typescript
1. import { webview } from '@kit.ArkWeb';
2.
3. @Entry
4. @Component
5. struct OnlyOnTheFirstTrigger {
6.  controller: webview.WebviewController = new webview.WebviewController();
7.  isFirst: boolean = false;
8.
9.  build() {
10.  Column() {
11.  Web({
12.  src: 'www.example.com', controller: this.controller
13.  })
14.  .onAppear(() => {
15.  this.isFirst = true;
16.  })
17.  .onPageBegin(() => {
18.  if (this.isFirst) {
19.  this.isFirst = false;
20.  console.info('First page loading triggered');
21.  }
22.  })
23.  }
24.  .width('100%')
25.  .height('100%')
26.  }
27. }

```


[OnlyOnTheFirstTrigger.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/OnlyOnTheFirstTrigger.ets#L21-L47)
