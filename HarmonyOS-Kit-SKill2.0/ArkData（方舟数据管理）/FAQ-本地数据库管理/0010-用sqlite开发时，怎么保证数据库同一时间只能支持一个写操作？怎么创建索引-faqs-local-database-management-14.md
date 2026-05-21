# 用sqlite开发时，怎么保证数据库同一时间只能支持一个写操作？怎么创建索引

可以使用事务来确保数据库在同一时间只支持一个写操作。创建索引时，请参考SQLite的官方文档中的索引创建语法规范。。



1.定义SQL语句的常量



const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,salary REAL)';



const CREATE_INDEX = 'CREATE INDEX idx_name ON employee (name)';



2.使用executeSql执行包含指定参数的 SQL 语句，但不返回值。



this.rdbStore.executeSql(SQL_CREATE_TABLE);



this.rdbStore.executeSql(CREATE_INDEX);



**参考链接**



[beginTransaction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#begintransaction)
