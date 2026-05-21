# 在多线程并发场景中，如何实现安全访问同一块共享内存

可以使用SharedArrayBuffer对象实现。SharedArrayBuffer对象存储的数据在同时被修改时，必须通过Atomics原子操作确保其同步性，即下一个操作必须在上一个操作完成后才能开始。代码示例：



```javascript
1. // index.ets
2. import { worker } from '@kit.ArkTS';
3. let sab = new SharedArrayBuffer(32);
4. // int32 buffer view for sab
5. let i32a = new Int32Array(sab);
6. i32a[0] = 0;
7. let producer = new worker.ThreadWorker("entry/ets/workers/worker_producer.ets")
8. producer.postMessage(sab);
9. let consumer = new worker.ThreadWorker("entry/ets/workers/worker_consumer.ets")
10. consumer.postMessage(sab);

```


[SecureAccessShared.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/SecureAccessShared.ets#L21-L30)



```javascript
1. // worker_producer.ets
2. import { MessageEvents, worker } from '@kit.ArkTS';
3.
4. const workerPort = worker.workerPort;
5. workerPort.onmessage = (e: MessageEvents): void => {
6.  let sab = e.data as SharedArrayBuffer;
7.  // view sab buffer in int32 array
8.  let i32a = new Int32Array(sab);
9.  console.info("Producer: received sab");
10.  // Wake up consumers every 2 seconds
11.  setInterval(() => {
12.  let length = i32a.length;
13.  for (let i = 1; i < length; i++) {
14.  i32a[i] = Math.random() * length;
15.  }
16.  Atomics.notify(i32a, 0, 1); // 通知 consumer
17.  }, 2000);
18. }

```


[Worker_producer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/Worker_producer.ets#L21-L38)



```javascript
1. // worker_consumer.ets
2. import { MessageEvents, worker } from '@kit.ArkTS';
3.
4. const workerPort = worker.workerPort;
5. workerPort.onmessage = (e: MessageEvents) => {
6.  let sab = e.data as SharedArrayBuffer;
7.  let i32a = new Int32Array(sab);
8.  console.info("Consumer: received sab");
9.  while (true) {
10.  Atomics.wait(i32a, 0, 0); // This place will be blocked until it wakes up
11.  let length = i32a.length;
12.  for (let i = length - 1; i > 0; i--) {
13.  console.info("arraybuffer " + i + " value is " + i32a[i]);
14.  i32a[i] = i;
15.  }
16.  }
17. }

```


[Worker_consumer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/Worker_consumer.ets#L21-L37)
