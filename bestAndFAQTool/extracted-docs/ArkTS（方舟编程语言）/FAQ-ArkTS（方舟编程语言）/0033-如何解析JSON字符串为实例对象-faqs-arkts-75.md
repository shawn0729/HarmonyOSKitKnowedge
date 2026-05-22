# 如何解析JSON字符串为实例对象

**问题背景**：



需要将JSON数据转换成ArkTS中类的实例对象。可以使用实例对象的属性，调用实例对象的方法。支持嵌套对象的场景。



对于这种情况，需要使用三方库 class-transformer 和 reflect-metadata（需通过 npm install 进行安装）。通过 @Type 指定嵌套情况下的类型，并使用 plainToClass 转换创建相应的实例对象。



**完整示例如下：**



```typescript
1. import { Type, plainToClass } from 'class-transformer'
2. import "reflect-metadata"
3.
4. // Assuming accepted JSON data
5. let testJSON: Record<string, ESObject> = {
6.  'id': 1,
7.  'firstName': "Johny",
8.  'lastName': "Cage",
9.  'age': 27,
10.  'arr': [
11.  {
12.  'name': 'john'
13.  },
14.  {
15.  'name': 'tom'
16.  }
17.  ],
18.  'instanceA': {
19.  'name': 'john'
20.  },
21. }
22.
23. // If there is a corresponding nested structure, the corresponding type needs to be specified
24. class A {
25.  name: string = 'john';
26.
27.  getName(): string {
28.  return this.name
29.  }
30. }
31.
32. // When attempting to convert an object with nested objects, it is necessary to know the object type to be converted and use the @ Type decorator to implicitly specify the object type contained in each attribute
33. class User {
34.  id: number = 0;
35.  firstName: string = '';
36.  lastName: string = '';
37.  age: number = 0;
38.  @Type(() => A)
39.  arr: A[] = [new A()]
40.  @Type(() => A)
41.  instanceA: A = new A();
42.
43.  getName() {
44.  return this.firstName + " " + this.lastName;
45.  }
46.
47.  isAdult() {
48.  return this.age > 36 && this.age < 60;
49.  }
50. }
51.
52. @Entry
53. @Component
54. struct parsingJSONStringsIntoInstanceObjects {
55.  aboutToAppear(): void {
56.  const instance = plainToClass(User, testJSON);
57.  console.info('instance:' + JSON.stringify(instance))
58.  }
59.
60.  build() {
61.
62.  }
63. }

```


[TestJSON.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestJSON.ets#L21-L83)
