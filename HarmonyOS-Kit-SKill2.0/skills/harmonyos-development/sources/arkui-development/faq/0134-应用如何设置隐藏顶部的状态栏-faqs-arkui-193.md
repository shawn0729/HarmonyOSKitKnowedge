# 应用如何设置隐藏顶部的状态栏

---

在UIAbility的onWindowStageCreate生命周期中，设置setWindowSystemBarEnable接口。



```cangjie
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2.  windowStage.getMainWindowSync().setWindowSystemBarEnable([])
3.  // ...
4. }

```


[EntryAbilityForHideBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityForHideBar.ets#L21-L37)



**参考链接**



[体验窗口沉浸式能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage#%E4%BD%93%E9%AA%8C%E7%AA%97%E5%8F%A3%E6%B2%89%E6%B5%B8%E5%BC%8F%E8%83%BD%E5%8A%9B)
