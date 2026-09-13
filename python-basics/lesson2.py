
#第二课 ：列表list 和字典 dict
#1列表：一筐数据，按照数据排好，用中括号[]
students = ["张三","李四","王治国"]
print(students)

#去元素编号：编号（索引）从0开始
print(students[0])
print(students[2])
#往末尾追加一个
students.append("赵五")
print(students)
#列表里有多少个元素
print(len(students))

#字典：成对的数据（键：值）像通讯录，用大括号{}
person = {"名字":"王治国","年龄":26,"身高":1.75}
#按“键” 查 “值”
print(person["名字"])
print(person["年龄"])
#新增一项/修改一项
person["城市"] = "上海"
print(person)

#列表套字典
classmates =[
    {"名字":"张三","年龄":25},
    {"名字":"李四","年龄":27},
]
print(classmates)
print(classmates[0]["名字"])#先去第一个同学，在取他的名字