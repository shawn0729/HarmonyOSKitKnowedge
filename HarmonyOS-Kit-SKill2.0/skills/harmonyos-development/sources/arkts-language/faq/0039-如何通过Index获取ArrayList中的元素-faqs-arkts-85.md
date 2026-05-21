# 如何通过Index获取ArrayList中的元素

- 方式一：     JS语法基础中可以通过数组元素的下标直接访问数组中的对象。示例如下：


  
  
  

```typescript
1. import { ArrayList } from '@kit.ArkTS';
2.
3. let arrayList: ArrayList<number> = new ArrayList();
4. arrayList.add(0);
5. arrayList.add(1);
6. arrayList.add(2);
7. arrayList.add(3);
8. arrayList.add(4);
9. arrayList.add(5);
10. arrayList.add(6);
11. arrayList.add(7);
12. arrayList.add(8);
13. arrayList.add(9);
14.
15. @Entry
16. @Component
17. struct Index {
18.  @State message: string = 'get arrayList value';
19.
20.  build() {
21.  Row() {
22.  Column() {
23.  Button(this.message)
24.  .onClick(() => {
25.  console.info('arrayList[6]:', arrayList[6]);
26.  })
27.  }
28.  .width('100%')
29.  }
30.  .height('100%')
31.  }
32. }


```
  [ArrayList1.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ArrayList1.ets#L21-L52)

- 方式二：     使用[subArrayList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arraylist#subarraylist)，subArrayList可以截取ArrayList中的一段元素，并返回这一段ArrayList实例。示例如下：


  
  
  

```typescript
1. import { ArrayList } from '@kit.ArkTS';
2.
3. let arrayList: ArrayList<number> = new ArrayList();
4. arrayList.add(0);
5. arrayList.add(1);
6. arrayList.add(2);
7. arrayList.add(3);
8. arrayList.add(4);
9. arrayList.add(5);
10. arrayList.add(6);
11. arrayList.add(7);
12. arrayList.add(8);
13. arrayList.add(9);
14.
15. let result: ArrayList<number> = arrayList.subArrayList(2, 4);
16.
17. @Entry
18. @Component
19. struct Index {
20.  @State message: string = 'subArrayList result';
21.
22.  build() {
23.  Row() {
24.  Column() {
25.  Button(this.message)
26.  .onClick(() => {
27.  console.info('subArrayList result:', JSON.stringify(result)); // subArrayList result {"0":"2","1":"3"}
28.  })
29.  }
30.  .width('100%')
31.  }
32.  .height('100%')
33.  }
34. }


```
  [ArrayList2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ArrayList2.ets#L21-L54)
