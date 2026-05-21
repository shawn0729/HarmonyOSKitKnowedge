# 如何获知数据存储沙箱路径

关系型数据库：



"/data/app/el2/100/database/(bundleName)/entry/rdb/"下的.db文件



键值型数据库：



"/data/app/el2/100/database/(bundleName)/entry/kvdb/<系统默认生成文件名>/single_ver/main/"路径下的.db文件



首选项：



"data/app/el2/100/base/(bundleName)/haps/entry/preferences"路径下的文件



应用持久化存储路径：



"/data/app/el2/100/base/(bundleName)/haps/<模块名>/files/persistent_storage"



通过[获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)获取kvStore、Rdb路径前缀databaseDir和preferences路径前缀preferencesDir，后面自行拼接。
