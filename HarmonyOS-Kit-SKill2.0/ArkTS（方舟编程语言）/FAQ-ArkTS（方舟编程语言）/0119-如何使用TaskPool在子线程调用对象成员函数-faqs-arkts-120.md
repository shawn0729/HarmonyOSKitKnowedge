# 如何使用TaskPool在子线程调用对象成员函数

通过将对象Sendable化来使用对象中的方法。具体可参考如下示例代码：



```typescript
1. // TestClass.ets
2. @Sendable
3. export class TestClass {
4.  value: number = 888;
5.
6.  GetValue(): number {
7.  return this.value;
8.  }
9.
10.  Print(): void {
11.  console.info('value:' + this.value);
12.  }
13. }

```


[TestClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestClass.ets#L21-L33)



```typescript
1. // xxx.ets:
2. import { taskpool } from '@kit.ArkTS';
3. import { TestClass } from './TestClass';
4.
5. // Step 1: Define concurrent functions and internally call synchronization methods
6. @Concurrent
7. function func(num: number): number {
8.  // Call synchronous wait call implemented in static class objects
9.  let testClass = new TestClass();
10.  let sum = testClass.GetValue() + num;
11.  return sum;
12. }
13.
14. // Step 2: Create a task and execute it
15. function asyncGet(): void {
16.  // Create a task and pass it in the function func
17.  let task: taskpool.Task = new taskpool.Task(func, 1);
18.  // Execute task and operate on the synchronized logic results
19.  taskpool.execute(task).then((result: object) => {
20.  console.info('testTag result:' + result);
21.  });
22. }
23.
24. @Entry
25. @Component
26. struct Index {
27.  @State message: string = 'Hello World';
28.
29.  build() {
30.  Row() {
31.  Column() {
32.  Text(this.message)
33.  .fontSize(50)
34.  .fontWeight(FontWeight.Bold)
35.  .onClick(() => {
36.  // Step 3: Perform concurrent operations
37.  asyncGet();
38.  })
39.  }
40.  .width('100%')
41.  }
42.  .height('100%')
43.  }
44. }

```


[EnableSubThreadInTaskPool.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EnableSubThreadInTaskPool.ets#L21-L65)
