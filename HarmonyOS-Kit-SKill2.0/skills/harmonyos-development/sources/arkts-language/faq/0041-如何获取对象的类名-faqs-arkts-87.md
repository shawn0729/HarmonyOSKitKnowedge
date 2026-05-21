# 如何获取对象的类名

获取类的实例，通过constructor的name属性获取类名。



示例如下：



```typescript
1. class TestClass {
2.  a: string = 'A';
3.  b: string = 'B';
4. }
5.
6. let testClassObj: TestClass = new TestClass();
7.
8. @Entry
9. @Component
10. struct Index {
11.  build() {
12.  Row() {
13.  Column() {
14.  Button('get Class Name')
15.  .onClick(() => {
16.  console.log('TestClass Name:', testClassObj.constructor.name);
17.  })
18.  }
19.  .width('100%')
20.  }
21.  .height('100%')
22.  }
23. }

```


[ClassObjName.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ClassObjName.ets#L21-L43)
