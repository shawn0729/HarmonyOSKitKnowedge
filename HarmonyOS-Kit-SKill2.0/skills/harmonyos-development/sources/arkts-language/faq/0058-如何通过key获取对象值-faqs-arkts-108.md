# 如何通过key获取对象值

ArkTS中不支持通过索引访问字段，要使用索引的话可以考虑Record<key, value>，参考代码如下：



```typescript
1. class Student {
2.  data: Record<string, string> = { 'name': 'aaa', 'age': 'bbb' };
3. }
4.
5.
6. @Entry
7. @Component
8. struct KeyObject {
9.  build() {
10.  Column() {
11.  Button('click')
12.  .onClick(() => {
13.  let student = new Student();
14.  console.info(`${student.data['name']}`);
15.  })
16.  }
17.  .justifyContent(FlexAlign.Center)
18.  .alignItems(HorizontalAlign.Center)
19.  .width('100%')
20.  .height('100%')
21.  }
22. }

```


[KeyObject.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/KeyObject.ets#L21-L42)
