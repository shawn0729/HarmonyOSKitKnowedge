# 如何获取当前HAP的BundleName

使用bundleManager模块的getBundleInfoForSelf接口获取所有信息。



GET_BUNDLE_INFO_DEFAULT：接口默认参数，返回结果的name字段对应BundleName。



GET_BUNDLE_INFO_WITH_APPLICATION：除基本字段外，还能够获取ApplicationInfo字段，ApplicationInfo的name字段对应BundleName。



下面代码以GET_BUNDLE_INFO_DEFAULT为例：



```typescript
1. import { bundleManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;
5. try {
6.  bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
7.  hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
8.  }).catch((err: BusinessError) => {
9.  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
10.  });
11. } catch (err) {
12.  let message = (err as BusinessError).message;
13.  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
14. }

```


[GetBundleName.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/GetBundleName.ets#L21-L34)
