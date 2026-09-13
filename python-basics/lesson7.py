# 第七课：input 输入 + 运算符
# ========== 1. input：程序停下来等你输入 ==========
# input("提示文字")：先显示提示，等你敲完回车，把你输入的内容作为字符串返回
name = input("你叫什么名字")
print("你好，"+name)
# 注意：input 返回的一定是字符串！要当数字用必须转换
age_text = input("你今年几岁了？")
age = int(age_text)
print(f"明年你就{age+1}")
# 也可以直接转（一步到位）
height = float(input("你身高多少米？"))
print(f"你身高{height}米")

# ========== 2. 算术运算符 ==========
a = 10
b =3
print(a+b)
print(a-b)
print(a*b)
print(a/b)    # 3.3333333333333335  除（结果是浮点数）
print(a//b)        # 3   整除（商，去掉小数）
print(a%b)       # 1   取余（除完剩多少）
print(a**b)         # 1000  次方（10 的 3 次方）

# // 和 % 的实用场景
print(7//2)       # 3（7 块糖 2 人分，每人 3 块）
print(7%2)           # 1（还剩 1 块）
print(3600//60)         # 60（3600 秒是几分钟）
print(3600%60)          # 0（还剩几秒）

# ========== 3. 比较运算符（结果都是 True/False）==========
x = 5
print(x > 3)     # True
print(x < 3)     # False
print(x >= 5)    # True（大于等于）
print(x == 5)    # True（等于，注意是两个等号！）
print(x != 5)    # False（不等于）

# 一个等号 = 赋值（把值装进盒子）
# 两个等号 == 比较（问两边一样吗）
y = 5            # 赋值
print(y == 5)    # 比较 → True

# ========== 4. 逻辑运算符 and / or / not ==========
score = 85
is_member =True
print(score>= 60 and score<90)
print(score>=90 or score< 60)
print(not is_member)

# 实战：判断能不能进会员价
age = 22
if age >= 18 and age <= 60:
    print("成年人且未退票，全票")
else:
    print("未成年或已退休，优惠")

# ========== 5. 实战：BMI 计算器（把前面全用上）==========
print("n\====== BIM计算器 ======")
weight = float(input("请输入体重（KG）:"))
height_m = float(input("请输入你的身高（M）:"))
bmi = weight /(height_m **2)
print(f"你的BIM是 {bmi:.1f}")

if bmi  < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi  < 28:
    print("偏胖")
else:
    print("肥胖")


