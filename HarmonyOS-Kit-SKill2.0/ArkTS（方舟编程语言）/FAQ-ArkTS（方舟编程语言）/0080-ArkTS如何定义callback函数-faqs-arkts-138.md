# ArkTS如何定义callback函数

定义一个callback函数的样例，参考代码如下：



1. 定义回调函数  

  
  
  

```typescript
1. // Define 2 parameters on the page, return empty callback function
2. myCallback: (a: number,b: string) => void = () => {}


```
  [DefineCallback.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DefineCallback.ets#L23-L24)
  

2. 在使用时进行初始化赋值  

  
  
  

```typescript
1. aboutToAppear() {
2.  // Initialization of callback function
3.  this.myCallback = (a,b) => {
4.  console.info(`handle myCallback a=${a},b=${b}`)
5.  }
6. }


```
  [DefineCallback.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DefineCallback.ets#L27-L32)
