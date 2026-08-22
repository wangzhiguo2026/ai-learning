
#第三课：if 和for循环
#1 if：条件成立才执行
age = 20
if age >=18:
    print("成年了")
else:
    print("未成年")

#2 elif:多分支判断
score = 85
if score >= 90:
    print("优秀")
elif score >=60:
    print("及格")
else:
    print("不及格")

#3 for：把列表里面的东西一个一个拿出来
students = ["张三","李四","王治国"]
for name in students:
    print("同学",name)

#4循环+判断组合（真实程序的样子）
scores ={"张三": 92,"李四": 58, "王治国": 75}
for name, score in scores.items():
    if score >= 60:
        print(name,"及格了，分数线",score)
    else:
        print(name,"不及格,分数",score)