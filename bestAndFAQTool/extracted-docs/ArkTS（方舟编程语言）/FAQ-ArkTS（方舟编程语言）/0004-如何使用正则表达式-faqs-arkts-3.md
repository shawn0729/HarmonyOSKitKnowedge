# 如何使用正则表达式

首先使用new RegExp()定义一个正则表达式：



```typescript
1. const reg = new RegExp('ba');

```


[RegExp.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/RegExp.ets#L5-L5)



然后，通过test() 方法检测字符串是否匹配，如果字符串中有匹配的值返回true，否则返回false：



```typescript
1. const res = reg.test('bar');
2. console.info('result', res);

```


[RegExp.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/RegExp.ets#L9-L10)
