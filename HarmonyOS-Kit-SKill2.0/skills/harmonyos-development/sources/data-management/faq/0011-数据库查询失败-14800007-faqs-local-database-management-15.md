# 数据库查询失败 14800007

**问题现象**



使用rdbStore.querySql可以获取 20 条结果，但在调用resultSet.isColumnNull时出现报错，报错信息如下：



[nodict]::[PrepareStep()-sqlite_shared_result_set.cpp:42]: StoreSession BeginStepQuery fail : not select sql !



[nodict]::[GetColumnIndex()-abs_result_set.cpp:334]: Failed to GetAllColumnNames, ret is 14800007



[nodict]::[GetColumnIndex()-napi_result_set.cpp:474]: IsAtLastRow failed code:14800007 columnName:-1



[nodict]::[PrepareStep()-sqlite_shared_result_set.cpp:42]: StoreSession BeginStepQuery fail : not select sql !



[nodict]::[GetColumnCount()-abs_result_set.cpp:308]: Failed to GetAllColumnNames, ret is 14800007



[nodict]::[IsColumnNull()-napi_result_set.cpp:503]: throw error: code = 14800000 , message = Inner error. Inner code is 8



[nodict][ecmascript] Pending exception before IsMixedDebugEnabled called in line:3200, exception details as follows:



[nodict]Error: Inner error. Inner code is 8



代码如下：



```typescript
1. async query() {
2.  const STORE_CONFIG: relationalStore.StoreConfig = {
3.  name: 'NetMonitor.db',
4.  securityLevel: relationalStore.SecurityLevel.S1
5.  };
6.  let rdbStore: relationalStore.RdbStore = await relationalStore.getRdbStore(context, STORE_CONFIG).then();
7.  let sql = 'SELECT * FROM net_monitor ORDER BY id desc LIMIT 20';
8.  let resultSet = await rdbStore.querySql(sql)
9.  let uuid = this.getString(resultSet, columnUuid) // report errors
10. }
11. /**
12.  * Retrieve the string column value of the current row in the result set.
13.  * @param resultSet
14.  * @param columnName
15.  * @returns
16.  */
17. private getString(resultSet: relationalStore.ResultSet, columnName: string): string | undefined {
18.  let isColumnNull = resultSet.isColumnNull(resultSet.getColumnIndex(columnName));
19.  if (isColumnNull){
20.  return undefined
21.  } else {
22.  return resultSet.getString(resultSet.getColumnIndex(columnName))
23.  }
24. }

```


[QueryFail.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalDatabaseManagement/entry/src/main/ets/pages/QueryFail.ets#L25-L48)



**解决措施**



isColumnNull：用于检查当前行中指定列的值是否为null。



ResultSet：返回的结果集合，用于调用关系型数据库查询接口后提供给用户。



请先转到结果集中需要查询的行，再使用isColumnNull方法。例如，使用ResultSet.goToFirstRow()转到结果集的第一行。



**参考链接**



[ResultSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-resultset)
