# 如何设置应用自动重启

可以通过ApplicationContext.restartApp实现，具体请参考示例代码：



```typescript
1. import { Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4.
5. @Entry
6. @Component
7. struct Index {
8.  @State message: string = 'Hello World';
9.  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
10.
11.  build() {
12.  RelativeContainer() {
13.  Text(this.message)
14.  .id('HelloWorld')
15.  .fontSize(50)
16.  .fontWeight(FontWeight.Bold)
17.  .alignRules({
18.  center: { anchor: '__container__', align: VerticalAlign.Center },
19.  middle: { anchor: '__container__', align: HorizontalAlign.Center }
20.  })
21.
22.  Button('RESTART').onClick(() => {
23.  let applicationContext = this.context.getApplicationContext();
24.  let want: Want = {
25.  bundleName: 'com.example.myapp',
26.  abilityName: 'EntryAbility'
27.  };
28.  try {
29.  applicationContext.restartApp(want);
30.  hilog.info(0x0000, 'testTag', '%{public}s', 'applicationContext.restartApp');
31.  } catch (error) {
32.  console.error(`restartApp fail, error: ${JSON.stringify(error)}`);
33.  }
34.  })
35.  }
36.  .height('100%')
37.  .width('100%')
38.  }
39. }

```


[SetAppAutomaticallyRestart.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/SetAppAutomaticallyRestart.ets#L21-L59)



**参考链接**



[ApplicationContext.restartApp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextrestartapp12)
