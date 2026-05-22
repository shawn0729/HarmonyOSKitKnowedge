# 如何让事件只在一个UIAbility实例中传递

在UIAbility中使用EventHub订阅事件，EventHub模块提供了事件中心，订阅、取消订阅、触发事件的能力。



参考代码如下：



```typescript
1. import { UIAbility } from '@kit.AbilityKit';
2.
3. export default class EntryAbility extends UIAbility {
4.  onForeground() {
5.  this.context.eventHub.on('myEvent', this.eventFunc);
6.  // result：
7.  // eventFunc is called,undefined,undefined
8.  this.context.eventHub.emit('myEvent');
9.  // result：
10.  // eventFunc is called,1,undefined
11.  this.context.eventHub.emit('myEvent', 1);
12.  // result：
13.  // eventFunc is called,1,2
14.  this.context.eventHub.emit('myEvent', 1, 2);
15.  }
16.
17.  eventFunc(argOne: number, argTwo: number) {
18.  console.log(`eventFunc is called, ${argOne}, ${argTwo}`);
19.  }
20. }

```


[EntryAbility2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/entryability/EntryAbility2.ets#L6-L25)



**参考链接**



[使用EventHub进行数据通信](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-data-sync-with-ui#%E4%BD%BF%E7%94%A8eventhub%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E9%80%9A%E4%BF%A1)
