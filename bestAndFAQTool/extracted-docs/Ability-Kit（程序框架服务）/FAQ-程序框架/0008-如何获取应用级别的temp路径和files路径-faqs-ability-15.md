# 如何获取应用级别的temp路径和files路径

通过上下文 context 获取。例如：



- temp路径：通过 this.context.getApplicationContext().tempDir 获取。
- 文件路径：可通过 this.context.getApplicationContext().filesDir 获取。


**参考链接**



[获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)
