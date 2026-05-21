# 如何在Worker中开启多级子线程

在Worker中开启多级子线程，具体可参考如下示例代码：



```typescript
1. import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';
2.
3. const workerInstance = new worker.ThreadWorker('entry/ets/pages/Worker.ets');
4.
5. // The main thread passes information to the worker thread
6. workerInstance.postMessage('123');
7.
8. // The main thread receives worker thread information
9. workerInstance.onmessage = (e: MessageEvents): void => {
10.  // Data: Information sent by the Worker thread
11.  let data: string = e.data;
12.  console.info(`main thread onmessage, data:${data}`);
13.  const workerInstance1 = new worker.ThreadWorker('entry/ets/pages/Work.ets');
14.  workerInstance1.postMessage('123');
15.  workerInstance1.onmessage = (e: MessageEvents): void => {
16.  // data：Information sent by worker threads
17.  let data1: string = e.data;
18.  console.info(`main thread onmessage1, data:${data1}`);
19.  // Destroy Worker object
20.  workerInstance1.terminate();
21.  }
22.  // After calling terminate, execute onexit
23.  workerInstance1.onexit = (code) => {
24.  console.info(`main thread terminate, code:${code}`);
25.  }
26.  // Destroy Worker object
27.  workerInstance.terminate();
28.
29. }
30. // After calling terminate, execute onexit
31. workerInstance.onexit = (code) => {
32.  console.info(`main thread terminate, code:${code}`);
33. }
34.
35. workerInstance.onerror = (err: ErrorEvent) => {
36.  console.error('main error message ' + err.message);
37. }

```


[EnableSubThreadInWorker.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EnableSubThreadInWorker.ets#L21-L57)



```typescript
1. // Work.ets & Worker.ets
2. import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';
3.
4. // Create an object in the worker thread that communicates with the main thread
5. const workerPort = worker.workerPort;
6.
7. // The worker thread receives information from the main thread
8. workerPort.onmessage = (e: MessageEvents): void => {
9.  // Data: Information sent by the main thread
10.  let data: string = e.data;
11.  console.info(`Work.ets onmessage: data ${data}`);
12.
13.  // Worker thread sends information to main thread
14.  workerPort.postMessage('123');
15. }
16.
17. // Callback for worker thread error
18. workerPort.onerror = (err: ErrorEvent) => {
19.  console.info('Worker.ets onerror' + err.message);
20. }

```


[EnableSubThreadInWorker2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EnableSubThreadInWorker2.ets#L21-L40)



```cangjie
1. "buildOption": {
2.  "sourceOption": {
3.  "workers": [
4.  "./src/main/ets/pages/Worker.ets",
5.  "./src/main/ets/pages/Work.ets"
6.  ]
7.  }
8. },

```


[EnableSubThreadInWork.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EnableSubThreadInWork.json5#L9-L16)



**参考链接**



[@ohos.worker (启动一个Worker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker)
