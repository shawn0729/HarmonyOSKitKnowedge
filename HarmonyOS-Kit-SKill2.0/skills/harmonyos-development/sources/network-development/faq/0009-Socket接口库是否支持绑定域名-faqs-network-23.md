# Socket接口库是否支持绑定域名

Socket不支持域名访问，只能使用IP地址。域名需要通过DNS解析为对应的IP地址。



参考代码如下：



```typescript
1. import { connection } from '@kit.NetworkKit'
2. import { BusinessError } from "@kit.BasicServicesKit"
3.
4. connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
5.  console.log(JSON.stringify(error));
6.  console.log(JSON.stringify(data));
7. })

```


[AddressesByName.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/AddressesByName.ets#L21-L27)



**参考链接**



[connection.getAddressesByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetaddressesbyname)
