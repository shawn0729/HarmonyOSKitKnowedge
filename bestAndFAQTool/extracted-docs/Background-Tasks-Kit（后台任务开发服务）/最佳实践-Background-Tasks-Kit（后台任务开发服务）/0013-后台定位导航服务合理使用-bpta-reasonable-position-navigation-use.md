# 后台定位导航服务合理使用

使用定位导航服务时，申请长时任务的应用需设置正确应用场景。



## 约束

NA



## 示例

应用可以使用被动定位：



方式1：



```typescript
1. import { geoLocationManager } from '@kit.LocationKit';
2.
3. let requestInfo: geoLocationManager.LocationRequest = {
4.  'scenario': geoLocationManager.LocationRequestScenario.NO_POWER,
5.  'timeInterval': 0,
6.  'distanceInterval': 0,
7.  'maxAccuracy': 0
8. };

```


[GpsOne.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/GpsOne.ets#L21-L28)



方式2：



```typescript
1. import { geoLocationManager } from '@kit.LocationKit';
2.
3. let requestInfo: geoLocationManager.LocationRequest = {
4.  'priority': geoLocationManager.LocationRequestPriority.LOW_POWER,
5.  'timeInterval': 0,
6.  'distanceInterval': 0,
7.  'maxAccuracy': 0
8. };

```


[GpsTwo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/GpsTwo.ets#L21-L28)



有关定位服务开发相关接口的使用，详情可以参考[Location Kit（位置服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-kit)。
