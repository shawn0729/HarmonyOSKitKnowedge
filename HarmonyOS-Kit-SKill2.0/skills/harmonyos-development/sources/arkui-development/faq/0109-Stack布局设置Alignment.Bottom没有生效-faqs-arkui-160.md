# Stack布局设置Alignment.Bottom没有生效

---

**问题现象**



在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。



![](../../_assets/images/65b8b069922c96ada34f5343.webp)



**解决措施**



由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
