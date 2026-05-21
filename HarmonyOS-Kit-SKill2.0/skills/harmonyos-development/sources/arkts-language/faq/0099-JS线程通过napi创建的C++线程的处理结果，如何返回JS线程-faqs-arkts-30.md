# JS线程通过napi创建的C++线程的处理结果，如何返回JS线程

使用napi_create_threadsafe_function在JS线程创建可被任意线程调用的函数，在C++线程调用napi_call_threadsafe_function将结果回调给主线程。



**参考链接**



[使用Node-API接口进行线程安全开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-thread-safety)
