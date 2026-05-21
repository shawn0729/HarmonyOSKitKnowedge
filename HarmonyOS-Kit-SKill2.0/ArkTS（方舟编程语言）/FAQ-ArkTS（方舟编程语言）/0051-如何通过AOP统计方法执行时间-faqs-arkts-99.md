# 如何通过AOP统计方法执行时间

为了统计执行时间，可以使用addBefore记录开始时间，使用addAfter记录结束时间。



示例如下：



```typescript
1. import { util } from '@kit.ArkTS';
2. import { systemDateTime } from '@kit.BasicServicesKit';
3.
4. class Utils {
5.  Add(len: number): number {
6.  let num = 0;
7.  for (let index = 1; index <= len; index++) {
8.  num += index;
9.  }
10.  return num;
11.  }
12. }
13.
14. let startTime = 0; // Initialization start time
15. let endTime = 0; // Initialization end time
16.
17. util.Aspect.addBefore(Utils, 'Add', false, () => {
18.  startTime = systemDateTime.getTime(true); // Return the start time in nanoseconds
19. })
20.
21. util.Aspect.addAfter(Utils, 'Add', false, () => {
22.  endTime = systemDateTime.getTime(true); // Return the end time in nanoseconds
23. })
24.
25. let utilsObj = new Utils();
26. utilsObj.Add(1000);
27.
28. @Entry
29. @Component
30. struct Index {
31.  build() {
32.  Row() {
33.  Column() {
34.  Button('get execution time')
35.  .onClick(() => {
36.  console.log('startTime:', startTime);
37.  console.log('endTime:', endTime);
38.  console.log('endTime - startTime = ', endTime - startTime);
39.  })
40.  }
41.  .width('100%')
42.  }.height('100%')
43.  }
44. }

```


[AopUtils.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AopUtils.ets#L21-L64)
