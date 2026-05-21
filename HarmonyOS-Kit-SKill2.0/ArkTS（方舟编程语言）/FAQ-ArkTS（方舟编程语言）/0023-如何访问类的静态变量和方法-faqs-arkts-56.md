# 如何访问类的静态变量和方法

在ArkTS中，静态变量和方法属于类自身，无法通过this访问，因为this指向类的实例。 若要在类中访问静态变量和方法，需要使用类名。



```typescript
1. // Accessing static variables or executing static methods
2. class TestStatic {
3.  static aaa: string = '3333';
4.
5.  static getAAA () {
6.  // console.log(this.aaa) Static variables cannot be accessed through this and can only be used in static methods
7.  return TestStatic.aaa;
8.  }
9. }
10. TestStatic.aaa;

```


[TestStatic.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestStatic.ets#L21-L30)
