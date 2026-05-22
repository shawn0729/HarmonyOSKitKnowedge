# 如何在Index.ets中导出默认导出的对象

**问题现象**



```typescript
1. // src/main/ets/api/AppInterfaces.ets
2. import { DemoService } from "../service/DemoService";
3. class AppInterfaces {
4.  demoService?: DemoService;
5. }
6. export default new AppInterfaces() as AppInterfaces;
7. // Index.ets
8. export AppInterfaces from './src/main/ets/api/AppInterfaces';

```



报错提示：Cannot find name 'AppInterfaces'. <ArkTSCheck>



**解决措施**



```typescript
1. import { DemoService } from "../service/DemoService";
2. class AppInterfaces {
3.  demoService?: DemoService;
4. }
5. let test = new AppInterfaces()
6. export default test;

```


[ExportDefaultObjects.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ExportDefaultObjects.ets#L5-L10)
