# 如何判断当前网络能否上网

可以使用@ohos.net.connection的能力，在网络连接状态发生变化时，判断当前网络是否可以访问互联网，并将判断结果存储到AppStorage中。需要判断网络连接状态时，直接从AppStorage获取结果。参考代码如下：



```typescript
1. import { connection } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3.
4.
5. @Entry
6. @Component
7. export struct NetJudge {
8.  public static netConnection: connection.NetConnection | undefined = undefined;
9.  private static JUDGE_NET_TAG: string = 'NetJudge.currNet.isUseful';
10.
11.  init() {
12.  NetJudge.netConnection = connection.createNetConnection();
13.  NetJudge.netConnection.register(() => {
14.  console.info('connection register success');
15.  });
16.
17.  NetJudge.netConnection.on('netAvailable', (data) => {
18.  console.info('NetJudge netAvailable ');
19.  AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
20.  });
21.
22.  NetJudge.netConnection.on('netUnavailable', () => {
23.  console.info('NetJudge netUnavailable ');
24.  AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
25.  });
26.
27.  NetJudge.netConnection.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
28.  AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
29.  });
30.
31.  // Subscribe to network connection information change events. You can only receive this event notification after calling register
32.  NetJudge.netConnection.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
33.  AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
34.  });
35.
36.  NetJudge.netConnection.on('netLost', () => {
37.  AppStorage.setOrCreate(NetJudge.JUDGE_NET_TAG, this.judgeHasNet());
38.  });
39.  }
40.
41.  regist() {
42.  if (NetJudge.netConnection === undefined) {
43.  this.init();
44.  }
45.  }
46.
47.  judgeHasNet(): boolean {
48.  try { // Get current network connection
49.  let netHandle = connection.getDefaultNetSync();
50.
51.  // 0-100 Reserved connections for the system
52.  if (!netHandle || netHandle.netId < 100) {
53.  return false;
54.  }
55.
56.  // Get the properties of the connection
57.  let netCapability = connection.getNetCapabilitiesSync(netHandle);
58.  let cap = netCapability.networkCap;
59.  if (!cap) {
60.  return false;
61.  }
62.
63.  for (let em of cap) {
64.  if (connection.NetCap.NET_CAPABILITY_VALIDATED === em) {
65.  return true;
66.  }
67.  }
68.  } catch (e) {
69.  let err = e as BusinessError;
70.  console.info('get netInfo error ：' + JSON.stringify(err));
71.  }
72.  return false;
73.  }
74.
75.  build() {
76.  Column({ space: 10 }) {
77.  Button('如何判断当前网络能否上网')
78.  .onClick(() => {
79.  this.regist();
80.  })
81.  }
82.  .alignItems(HorizontalAlign.Center)
83.  .height('100%')
84.  .width('100%')
85.  }
86. }

```


[HasNet.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/HasNet.ets#L21-L106)
