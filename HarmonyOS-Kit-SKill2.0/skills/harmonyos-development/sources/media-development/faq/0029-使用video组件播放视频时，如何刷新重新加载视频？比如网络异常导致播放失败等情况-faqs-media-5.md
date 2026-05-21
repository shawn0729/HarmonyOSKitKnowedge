# 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况

先将URL设置为空，再改回原来的值，示例代码如下：



```typescript
1. @Component
2. export struct VideoErrorReload {
3.  @State url: string = 'https://******';
4.
5.  build() {
6.  Column({ space: 20 }) {
7.  Video({ src: this.url })
8.  .height(300)
9.
10.  Button('重新url')
11.  .onClick(() => {
12.  let temp = this.url;
13.  this.url = '';
14.  setTimeout(() => {
15.  this.url = temp;
16.  }, 100);
17.  })
18.  }
19.  }
20. }

```


[VideoErrorReload.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AudioKit/entry/src/main/ets/pages/VideoErrorReload.ets#L6-L25)
