# 如何获取router.back传递的参数

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-164

---

在 onPageShow 回调方法中使用 Router模块的getParams方法来获取传递过来的参数。参考代码如下：



```cangjie
1. class InfoTmp {
2.  age: number = 0
3. }
4.
5. class RouTmp {
6.  id: object = () => {
7.  }
8.  info: InfoTmp = new InfoTmp()
9. }
10.
11. const context = AppStorage.get("context") as UIContext;
12. const params: RouTmp = context.getRouter().getParams() as RouTmp; // Get the parameter object passed
13. const id: object = params.id // Get the value of the id property
14. const age: number = params.info.age // Get the value of the age property

```


[GetRouterBackParam.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetRouterBackParam.ets#L21-L34)



**参考链接**



[页面跳转](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#%E9%A1%B5%E9%9D%A2%E8%B7%B3%E8%BD%AC)
