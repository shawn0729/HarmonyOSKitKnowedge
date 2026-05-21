# ArkTS是否支持匿名内部类

ArkTS不支持匿名类，建议使用嵌套类实现。



因为使用匿名类创建的对象类型未知，这与ArkTS[不支持structural typing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide#%E4%B8%8D%E6%94%AF%E6%8C%81structural-typing)和对象字面量的类型冲突。限制主要是考虑运行时的性能开销，需要显式声明类。



**参考链接**



[不支持使用类表达式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide#%E4%B8%8D%E6%94%AF%E6%8C%81%E4%BD%BF%E7%94%A8%E7%B1%BB%E8%A1%A8%E8%BE%BE%E5%BC%8F)
