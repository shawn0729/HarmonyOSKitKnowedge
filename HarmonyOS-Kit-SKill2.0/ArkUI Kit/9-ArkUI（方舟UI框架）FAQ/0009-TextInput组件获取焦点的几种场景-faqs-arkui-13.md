# TextInput组件获取焦点的几种场景

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-13

---

- 场景一：TextInput[主动获焦/失焦](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#%E4%B8%BB%E5%8A%A8%E8%8E%B7%E7%84%A6%E5%A4%B1%E7%84%A6)。     调用focusControl.requestFocus接口可以主动让焦点转移至参数指定的组件上。可参考如下代码：


  
  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5.  build() {
6.  Row() {
7.  Column() {
8.  Button('The second focus acquisition')
9.  .onClick(() => {
10.  focusControl.requestFocus('BBB'); // Get focus on the second input box
11.  })
12.
13.
14.  TextInput({ placeholder: 'Please enter the content.' })
15.  .showUnderline(true)
16.  .width(380)
17.  .height(60)
18.  .id('AAA')
19.  TextInput({ placeholder: 'Please enter the content.' })
20.  .showUnderline(true)
21.  .width(380)
22.  .height(60)
23.  .id('BBB')
24.  }
25.  .width('100%')
26.  }
27.  .height('100%')
28.  }
29. }


```
  [GetTheFocusScene_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_One.ets#L21-L49)

- 场景二：页面初次构建完成时，使第二个TextInput获取[默认焦点](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#%E9%BB%98%E8%AE%A4%E7%84%A6%E7%82%B9)。     设置defaultFocus属性，defaultFocus可以使绑定的组件成为页面创建后首次获焦的焦点。可参考如下代码：


  
  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5.  build() {
6.  Row() {
7.  Column() {
8.  TextInput({ placeholder: 'Please enter the content.' })
9.  .showUnderline(true)
10.  .width(380)
11.  .height(60)
12.
13.
14.  TextInput({ placeholder: 'Please enter the content.' })
15.  .showUnderline(true)
16.  .defaultFocus(true) // When the page is first opened, this TextInput gets focus
17.  .width(380)
18.  .height(60)
19.  }
20.  .width('100%')
21.  }
22.  .height('100%')
23.  }
24. }


```
  [GetTheFocusScene_Two.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Two.ets#L21-L44)

- 场景三：页面初次构建完成时，使TextInput获取焦点且不弹出键盘。     设置enableKeyboardOnFocus(false)，在页面进入后不弹出键盘。可参考如下代码：


  
  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5.  build() {
6.  Row() {
7.  Column() {
8.  TextInput({ placeholder: 'Please enter the content.' })
9.  .defaultFocus(true) // When the page is first opened, this TextInput gets focus
10.  .enableKeyboardOnFocus(false) // Is TextInput bound to an input method when focusing through methods other than clicking.
11.  .placeholderColor(Color.Grey)
12.  .placeholderFont({ size: 14, weight: 400 })
13.  .caretColor(Color.Blue)
14.  .width('95%')
15.  .height(40)
16.  .margin(20)
17.  }
18.  .width('100%')
19.  }
20.  .height('100%')
21.  }
22. }


```
  [GetTheFocusScene_Three.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Three.ets#L21-L42)

- 场景四：页面初次构建完成时，使TextInput不获取焦点且不弹出键盘。     TextInput默认不获取焦点，不弹出键盘。可参考如下代码：


  
  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5.  build() {
6.  Column() {
7.  TextInput({ placeholder: 'Please enter the content.' })
8.  }
9.  .width('100%')
10.  }
11. }


```
  [GetTheFocusScene_Four.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetTheFocusScene_Four.ets#L21-L31)
