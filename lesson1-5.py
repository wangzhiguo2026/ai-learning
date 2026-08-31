#复习
# 复习课：把第 1-5 课串起来

# ========== 第一部分：基础知识回顾 ==========
# 1. 变量和类型（第1课）
name = "王治国"
age = 26
height = 1.75
is_student = True
print(f"{name}今年{age}岁，身高{height}米，是学生:{is_student}")

# 2. 列表和字典（第2课）
classmates = ["张三", "李四", "王治国"]
print(f"全班{len(classmates)}人，第一个人是{classmates[0]}，最后一个是{classmates[-1]}")
scores = {"张三": 92, "李四": 58, "王治国": 75}
print(f"张三的分数是{scores['张三']}")

# 3. 判断和循环（第3课）
for name, score in scores.items():
    if score >= 60:
        print(f"{name}:{score}分，及格")
    else:
        print(f"{name}:{score}分，不及格")

# 4. 函数（第4课）——注意：这里顶格了，和上面的 for 同级！
def add(a, b):
    return a + b
print(f"add(3,5) = {add(3,5)}")

# 5. 字符串（第5课）——注意：split 不是 strip！
data = "苹果，香蕉，橘子"
fruits = data.split("，")
print(f"有{len(fruits)}种水果:{'、'.join(fruits)}")


# ========== 第二部分：班级成绩分析（函数 + 字典 + 循环 + 判断 + 字符串）==========

def calc_avg(scores_list):
    """计算一个学生的平均分"""
    total = 0
    for s in scores_list:
        total = total + s
    return total / len(scores_list)   # 重点：顶格，和 for 同级！

def make_report(student_scores):
    """生成成绩单：每条记录 = 姓名 + 平均分 + 评级"""
    report = []
    for name, scores_list in student_scores.items():
        avg = calc_avg(scores_list)
        if avg >= 90:
            level = "优秀"
        elif avg >= 70:
            level = "良好"
        elif avg >= 60:
            level = "及格"
        else:
            level = "不及格"
        report.append({"名字": name, "平均分": avg, "评级": level})
    return report
#调用函数
class_data = {
    "张三":[88,92,78],
    "李四":[55,61,48],
    "王治国":[95,88,90],
}
report = make_report(class_data)
print("\n===== 成绩单 ====")
for item in report :
    print(f"{item['名字']} 平均分{item['平均分']:.1f}")

avg_list = []
for item in report:
    avg_list.append(item["平均分"])

best = avg_list[0]
worst = avg_list[0]
for a in avg_list:
    if a> best:
        best=a
    if a < worst:
        worst=a


print(f"\n全班最高平均分:{best:.1f}")
print(f"全班最低平均分:{worst:.1f}")

# 谁的分数最高？（用 find 的亲戚 index：在列表里找位置）
for item in report:
    if item["平均分"] == best:
        print(f"第一名是{item['名字']},平均分{item['平均分']:.1f}")

    
