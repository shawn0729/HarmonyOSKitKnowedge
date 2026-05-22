# 后台系统资源合理使用

无长时任务的应用退至后台后，应释放对应资源，避免阻止系统休眠。



## 约束

接口runningLock.create的type参数BACKGROUND类型已废弃，不建议使用。如果确实需要使用，后台运行时必须主动释放锁。



## 示例



### 应用直接持锁

```typescript
1. import { runningLock } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4.
5. // Return to the background to release the lock
6. runningLock.create('running_lock_test', runningLock.RunningLockType.BACKGROUND)
7.  .then((lock: runningLock.RunningLock) => {
8.  try {
9.  lock.unhold();
10.  } catch (error) {
11.  let err = error as BusinessError;
12.  hilog.warn(0x000, 'testTag', `setColorMode failed, code=${err.code}, message=${err.message}`);
13.  }
14.  })
15.  .catch((err: Error) => {
16.  console.error('create running lock failed, err: ' + err);
17.  });

```


[LockByApplication.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/LockByApplication.ets#L21-L37)



有关RunningLock开发相关接口的使用，详情可以参考[RunningLock锁](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-runninglock)。



### 系统帮助应用持锁

使用音频资源时，系统会为应用持锁。如果不释放音频资源，会导致系统持锁不释放。因此，应用在后台应主动释放音频资源。



可参考[合理使用音频资源](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-audio-use)。



```typescript
1. import { UIAbility } from '@kit.AbilityKit';
2. import { audio } from '@kit.AudioKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. // ...
5. export default class EntryAbility extends UIAbility {
6.  // ...
7.
8.  onForeground(): void {
9.  //Apply for the resources required by the system, or reapply for the resources released in onBackground ()
10.  audio.createAudioRenderer(audioRendererOptions,(err: BusinessError) => {});
11.  }
12.
13.  onBackground(): void {
14.  //Release resources when the UI is invisible
15.  audioRenderer.stop((err: BusinessError) => {});
16.  }
17. }

```


[LockBySystem.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/LockBySystem.ets#L22-L65)
