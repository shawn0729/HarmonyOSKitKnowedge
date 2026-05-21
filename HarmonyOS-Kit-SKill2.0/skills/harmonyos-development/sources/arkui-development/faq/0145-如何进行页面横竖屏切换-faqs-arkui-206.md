# 如何进行页面横竖屏切换

---

设置方法：setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void。Orientation取值为AUTO_ROTATION，表示传感器自动旋转模式。参考代码如下：



```javascript
1. let orientation = window.Orientation.AUTO_ROTATION;
2. try{
3.  windowClass.setPreferredOrientation(orientation, (err) => {
4.  if(err.code){
5.  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
6.  return;
7.  }
8.  console.info('Succeeded in setting window orientation.');
9.  });
10. }catch (exception) {
11.  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
12. }

```


[EntryAbilityHorizontalAndVertical.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityHorizontalAndVertical.ets#L40-L51)



**参考链接**



[setPreferredOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9)
