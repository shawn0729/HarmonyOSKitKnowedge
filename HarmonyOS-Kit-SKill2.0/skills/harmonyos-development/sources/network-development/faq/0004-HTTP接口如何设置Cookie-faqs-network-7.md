# HTTP接口如何设置Cookie

HttpRequestOptions中的header是一个Object类型，可以直接在header里设置cookie。调用httpRequest.request()需要申请权限：ohos.permission.INTERNET。使用时，httpRequest.request()接口中的“EXAMPLE_URL”需要替换成实际请求地址。参考代码如下：



```typescript
1. import { http } from '@kit.NetworkKit';
2.
3. @Entry
4. @Component
5. struct HttpRequest {
6.  @State message: string = '发起请求';
7.
8.  request() {
9.  let httpRequest = http.createHttp();
10.  let options: http.HttpRequestOptions = {
11.  method: http.RequestMethod.POST,
12.  extraData: 'data to send',
13.  expectDataType: http.HttpDataType.STRING,
14.  priority: 1,
15.  header: {
16.  'cookie': 'key1=value1;key2=value2'
17.  }
18.  };
19.  httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
20.  if (!err) {
21.  console.info('Result:' + data.result);
22.  console.info('code:' + data.responseCode);
23.  console.info('type:' + JSON.stringify(data.resultType));
24.  console.info('header:' + JSON.stringify(data.header));
25.  console.info('cookies:' + data.cookies); // Starting from API version 8, cookies are supported
26.  } else {
27.  console.info('error:' + JSON.stringify(err));
28.  }
29.  });
30.  }
31.
32.  build() {
33.  Row() {
34.  Column() {
35.  Button(this.message)
36.  .fontSize(30)
37.  .fontWeight(FontWeight.Bold)
38.  .onClick(() => {
39.  this.request();
40.  })
41.  }
42.  .width('100%')
43.  }
44.  .height('100%')
45.  }
46. }

```


[SetCookie.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetCookie.ets#L21-L66)



**参考链接**



[@ohos.net.http (数据请求)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http)
