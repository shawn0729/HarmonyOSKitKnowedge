# Text组件如何加载Unicode字符

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-46

---

在Text组件的content参数中使用字符串，并在字符串中转义Unicode编码。示例代码如下：



```typescript
1. @Entry
2. @Component
3. struct TextView {
4.  build() {
5.  Column() {
6.  Text("\u{1F468}\u200D\u{1F469}\u200D\u{1F467}\u200D\u{1F466}")
7.  .width(100)
8.  .height(100)
9.  .fontSize(50)
10.  }
11.  }
12. }

```


[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L36-L47)



字符串转Unicode编码：



```typescript
1. let chineseStr: string = "中文";
2. const encodedStr = Array.from(chineseStr).map(char =>`\\u${char.codePointAt(0)!.toString(16).padStart(4, '0')}`).join("");

```


[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L22-L23)



Unicode编码转字符串：



```typescript
1. let unicodeStr: string = "\\u4e2d\\u6587";
2. const decodedStr = unicodeStr.replace(/\\u([\dA-Fa-f]{4})/g,(_,p1:string) => String.fromCodePoint(parseInt(p1, 16)));

```


[LoadUnicodeCharacters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadUnicodeCharacters.ets#L29-L30)
