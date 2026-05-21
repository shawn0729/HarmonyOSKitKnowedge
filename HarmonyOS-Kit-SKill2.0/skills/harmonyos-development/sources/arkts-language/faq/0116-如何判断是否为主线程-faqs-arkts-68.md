# 如何判断是否为主线程

通过Process获取当前的进程号和线程号。如果二者相同，表示当前执行环境为主线程。



**参考代码：**



```typescript
1. import { process } from '@kit.ArkTS'
2.
3. function isMainThread(): boolean {
4.  return process.pid == process.tid;
5. }

```


[IsMainThread.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/IsMainThread.ets#L21-L25)



对于Native侧，通过getpid()方法获取进程ID，通过syscall方式获取线程ID。



**参考代码：**



```cpp
1. #include <unistd.h>
2. #include <thread>
3. #include <sys/syscall.h>
4.
5. bool isMainThread() {
6.  pid_t pid = getpid();
7.  pid_t tid = syscall(SYS_gettid);
8.  if (pid == tid) {
9.  return true;
10.  } else {
11.  return false;
12.  }
13. }

```


[IsMainThread2.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/IsMainThread2.cpp#L21-L33)
