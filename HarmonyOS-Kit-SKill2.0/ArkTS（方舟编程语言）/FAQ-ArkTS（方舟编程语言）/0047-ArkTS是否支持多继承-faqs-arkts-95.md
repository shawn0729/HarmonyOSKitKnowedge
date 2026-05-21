# ArkTS是否支持多继承

接口支持多继承，类仅支持单继承。示例如下：



```
class TestClassA {
 address: string = '';
}

class TestClassB {
 name: string = '';
}

// report errors：Classes can only extend a single class.
// class TestClassC extends TestClassA, TestClassB {
// }

interface AreaSize {
 calculateAreaSize(): number;
}

interface Cal {
 Sub(a: number, b: number): number;
}

interface Area extends AreaSize, Cal {
 areaName: string;
 length: number;
 width: number;
}
```


[AreaSize.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AreaSize.ets#L21-L45)
