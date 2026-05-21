# 如何选择图文混排的实现方案

---

1. 轻量级Span和ImageSpan图文混排：可通过[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件中嵌套[ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)子组件和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)子组件的方式，实现图文混排。具体实现可参考ImageSpan中的[示例1（设置对齐方式）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#%E7%A4%BA%E4%BE%8B1%E8%AE%BE%E7%BD%AE%E5%AF%B9%E9%BD%90%E6%96%B9%E5%BC%8F)。
2. 富文本[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)支持文本交互式编辑和图文混排，通过[addTextSpan()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan)方法添加文本内容，通过[addImageSpan()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addimagespan)方法添加图片内容。具体实现可参考RichEditor中的[示例1（更新文本样式）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#%E7%A4%BA%E4%BE%8B1%E6%9B%B4%E6%96%B0%E6%96%87%E6%9C%AC%E6%A0%B7%E5%BC%8F)。
