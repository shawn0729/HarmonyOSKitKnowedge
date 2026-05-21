# 三方库@ohos/axios中发起post请求，如何以queryParams形式传递参数

- 方式一：使用axios.post接口时，Url.URLParams需要转换为字符串并拼接到URL后面。
  
  
  

```typescript
1. let params: url.URLParams = new url.URLParams()
2. params.append('fod' ,'1')
3. params.append('bard','2')
4. axios.post('https://developer.mozilla.org/?' + params.toString()).then((res: AxiosResponse) => {
5.  let message = "request result: " + JSON.stringify(res.data);
6. }).catch((err:AxiosError) => {
7.  let message = "request error: " + err.message;
8. })

```
  [AxiosPost.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/AxiosPost.ets#L23-L30)

- 方式二：使用axios接口，请求参数写在config对象的params中。
  
  
  

```typescript
1. axios({ url: 'https://developer.mozilla.org/?', method: 'post', params: { fod: '1', bard: '2', } }).then((res: AxiosResponse) => {
2.  let message = "request result: " + JSON.stringify(res.data);
3. }).catch((err:AxiosError) => {
4.  let message = "request error: " + err.message;
5. })

```
  [AxiosPost.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/AxiosPost.ets#L35-L39)



**参考链接**



[URLParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url#urlparams9)
