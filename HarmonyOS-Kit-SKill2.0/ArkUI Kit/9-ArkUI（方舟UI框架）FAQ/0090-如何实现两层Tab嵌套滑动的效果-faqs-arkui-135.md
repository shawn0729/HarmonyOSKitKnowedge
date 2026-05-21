# 如何实现两层Tab嵌套滑动的效果

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-135

---

**问题描述**



在一级Tabs组件下嵌套二级Tabs时，如果二级Tabs的第一个页面左滑或最后一个页面右滑不能切换一级Tabs标签，可以采取以下方法解决：



1. 禁用二级Tabs的边界滑动。



2. 在二级Tabs的边界滑动事件中，手动处理一级Tabs的切换逻辑。



**解决措施**



通过将参数exposeInnerGesture设置为true，实现了一级Tabs容器在嵌套二级Tabs的场景下，能够屏蔽二级Tabs内置Swiper的滑动手势，从而触发一级Tabs内置Swiper滑动手势的功能。



开发者自行定义变量来记录内层Tabs的索引值，通过该索引值判断当滑动达到内层Tabs的边界处时，触发回调返回屏蔽使外层Tabs产生滑动手势。



具体示例可参考：[示例2（嵌套场景下拦截内部容器手势）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement#%E7%A4%BA%E4%BE%8B2%E5%B5%8C%E5%A5%97%E5%9C%BA%E6%99%AF%E4%B8%8B%E6%8B%A6%E6%88%AA%E5%86%85%E9%83%A8%E5%AE%B9%E5%99%A8%E6%89%8B%E5%8A%BF)。
