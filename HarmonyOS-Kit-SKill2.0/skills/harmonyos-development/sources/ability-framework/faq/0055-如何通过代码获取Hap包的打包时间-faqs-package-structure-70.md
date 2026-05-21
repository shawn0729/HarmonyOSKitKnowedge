# 如何通过代码获取Hap包的打包时间

通过hvigor构建脚本实现，打包时将时间写入到一个Json文件，保存到rawfile目录下，然后在APP中直接读取这个文件的内容即可。hvigorfile.ts文件内容：



```javascript
1. import { appTasks } from '@ohos/hvigor-ohos-plugin';
2. import { hvigor } from '@ohos/hvigor';
3. import * as fileIo from 'fs';
4. import * as path from 'path';
5.
6. // Callback function after node evaluation
7. hvigor.afterNodeEvaluate((hvigorNode) => {
8.  // Ensure this directory exists
9.  const resourcesDir = path.join(__dirname, 'entry/src/main/resources/rawfile');
10.  if (!fileIo.existsSync(resourcesDir)) {
11.  fileIo.mkdirSync(resourcesDir, { recursive: true });
12.  }
13.
14.  // Write the build time into the JSON file
15.  const now = new Date();
16.  const buildTime = now.getFullYear() + '-'
17.  + String(now.getMonth() + 1).padStart(2, '0') + '-'
18.  + String(now.getDate()).padStart(2, '0') + ' '
19.  + String(now.getHours()).padStart(2, '0') + ':'
20.  + String(now.getMinutes()).padStart(2, '0') + ':'
21.  + String(now.getSeconds()).padStart(2, '0');
22.  const buildInfo = { 'buildTime': buildTime };
23.  fileIo.writeFileSync(
24.  path.join(resourcesDir, 'build_info.json'),
25.  JSON.stringify(buildInfo, null, 2)
26.  );
27. })
28.
29. export default {
30.  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
31.  plugins: [] /* Custom plugin to extend the functionality of Hvigor. */
32. }

```


[hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/hvigorfile.ts#L17-L48)
