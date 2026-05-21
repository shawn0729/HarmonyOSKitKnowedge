# ArkTS是否支持调用js文件中的方法

**问题描述**



ArkTS是否支持调用js文件中的方法，如果支持，能否提供一下ArkTS与js交互的代码样例?



**解决措施**



ets文件调用js文件和正常ts/ets模块一样，import然后调用就行。



```typescript
1. import {jsFunc} from './JsLib';
2. @Entry
3. @Component
4. struct Index {
5.
6.  build() {
7.  Column({ space: 20 }) {
8.  Text("Import Js Demo")
9.  Button("Call Js")
10.  .onClick(() => {
11.  jsFunc(); // Call jsFunc from js file
12.  })
13.  }
14.  .width("100%")
15.  .height("100%")
16.  .padding(10)
17.  }
18. }

```


[ImportJs.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImportJs.ets#L21-L38)



JsLib.js文件中的demo如下：



```javascript
1. export function jsFunc(){
2.  console.info("this is a js function");
3. }

```


[JsLib.js](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/JsLib.js#L20-L22)
