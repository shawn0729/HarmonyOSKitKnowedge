# ArkTS中Worker线程、TaskPool线程如何与宿主线程通信

Worker通过PostMessage向父线程发送任务。TaskPool通过sendData向父线程发送消息，触发任务。



PostMessage接口示例如下：



```typescript
1. import { worker } from '@kit.ArkTS';
2.
3. const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
4. let buffer = new ArrayBuffer(8);
5. workerInstance.postMessage(buffer, [buffer]);

```


[CommunicateHostThread.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CommunicateHostThread.ets#L21-L25)



sendData接口示例如下：



```typescript
1. import { taskpool } from '@kit.ArkTS';
2.
3. @Concurrent
4. function ConcurrentFunc(num: number): number {
5.  let res: number = num * 10;
6.  taskpool.Task.sendData(res);
7.  return num;
8. }

```


[CommunicateHostThread2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CommunicateHostThread2.ets#L21-L28)



**参考链接**



[postMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker#postmessage9)，[sendData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#senddata11)
