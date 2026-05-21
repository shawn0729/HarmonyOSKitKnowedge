# emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息

是的，emitter.off取消订阅某个事件后，所有订阅这个事件的地方都不会再收到这个事件的消息。



参考代码如下：



```
emitter.off(1);
```


[EmitterOff.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/pages/EmitterOff.ets#L22-L22)



**参考链接**



[emitter.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#emitteroff)
