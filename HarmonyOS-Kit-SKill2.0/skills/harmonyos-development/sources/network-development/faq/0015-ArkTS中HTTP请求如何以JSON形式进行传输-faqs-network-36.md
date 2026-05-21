# ArkTS中HTTP请求如何以JSON形式进行传输

HTTP协议消息头中，Content-Type表示媒体类型。



设置参数值为application/json。请求中的数据将以JSON形式传输。参考代码如下：



```typescript
1. import { http } from '@kit.NetworkKit';
2.
3. class Header {
4.  public contentType: string;
5.  constructor(contentType: string) {
6.  this.contentType = contentType;
7.  }
8. }
9. let httpRequest = http.createHttp();
10. let promise = httpRequest.request("EXAMPLE_URL", {
11.  method: http.RequestMethod.GET,
12.  connectTimeout: 60000,
13.  readTimeout: 60000,
14.  header: new Header('application/json')
15. });

```


[RequestJson.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/RequestJson.ets#L21-L35)



**参考链接**



[request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http#request)
