# Stack布局设置Alignment.Bottom没有生效

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160

---

**问题现象**



在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/qMUALhWoTZqL9QL5auu_VQ/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T064452Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEC2F752E7C768E850CD04F3738D8B7C13338DAA643A5A4EC4C805DA53CF915F)



**解决措施**



由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
