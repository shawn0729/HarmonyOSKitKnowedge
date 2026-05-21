# 如何获取手机屏幕信息

---

可参考如下代码，获取了屏幕的宽和高，Display实例的所有属性见文档：[@ohos.display (屏幕属性)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display)。



```typescript
1. import { display } from '@kit.ArkUI';
2.
3. @Entry
4. @Component
5. struct Index {
6.  @State message: string = 'Hello World';
7.  private screenWidth: number = 0;
8.  private screenHeight: number = 0;
9.
10.  aboutToAppear() {
11.  try {
12.  this.screenWidth = display.getDefaultDisplaySync().width;
13.  this.screenHeight = display.getDefaultDisplaySync().height;
14.  } catch (e) {
15.  console.error('Fail with code: ' + JSON.stringify(e));
16.  }
17.  }
18.
19.  build() {
20.  Row() {
21.  Column() {
22.  Text('---->width: ' + this.screenWidth)
23.  Text('---->height: ' + this.screenHeight)
24.  }
25.  .width('100%')
26.  }
27.  .height('100%')
28.  }
29. }

```


[GetPhoneScreenInformation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetPhoneScreenInformation.ets#L21-L49)
