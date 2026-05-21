# 如何读取运动传感器比如加速度传感器

1. 导入sensor（传感器）模块：



```typescript
1. import { sensor } from '@kit.SensorServiceKit';

```


[Accelerometer.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/SensorService/entry/src/main/ets/pages/Accelerometer.ets#L21-L21)



2. 设置加速度传感器的数据回调监听：



```typescript
1. try {
2.  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
3.  console.info('X-coordinate component: ' + data.x);
4.  console.info('Y-coordinate component: ' + data.y);
5.  console.info('Z-coordinate component: ' + data.z);
6.  }, { interval: 10000000 });
7. } catch (err) {
8.  console.error('On fail, errCode: ' + err.code + ' ,msg: ' + err.message);
9. }

```


[Accelerometer.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/SensorService/entry/src/main/ets/pages/Accelerometer.ets#L26-L34)



**参考链接**



[传感器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor)
