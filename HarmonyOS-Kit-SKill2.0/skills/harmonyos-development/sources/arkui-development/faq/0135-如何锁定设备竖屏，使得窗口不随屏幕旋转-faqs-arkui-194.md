# 如何锁定设备竖屏，使得窗口不随屏幕旋转

---

使用setPreferredOrientation方法锁定竖屏，设置orientation为window.Orientation.PORTRAIT。参考代码如下：



```typescript
1. //1.Get the window instance object, use the createWindow method to create a new window, and use the findWindow method to obtain an existing window
2. let windowClass: window.Window | undefined = undefined;
3. let config: window.Configuration = {
4.  name: "alertWindow",
5.  windowType: window.WindowType.TYPE_SYSTEM_ALERT,
6.  ctx: this.context
7. };
8. try {
9.  let promise = window.createWindow(config);
10.  promise.then((data)=> {
11.  windowClass = data;
12.  console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
13.  }).catch((err: BusinessError)=>{
14.  console.error('Failed to create the Window. Cause:' + JSON.stringify(err));
15.  });} catch (exception) {
16.  console.error('Failed to create the window. Cause: ' + JSON.stringify(exception));
17. }
18. //2.The window instance uses the setPreferred Orientation method to set the display orientation of the window. PORTRAIT is a fixed vertical screen, and other orientations can refer to the reference link
19. let orientation = window.Orientation.PORTRAIT;
20. try {
21.  let windowClass: window.Window = window.findWindow("test");
22.  windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
23.  const errCode: number = err.code;
24.  if (errCode) {
25.  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
26.  return;
27.  }
28.  console.info('Succeeded in setting window orientation.');
29.  });
30. } catch (exception) {
31.  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
32. }

```


[EntryAbilityLockDevice.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityLockDevice.ets#L39-L70)



**参考链接**



[Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#orientation10)
