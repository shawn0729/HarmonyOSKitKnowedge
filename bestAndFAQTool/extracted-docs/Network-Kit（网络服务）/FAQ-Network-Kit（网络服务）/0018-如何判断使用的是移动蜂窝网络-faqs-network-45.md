# 如何判断使用的是移动蜂窝网络

使用@kit.NetworkKit中的connection.getNetCapabilities接口获取网络能力信息。如果返回结果中bearerTypes的值为 0，表示移动蜂窝网络，否则表示其他网络。需要权限：ohos.permission.GET_NETWORK_INFO。



参考代码如下：



```typescript
1. import { connection } from '@kit.NetworkKit';
2.
3. // Check if the network is connected
4. connection.hasDefaultNet((error, data) => {
5.  console.log('data: ' + data);
6. })
7. // Obtain network capability information
8. connection.getDefaultNet().then((netHandle) => {
9.  connection.getNetCapabilities(netHandle, (error, data) => {
10.  console.log(JSON.stringify(error));
11.  console.log(JSON.stringify(data));
12.  })
13. })

```


[SetNetType.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetNetType.ets#L21-L33)



**参考链接**



[connection.getNetCapabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities)



[NetBearType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netbeartype)
