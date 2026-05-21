# 默认界面扫码取消后，如何感知

**问题现象**



调用默认界面扫码功能，没有扫码直接关闭，如何在逻辑中判断？



**解决措施**



开启扫码，却没有进行任何扫码操作而直接取消扫码，可以从回调中获取返回错误码：[1000500002](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-error-code#section1000500002-%E7%94%A8%E6%88%B7%E5%8F%96%E6%B6%88%E6%89%AB%E7%A0%81)，用户取消扫码，据此自行修改逻辑操作。
