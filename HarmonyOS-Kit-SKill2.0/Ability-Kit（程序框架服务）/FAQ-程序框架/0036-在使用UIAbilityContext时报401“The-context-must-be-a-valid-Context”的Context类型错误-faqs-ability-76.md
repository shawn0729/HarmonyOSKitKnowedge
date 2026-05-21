# 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误

401错误表示提供的上下文类型不正确，需要使用UIAbility的上下文。获取[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)的方式如下：



```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
 onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
 let uiAbilityContext = this.context;
 // ...
 }
}
```


[GetUIAbilityContext.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetUIAbilityContext.ets#L21-L28)



**参考链接**



[应用上下文Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage)
