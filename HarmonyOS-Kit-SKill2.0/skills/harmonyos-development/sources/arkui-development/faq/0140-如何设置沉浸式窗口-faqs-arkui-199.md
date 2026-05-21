# 如何设置沉浸式窗口

---

在EntryAbility的onWindowStageCreate方法中通过windowStage获取window，然后分别调用setWindowLayoutFullScreen和setWindowSystemBarEnable方法。参考代码如下：



```typescript
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4.
5. export default class EntryAbility extends UIAbility {
6.  onWindowStageCreate(windowStage: window.WindowStage) {
7.  // 1.Get the main window of the application.
8.  let windowClass: window.Window | null = null;
9.  windowStage.getMainWindow((err: BusinessError, data) => {
10.  let errCode: number = err.code;
11.  if (errCode) {
12.  console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
13.  return;
14.  }
15.  windowClass = data;
16.  console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
17.
18.  // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
19.  let names: Array<'status' | 'navigation'> = [];
20.  windowClass.setWindowSystemBarEnable(names).then(() => {
21.  console.info('Succeeded in setting the system bar to be visible.');
22.  });
23.  // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
24.  let isLayoutFullScreen = true;
25.  windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
26.  console.info('Succeeded in setting the window layout to full-screen mode.');
27.  });
28.  let sysBarProps: window.SystemBarProperties = {
29.  statusBarColor: '#ff00ff',
30.  navigationBarColor: '#00ff00',
31.  statusBarContentColor: '#ffffff',
32.  navigationBarContentColor: '#ffffff'
33.  };
34.  windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
35.  console.info('Succeeded in setting the system bar properties.');
36.  });
37.  })
38.  // 3.Load the corresponding target page for the immersive window.
39.  windowStage.loadContent("pages/page2", (err: BusinessError) => {
40.  let errCode: number = err.code;
41.  if (errCode) {
42.  console.error('Failed to load the content. Cause:' + JSON.stringify(err));
43.  return;
44.  }
45.  console.info('Succeeded in loading the content.');
46.  });
47.  }
48. };

```


[EntryAbilityImmersiveWindow.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersiveWindow.ets#L21-L68)



**参考链接**



[体验窗口沉浸式能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage#%E4%BD%93%E9%AA%8C%E7%AA%97%E5%8F%A3%E6%B2%89%E6%B5%B8%E5%BC%8F%E8%83%BD%E5%8A%9B)
