# 如何实现文本竖向排列

---

可以通过设置Text组件宽度width与字号一致的方式实现。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  private message: string = 'This document is suitable for beginners in application development. By building a simple application with page jump/return function, quickly understand the main files of the project directory and familiarize yourself with the application development process.';
5.  build() {
6.  Column() {
7.  Text(this.message)
8.  .fontSize(13)
9.  .width(13)
10.  }
11.  }
12. }

```


[VerticalArrangementOfText.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/VerticalArrangementOfText.ets#L21-L32)
