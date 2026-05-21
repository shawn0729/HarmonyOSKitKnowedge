# 如何获取对象的所有方法

可以使用Object.getOwnPropertyNames获取所有方法的字符串数组。注意，获取对象的原型prototype需要文件后缀为.ts。参考代码如下：



1. 定义需要获取方法的类文件testClass.ts；



```csharp
1. export class TestClass {
2.  public test(): string {
3.  return 'ArkUI Web Component';
4.  }
5.
6.  public toString(): void {
7.  console.info('Web Component toString');
8.  }
9.
10.  public funToString(): void {
11.  console.info('Web Component toString');
12.  }
13. }

```


[TestClass.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TestClass.ts#L21-L34)



2. 获取文件中的方法；



```typescript
1. import { TestClass } from '../utils/TestClass';
2.
3. let protoType = testClass.prototype;
4. let methodsName: string[] = Object.getOwnPropertyNames(protoType);
5. console.info(methodsName.toString());
6.
7. @Entry
8. @Component
9. struct GetObjectAllFun {
10.  @State message: string = 'Hello World';
11.
12.  build() {
13.  Row() {
14.  Column() {
15.  Text(this.message)
16.  .fontSize(50)
17.  .fontWeight(FontWeight.Bold)
18.  }
19.  .width('100%')
20.  }
21.  .height('100%')
22.  }
23. }

```


[GetObjectAllFun.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/GetObjectAllFun.ets#L21-L44)
