# 如何在TaskPool和Worker获取上下文Context

Worker线程和TaskPool线程中无法直接获取到组件级的Context 。可以通过主线程参数传递应用级Context，通过[getHostContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#gethostcontext12)接口获取Context上下文。



```typescript
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { taskpool } from '@kit.ArkTS';
3.
4. // Support for ordinary functions and passing of reference parameters as input.
5. @Concurrent
6. function printArgs(args: string, uiContext: Context | undefined): string {
7.  hilog.info(0x0000, 'printArgs', `func: ${args}`);
8.  hilog.info(0x0000, 'printArgs',
9.  `Obtain the bundle name of the application: ${uiContext?.applicationInfo.name.toString()}`);
10.  return args;
11. }
12.
13. async function taskpoolExecute(uiContext: Context | undefined): Promise<void> {
14.  try {
15.  let task: taskpool.Task = new taskpool.Task(printArgs, 'create task, then execute', uiContext!);
16.  hilog.info(0x0000, 'taskpoolExecute', 'taskpool.execute(task) result: ' + await taskpool.execute(task));
17.  hilog.info(0x0000, 'taskpoolExecute',
18.  'taskpool.execute(function) result: ' + await taskpool.execute(printArgs, 'execute task by func', uiContext!));
19.  } catch (error) {
20.  hilog.info(0x0000, 'taskpoolExecute', `taskpool: error code: ${error.code}, info: ${error.message}`);
21.  }
22. }
23.
24. @Entry
25. @Component
26. struct TaskPoolGetContext {
27.  @State message: string = 'Hello World';
28.  // Obtain the context.
29.  uiContext = this.getUIContext().getHostContext();
30.
31.  build() {
32.  Column() {
33.  Text(this.message)
34.  .fontSize(50)
35.  .fontWeight(FontWeight.Bold)
36.  .onClick(() => {
37.  taskpoolExecute(this.uiContext);
38.  })
39.  }
40.  .width('100%')
41.  .height('100%')
42.  }
43. }

```


[TaskPoolGetContext.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TaskPoolGetContext.ets#L21-L63)
