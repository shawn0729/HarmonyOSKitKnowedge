# 如何判断蜂窝信号强度

可以通过radio.getSignalInformation()接口获取蜂窝信号强度，具体步骤如下：



1. 导入相应的模块。
2. 调用getSignalInformation()方法，返回SignalInformation列表。
3. 遍历SignalInformation数组，根据不同的signalType获取相应制式的信号强度。
4. （可选）订阅蜂窝网络信号变化。


参考代码如下：



```typescript
1. import { radio, observer } from '@kit.TelephonyKit';
2.
3. // Taking obtaining the signal strength of card 1 as an example
4. let slotId: number = 0;
5. radio.getSignalInformation(slotId, (err, data) => {
6.  if (!err) {
7.  console.log("get signal information success.");
8.  // Traverse the array and output the signal strength under different network standards
9.  for (let j = 0; j < data.length; j++) {
10.  console.log("type:" + data[j].signalType + ", level:" + data[j].signalLevel);
11.  }
12.  } else {
13.  console.error("get signal information fail, err is:" + JSON.stringify(err));
14.  }
15. });
16.
17. // Subscription to cellular network signal changes (optional)
18. observer.on("signalInfoChange", (data) => {
19.  console.log("signal info change, data is:" + JSON.stringify(data));
20. });

```


[GetSignal.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/TelephonyKit/entry/src/main/ets/pages/GetSignal.ets#L21-L41)



**参考链接**



[getSignalInformation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-radio#radiogetsignalinformation7)
