# 如何在调用处实现接口中的方法

示例代码如下：



```typescript
1. // The custom interface is as follows:
2. export interface OnTrustListener {
3.  OnSuccess: (data: string) => void;
4.  OnError: (error: string) => void;
5. }
6.
7. @Component
8. export struct InterfaceUse {
9.  private listener: OnTrustListener = {
10.  OnSuccess: (data: string) => {
11.  console.info('data is:' + data);
12.  },
13.  OnError: (error: string) => {
14.  console.info('error is:' + error);
15.  }
16.  };
17.
18.  build() {
19.  Column() {
20.  Button('click me')
21.  .onClick((event: ClickEvent) => {
22.  this.listener.OnSuccess('success');
23.  })
24.  }
25.  .width('100%')
26.  .height('100%')
27.  }
28. }

```


[CallInterface.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CallInterface.ets#L21-L48)
