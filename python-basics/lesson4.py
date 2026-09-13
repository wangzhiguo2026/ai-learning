#第四课: 函数def
#定义函数：def 函数名(参数):
def greet():
    print("你好呀")
    print("欢迎来到函数世界")
    #调用函数: 函数名()
greet()
greet()
greet()

    #2带参数的函数名：括号里的是“参数”，每次调用可以给不同的值
def greet2(name):
    print("你好，",name)

greet2("张三")
greet2("王治国")

#3.参数+返回值: return 把结果“交出来”
def add(a,b):
    result = a+b
    return result

x = add(3,5)
print("3+5=",x)

#4.真实例子：判断及格，返回一句话
def check(score):
    if score >= 60:
        return "及格了"
    else:
        return "不及格"

scores ={"张三":92, "李四":58, "王治国":75}
for name, score in scores.items():
    print(name,check(score))
        