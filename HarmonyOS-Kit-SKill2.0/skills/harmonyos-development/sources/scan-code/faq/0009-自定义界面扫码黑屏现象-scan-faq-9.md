# 自定义界面扫码黑屏现象

**问题现象**



自定义启动相机却显示黑屏现象。



**解决措施**



-      权限校验错误码：201，没有申请相机权限，[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。

-      参考ArkTS API错误码[1000500001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-error-code#section1000500001-%E5%86%85%E9%83%A8%E9%94%99%E8%AF%AF)：如首次未调用customScan.[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api#customscaninit)初始化，直接调用customScan.[start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api#customscanstart-1)启动扫码相机流，请参考自定义界面扫码的[业务流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-customscan#%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B)。
