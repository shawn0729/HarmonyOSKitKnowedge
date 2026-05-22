# 如何获取当前应用对应的UIAbility名称

可以通过[bundleManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager)的getBundleInfoForSelf()接口获取当前应用的[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo)信息，其中参数bundleFlags需要包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY。AbilityInfo中包含当前应用的Ability名称、Bundle名称等信息。
