# 后台音频播放合理使用

申请音频播放长时任务的应用退到后台后，禁止不写入数据或写入静音数据等恶意行为。



## 约束

系统检测到应用后台行为时，将挂起或清理应用。



## 示例

```typescript
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. // ...
3.
4. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
5. let context = uiContext!.getHostContext()!;
6.
7. async function read() {
8.  const bufferSize: number = await audioRenderer.getBufferSize();
9.  let path = context.filesDir; // Path of the file
10.
11.  const filePath = path + '/voice_call_data.wav'; // Prohibit the file from being played silently
12.  try {
13.  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY); // Open the file
14.  let buf = new ArrayBuffer(bufferSize);
15.  let readSize: number = await fs.read(file.fd, buf); // Read the file content
16.  } catch (error) {
17.  let err = error as BusinessError;
18.  hilog.warn(0x000, 'testTag', `openSync or read failed, code=${err.code}, message=${err.message}`);
19.  }
20. }

```


[Audio.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/Audio.ets#L21-L71)



有关AudioRenderer开发相关接口的使用，详情可以参考[使用AudioRenderer开发音频播放功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback)。
