# 第六课：元组、集合、类型转换
# ========== 1. 元组 tuple：不能修改的列表 ==========
# 用小括号 ()，和列表一样能取、能数、能遍历
point =(3,5)
print(point[0])
print(point[1])
print(len(point))
# 元组不能修改：下面这行会报错 TypeError
# point[0] = 99             # ← 取消注释试试，会报错

# 为什么需要元组？数据不允许被改（比如坐标、日期），防手滑

# ========== 2. 集合 set：自动去重 ==========
# 用大括号 {}，但没有键值对，只有元素；重复的会自动去掉
nums =[1,2,2,3,3,3,4]
unique = set(nums)       # 列表 → 集合（自动去重）
print(unique)            # {1, 2, 3, 4}


# 集合运算：交集 &（两边都有的）、并集 |（合起来）
a ={1,2,3,4}
b ={3,4,5,6}
print(a&b)      # {3, 4}（共同元素）
print(a | b)      # {1, 2, 3, 4, 5, 6}（全部元素)


# 往集合里加/删除
s={"苹果","香蕉"}
s.add("橘子")
print(s)        # {'苹果', '香蕉', '橘子'}
s.remove("香蕉")
print(s)         # {'苹果', '橘子'}


# ========== 3. 类型转换：int / float / str ==========
# 字符串 → 数字
age_text = "26"
age_num = int(age_text)       # 26（数字）
print(age_num+1)                # 27（能加减了）

# 数字 → 字符串
num = (int(3.9))     # 3（不是4！）
print(round(3.9))    # 4（round 才是四舍五入）
# 整数 → 小数
print(float(5))
# 字符串 → 小数
price = "19.9"
print(float(price)*2)

# ========== 4. 实战：去重 + 统计 ==========

names = ["张三","李四","张三","王治国","李四","李四"]
uniqut_names = set(names)
print(f"原始{len(names)}条,去重后{len(uniqut_names)}条")
for name in uniqut_names:
    print(name)