# ArkTS中this的常用场景及使用

在ArkTS中，this 用于类中访问对象属性和方法，或在自定义组件的回调中使用UIContext.getHostContext(this)。



- 类中使用 this，this 实际指向实例化后的对象。
  
  
  

```typescript
1. class UserInfo {
2.  name: string = 'xxx';
3.
4.  getName() {
5.  return this.name;
6.  }
7. }
8.
9. const user: UserInfo = new UserInfo();

```
  [ThisUsageInArkTS.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ThisUsageInArkTS.ets#L21-L29)

- 在自定义组件中使用 this，通常是在回调事件中，此时 this 指向自定义组件本身。常用的方法是通过UIContext.getHostContext(this)获取上下文。
