# 如何实现匿名内部类

ArkTS不支持匿名类，建议使用嵌套类。匿名类创建的对象类型未知，与ArkTS不支持structural typing和对象字面量的规则冲突。示例如下：



```typescript
1. class A {
2.  foo() {
3.  class B {
4.  v: number = 123;
5.  }
6.  let b = new B();
7.  }
8. }

```


[AnonymousInnerClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AnonymousInnerClass.ets#L21-L28)



或者采用以下写法：



```typescript
1. export interface AnonymousInnerClass<T> {
2.  onSuccess: (t: T) => void;
3.  onFailed: (code: string, reason: string) => void;
4. }
5.
6. let AnonymousInnerClassInstance: AnonymousInnerClass<void> = {
7.  onSuccess: () => {
8.  console.log('success');
9.  },
10.  onFailed: () => {
11.  console.log('failed');
12.  }
13. }

```


[AnonymousInnerClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AnonymousInnerClass.ets#L32-L44)
