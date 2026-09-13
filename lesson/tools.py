# 第十课配套文件：自己写的“工具箱” tools.py
# 里面只定义函数，不负责运行，等别人 import 后调用
def greet(name):
    """打招呼：传一个名字，返回一句问候"""
    return f"你好，{name}!"
def add (a,b):
    " ""加法：返回 a+b"" "
    return a+b
def avg(numbers):
    """平均分：把列表的数加起来，除以个数"""
    total = 0
    for n in numbers:
        total += n              # 等价于 total = total + n
    return total / len(numbers)

    