# 如何在ArkTS使用Reflect正确绑定this指针

参考以下示例代码，注意只有对象的get/set方法才能绑定this指针。



```typescript
1. class ReflectClass {
2.  private a = 'a';
3.
4.  get getA() {
5.  return () => {
6.  return this.a;
7.  };
8.  }
9.
10.  set setA(a: string) {
11.  this.a = a;
12.  }
13. }
14.
15. function testInvoke() {
16.  const reflectClass = new ReflectClass();
17.  const fn: Function = Reflect.get(reflectClass, 'getA', reflectClass);
18.  console.info(fn());
19. }
20.
21. @Entry
22. @Component
23. struct ReflectBoundThis {
24.  aboutToAppear(): void {
25.  testInvoke();
26.  }
27.
28.  build() {
29.  }
30. }

```


[ReflectBoundThis.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ReflectBoundThis.ets#L21-L51)
