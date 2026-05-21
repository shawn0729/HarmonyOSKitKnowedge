# 不同类型的Context获取fileDir目录的结果不一致

**问题描述**



不同类型的Context获取fileDir目录的结果存在差异。



1. 使用Application的Context获取的目录是“/data/storage/el2/base/files”。



2. 使用Ability的Context获取的目录是“/data/storage/el2/base/haps/entry/files”。



**问题澄清**



当前设计如下：Application可能包含多个Ability，每个Ability对应沙箱目录下的一个hap路径。



**参考链接**



[应用沙箱目录与应用沙箱路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#%E5%BA%94%E7%94%A8%E6%B2%99%E7%AE%B1%E7%9B%AE%E5%BD%95%E4%B8%8E%E5%BA%94%E7%94%A8%E6%B2%99%E7%AE%B1%E8%B7%AF%E5%BE%84)
