# Stage模型与FA模型在进程内对象共享方面有哪些差异

- Stage模型中，多个应用组件共享同一个ArkTS引擎实例。应用组件之间可以方便地共享对象和状态，从而减少了复杂应用运行对内存的占用。
- FA模型中，每个应用组件独享一个ArkTS引擎实例。


Stage模型是主推的应用模型，开发者可以更方便地开发分布式场景下的复杂应用。



**参考链接**



[通过对比认识FA模型与Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-models#%E9%80%9A%E8%BF%87%E5%AF%B9%E6%AF%94%E8%AE%A4%E8%AF%86fa%E6%A8%A1%E5%9E%8B%E4%B8%8Estage%E6%A8%A1%E5%9E%8B)
