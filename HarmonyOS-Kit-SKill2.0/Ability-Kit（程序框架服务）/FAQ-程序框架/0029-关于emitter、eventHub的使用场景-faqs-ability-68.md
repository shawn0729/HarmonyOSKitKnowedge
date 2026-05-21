# 关于emitter、eventHub的使用场景

Emitter提供跨线程事件的发送和处理功能，包括事件的持续订阅、单次订阅、取消订阅及事件队列的发送。



1. 订阅事件  

  

```
import { emitter } from '@kit.BasicServicesKit';

const TAG: string = 'ThreadModel';
```
  [EmitterAndEventHub1.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub1.ets#L21-L23)

  

```
// Define an event with an eventId of 1
let event: emitter.InnerEvent = {
 eventId: 1
};

    // Execute the callback after receiving an event with eventId 1
let callback = (eventData: emitter.EventData): void => {
 this.getUIContext().getPromptAction().showToast({
 message: JSON.stringify(eventData)
 });
};

    // Subscribe to events with eventId 1
emitter.on(event,callback);
this.getUIContext().getPromptAction().showToast({
 message: 'subscribe_success'
});
```
  [EmitterAndEventHub2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub2.ets#L27-L43)
  

2. 发送事件  

  

```
import { emitter } from '@kit.BasicServicesKit';
```
  [EmitterAndEventHub.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub.ets#L21-L22)

  

```
// Define an event with an eventId of 1 and a priority of Low
let event: emitter.InnerEvent = {
 eventId: 1,
 priority: emitter.EventPriority.LOW
};

    let eventData: emitter.EventData = {
 data: {
 content: 'c',
 id: 1,
 isEmpty: false
 }
};

    // Send an event with eventId 1 and the event content is eventData
emitter.emit(event,eventData);
```
  [EmitterAndEventHub.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub.ets#L26-L41)
     EventHub提供同线程内事件的发送与处理功能，包括事件订阅、取消订阅及触发。以UIAbility组件与UI的数据同步为例，具体使用方法请参考相关文档。

     **参考链接**

     [UIAbility组件与UI的数据同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-data-sync-with-ui)
