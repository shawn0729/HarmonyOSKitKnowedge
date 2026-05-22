# http请求如何以表单形式进行传输

1. 在HTTP协议消息头中，使用Content-Type来表示媒体类型信息，设置该参数值为“application/x-www-form-urlencoded”。
  
  
  

```typescript
1. import { http } from '@kit.NetworkKit';
2.
3. let options: http.HttpRequestOptions = {
4.  method: http.RequestMethod.GET,
5.  extraData: 'send message',
6.  header: { 'Content-Type': 'application/x-www-form-urlencoded' },
7.  readTimeout: 50000,
8.  connectTimeout: 50000
9. }

```
  [SetForm.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetForm.ets#L21-L29)

2. extraData表示发送请求的数据，目前支持string、Object和ArrayBuffer三种类型。
  
  
  

```typescript
1. let httpRequest = http.createHttp();
2. let data = "user=Query&password=Admin123";
3. httpRequest.request(
4.  'https:xxx',
5.  {
6.  method: http.RequestMethod.POST,
7.  // Optional, default is http.RequestMethod.GET//Developers can add header fields according to their own business needs
8.  header: { 'Content-Type': 'application/x-www-form-urlencoded' }, // This field is used to pass content when using POST requests
9.  extraData: data,
10.  connectTimeout: 60000, // Optional, default is 60000ms
11.  readTimeout: 60000, // Optional, default is 60000ms
12.  }, (err, data) => {
13.  if (!err) {
14.  // Data.read is the HTTP response content, which can be parsed according to business needs
15.  console.info('Result:' + JSON.stringify(data.result));
16.  console.info('code:' +
17.  JSON.stringify(data.responseCode)); // Data.reader is an HTTP response header that can be parsed according to business needs
18.  console.info('header:' + JSON.stringify(data.header));
19.  console.info('cookies:' +
20.  JSON.stringify(data.cookies)); // Starting from API8
21.  } else {
22.  console.info('error:' + JSON.stringify(err)); // Unsubscribe from HTTP response header events
23.  httpRequest.off('headersReceive'); // When the request is exhausted, call the destroy method to actively destroy it.
24.  httpRequest.destroy();
25.  }
26. })

```
  [SetForm.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetForm.ets#L33-L58)
