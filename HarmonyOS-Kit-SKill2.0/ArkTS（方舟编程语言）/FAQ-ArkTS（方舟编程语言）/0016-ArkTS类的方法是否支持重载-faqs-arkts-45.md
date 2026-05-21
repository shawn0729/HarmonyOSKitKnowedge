# ArkTS类的方法是否支持重载

ArkTS支持TS中的重载，包括多个重载签名及一个实现签名。函数签名仅在编译期进行类型检查，不保留到运行时。



ArkTS不支持多个函数体的重载。示例如下：



```typescript
1. // declare
2. function test(param: User): number;
3. function test(param: number, flag: boolean): number;
4. // implement
5. function test(param: User | number, flag?: boolean) {
6.  if (typeof param === 'number') {
7.  return param + (flag ? 1 : 0)
8.  } else {
9.  return param.age
10.  }
11. }

```
