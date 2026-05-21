# 如何监听判断VPN类型网络

VPN类型可使用getNetCapabilities方法获取到bearerTypes，当[bearerTypes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netbeartype)的值是4时表示使用了VPN。需要权限：ohos.permission.INTERNET、ohos.permission.GET_NETWORK_INFO。



参考代码如下：



```typescript
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3.
4. @Entry
5. @Component
6. export struct JudeNetType {
7.  getNetType() {
8.  connection.getAllNets((error: BusinessError, allNets: connection.NetHandle[]) => {
9.  if (error) {
10.  console.error(`Failed to get getAllNets. Code: ${error.code}, message: ${error.message}`);
11.  return;
12.  }
13.  for (let netHandle of allNets) {
14.  connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
15.  if (error) {
16.  console.error(`Failed to get capabilities. Code: ${error.code}, message: ${error.message}`);
17.  return;
18.  }
19.  if (data.bearerTypes[0] == connection.NetBearType.BEARER_VPN) {
20.  console.info('The VPN network is connected');
21.  }
22.  })
23.  }
24.  });
25.  }
26.
27.  build() {
28.  Column({ space: 10 }) {
29.  Button('Obtain the type of network connection').onClick(() => {
30.  this.getNetType()
31.  })
32.  }.alignItems(HorizontalAlign.Center)
33.  .height('100%')
34.  .width('100%')
35.  }
36. }

```


[OnNetVpn.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/OnNetVpn.ets#L21-L57)



参考文档：[网络连接管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netbeartype)
