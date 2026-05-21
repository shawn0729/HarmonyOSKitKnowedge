# 是否支持模块的动态加载？如何实现

当前不支持动态加载设备侧的二进制包。可以使用动态import进行异步加载，以实现类似Class.forName()的反射效果。



示例如下，hap动态导入harlibrary，并调用静态成员函数staticAdd()、实例成员函数instanceAdd()和全局方法addHarlibrary()。



```typescript
1. // harlibrary's src/main/ets/utils/Calc.ets
2. export class Calc {
3.  public static staticAdd(a:number, b:number):number {
4.  let c = a + b;
5.  console.log('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
6.  return c;
7.  }
8.  public instanceAdd(a:number, b:number):number {
9.  let c = a + b;
10.  console.log('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
11.  return c;
12.  }
13. }
14. export function addHarlibrary(a:number, b:number):number {
15.  let c = a + b;
16.  console.log('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
17.  return c;
18. }

```


[Calc.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/harlibrary/src/main/ets/utils/Calc.ets#L22-L39)



```typescript
1. // harlibrary's Index.ets
2. export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'

```


[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/harlibrary/Index.ets#L22-L23)
