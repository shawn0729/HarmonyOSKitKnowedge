# 如何保持屏幕常亮

---

获取窗口实例对象后，调用setWindowKeepScreenOn方法可设置屏幕是否常亮。



```typescript
1. let isKeepScreenOn: boolean = true;
2. let windowClass: window.Window = window.findWindow("test");
3. try {
4.  windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
5.  const errCode: number = err.code;
6.  if (errCode) {
7.  console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(err));
8.  return;
9.
10.  }
11.  console.info('Succeeded in setting the screen to be always on.');
12.  });
13. } catch (exception) {
14.  console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(exception));
15. }

```


[EntryAbilityKeepScreenOn.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityKeepScreenOn.ets#L39-L53)



**参考链接**



[setWindowKeepScreenOn](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowkeepscreenon9)
