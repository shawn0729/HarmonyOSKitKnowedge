# 如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题

清空文件时必须要设置OpenMode.TRUNC，默认覆盖模式(WRITE_ONLY)只是覆盖不会清除，TRUNC模式会先清空文件内容。参考代码如下：



```typescript
1. fileIo.openSync(dst, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC | fileIo.OpenMode.CREATE);

```
