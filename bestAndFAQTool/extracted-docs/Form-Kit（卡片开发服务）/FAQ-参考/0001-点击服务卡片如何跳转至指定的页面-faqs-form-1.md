# 点击服务卡片如何跳转至指定的页面

配置卡片事件，指定目标UIAbility进行跳转。



- 如果应用不在后台，可以在目标UIAbility的onWindowStageCreate()中调用loadContent加载指定的页面。
- 如果应用已在后台，可在目标UIAbility的onNewWant()中调用loadContent加载指定页面。


**参考链接**



[启动UIAbility的指定页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction#%E5%90%AF%E5%8A%A8uiability%E7%9A%84%E6%8C%87%E5%AE%9A%E9%A1%B5%E9%9D%A2)
