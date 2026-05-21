# ValuesBucket是否有可动态添加字段的方式

**解决措施**



ValuesBucket的实现如下：



```typescript
1. export type ValuesBucket = Record<string, ValueType | Uint8Array | null>;

```


[ValuesBucket.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalDatabaseManagement/entry/src/main/ets/pages/ValuesBucket.ets#L22-L22)



若要动态添加字段，可以参考以下方法。



```typescript
1. function set(): void {
2.
3.  let value : ValuesBucket={};
4.  let name : string ='NAME';
5.  value[name]= 'cxx';
6.  value['AGE']=18;
7.  value['SALARY']=20000;
8. }

```


[ValuesBucket.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalDatabaseManagement/entry/src/main/ets/pages/ValuesBucket.ets#L26-L33)
