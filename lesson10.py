# 第十课：模块 module 与 import（把代码拆进不同文件）

# ========== 1. import 系统自带模块 ==========
# random 是 Python 自带的模块，装 Python 就有，不用自己写
import random
# 用 random.函数名：randint(1, 6) = 从 1~6 随机抽一个整数
print("随机数",random.randint(1,6))

# ========== 2. from 模块 import 名字 ==========
# import random 后用起来要写 random.choice；
# from random import choice 直接把 choice 函数“拿进来”，调用时少写前缀
from random import choice

name = ["张三","李四","王治国"]
print("随机选中的同学：",choice(name))
# ========== 3. import 自己写的模块 ==========
# tools.py 和 lesson10.py 放在同一文件夹里
# import tools 会执行 tools.py，里面的 def 函数变成 tools 的“财产”

import tools
print(tools.greet("王治国"))
print("3+5=", tools.add(3,5)) #调用tools中add函数

# ========== 4. 取别名 as ==========
# 名字太长或想用短名：from 模块 import 名字 as 别名
from tools import avg as average
scores = [92,58,75]
print("三个同学的平均分：",average(scores))
# ========== 5. 其他常用内置模块 ==========
import math
print("圆周率：",math.pi)
print("16的开平方：",math.sqrt(16))

