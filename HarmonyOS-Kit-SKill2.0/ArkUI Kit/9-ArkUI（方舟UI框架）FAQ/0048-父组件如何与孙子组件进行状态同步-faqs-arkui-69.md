# 父组件如何与孙子组件进行状态同步

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-69

---

- 方式一（推荐）：使用@Provider和@Consumer装饰器。在父组件中使用@Provider，在孙子组件中使用@Consumer，实现双向数据绑定。


1. 在父组件中使用子组件，并通过@Provider提供reviewVote参数，实现跨级传递到孙子组件。  

  
  
  

```typescript
1. @Entry
2. @ComponentV2
3. struct Father{
4.  @Provider("reviewVote") reviewVotes: number = 0;
5.
6.
7.  build() {
8.  Column() {
9.  Son()
10.  Button(`Father: ${this.reviewVotes}`)
11.  }
12.  }
13. }


```
  [ComponentStatusSynchronization_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_One.ets#L21-L33)
  

2. 在子组件中使用孙组件。  

  
  
  

```typescript
1. @ComponentV2
2. struct Son{
3.  build() {
4.  Column() {
5.  Grandson()
6.  }
7.  }
8. }


```
  [ComponentStatusSynchronization_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_One.ets#L37-L44)
  

3. 在孙子组件中使用@Consumer接收reviewVote参数。  

  
  
  

```typescript
1. @ComponentV2
2. struct Grandson{
3.  @Consumer("reviewVote") reviewVotes: number = 0;
4.
5.
6.  build() {
7.  Column() {
8.  Button(`Grandson: ${this.reviewVotes}`)
9.  }.width('100%')
10.  }
11. }


```
  [ComponentStatusSynchronization_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_One.ets#L48-L58)
  



- 使用方式二：在父组件使用 @Local 装饰器，在子组件和孙子组件中使用 @Param 装饰器。


1. 在父组件Father中使用@Local绑定数据reviewVote。  

  
  
  

```typescript
1. @Entry
2. @ComponentV2
3. struct Father {
4.  @Local reviewVotes: number = 0;
5.
6.
7.  build() {
8.  Column() {
9.  Son({ reviewVotes: this.reviewVotes })
10.  Button(`Father: ${this.reviewVotes}`)
11.  }
12.  }
13. }


```
  [ComponentStatusSynchronization_Two.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_Two.ets#L21-L33)
  

2. 子组件Son中使用@Param接收父组件Father传递的参数reviewVote。  

  
  
  

```typescript
1. @ComponentV2
2. struct Son {
3.  @Require @Param reviewVotes: number = 1;
4.
5.
6.  build() {
7.  Column() {
8.  Grandson({ reviewVotes: this.reviewVotes })
9.  }
10.  }
11. }


```
  [ComponentStatusSynchronization_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_Two.ets#L37-L47)
  

3. 孙子组件Grandson 使用@Param接收Son组件传递的参数reviewVote。  

  
  
  

```typescript
1. @ComponentV2
2. struct Grandson {
3.  @Require @Param reviewVotes: number = 1;
4.
5.
6.  build() {
7.  Column() {
8.  Button(`Grandson: ${this.reviewVotes}`)
9.  }.width('100%')
10.  }
11. }


```
  [ComponentStatusSynchronization_Two.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentStatusSynchronization_Two.ets#L51-L61)
