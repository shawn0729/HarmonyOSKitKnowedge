# 如何禁用窗口的全屏显示功能

在module.json5文件中配置abilities的supportWindowMode字段，用于指定窗口显示模式。



fullscreen表示支持全屏显示，split表示支持分屏显示，floating表示支持窗口化显示。



参考代码如下：



```json
1. "abilities": [
2.  {
3.  "name": "EntryAbility",
4.  "srcEntry": "./ets/entryability/EntryAbility.ets",
5.  "description": "$string:EntryAbility_desc",
6.  "icon": "$media:icon",
7.  "label": "$string:EntryAbility_label",
8.  "startWindowIcon": "$media:icon",
9.  "startWindowBackground": "$color:start_window_background",
10.  "exported": true,
11.  "supportWindowMode": ["split", "floating"],
12.  "skills": [
13.  {
14.  "entities": [
15.  "entity.system.home"
16.  ],
17.  "actions": [
18.  "ohos.want.action.home"
19.  ]
20.  }
21.  ]
22.  }
23. ],

```


[module_fullscreen.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/module_fullscreen.json5#L20-L42)



**参考链接**



[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities%E6%A0%87%E7%AD%BE)
