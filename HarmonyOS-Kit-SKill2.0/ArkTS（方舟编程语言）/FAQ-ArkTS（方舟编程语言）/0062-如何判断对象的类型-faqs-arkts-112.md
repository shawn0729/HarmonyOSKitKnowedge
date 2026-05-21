# 如何判断对象的类型

在代码开发中，如果需要对对象的类型做判断，调用不同类的方法，可以使用instanceof进行判断来得知对象的类型，参考代码如下：



```typescript
1. class BaseClass {
2.  value: number = 0;
3.
4.
5.  printf() {
6.  console.info('base value:' + this.value);
7.  }
8.
9.
10.  setValue(val: number) {
11.  this.value = val;
12.  }
13. }
14.
15.
16. class AClass extends BaseClass {
17.  value: number = 1;
18.
19.
20.  setValue(val: number) {
21.  this.value = val;
22.  }
23.
24.
25.  getValue(): number {
26.  return this.value;
27.  }
28. }
29.
30.
31. class BClass extends BaseClass {
32.  value: number = 2;
33.
34.
35.  setValue(val: number) {
36.  this.value = val;
37.  }
38. }
39.
40.
41. function printValue(base: BaseClass) {
42.  base.printf();
43.  let flag = base instanceof AClass;
44.  console.info('printValue flag:' + flag);
45.  if (flag) {
46.  let val = (base as AClass).getValue();
47.  console.info('printValue val:' + val);
48.  }
49. }
50.
51.
52. @Entry
53. @Component
54. struct DetermineObjectType {
55.  aboutToAppear(): void {
56.  printValue(new AClass());
57.  printValue(new BClass());
58.  }
59.
60.
61.  build() {
62.  }
63. }

```


[DetermineObjectType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DetermineObjectType.ets#L21-L83)
