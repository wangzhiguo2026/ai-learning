# ============================================
# emp_tools.py —— 员工档案系统的“工具箱模块”
# 职责：管数据（加载/保存/增删查/统计）
# ============================================
import os

# 文件放“这个模块所在文件夹”，这样你在哪运行都能找到它
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR,("employees.csv"))
# ========== 读文件 → 变成 员工列表 ==========
# 员工列表长这样：
# [{"id":1001, "name":"张三", "department":"技术部", "salary":8000}, ...]
def load_employees():
    employees = []
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as file:
            lines = file.readlines() # 一行一行读

        for line in lines[1:]:    # 跳过第一行表头
            line =line.strip()      # 去掉换行和首尾空格
            if not line:             # 空行跳过
                continue
            parts = line.split(",")     # "1001,张三,技术部,8000" 切成4段

            employees.append({
                "id":int(parts[0]),       # 工号是整数
                "name":parts[1],            # 姓名是字符串
                "department":parts[2],       #部门是字符串
                "salary":float(parts[3]),   #工资是小数
            })
    except FileNotFoundError:
        #第一次运行还没有文件，返回空名单即可，不算错误
        return employees
    except (ValueError,IndexError):
         # 文件里有非数字/少一列 = 文件损坏，给友好提示
         print("警告：employees.csv 数据损坏，请检查文件")
         return employees
    return employees 
#========== 员工列表 → 存进文件 ==========
def save_employees(employees):
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        file.write("工号，姓名，部门，工资\n") # 第一行表头
        for emp in employees:
            file.write(f"{emp['id']},{emp['name']},{emp['department']},{emp['salary']}\n")

# ========== 自动生成下一个工号 ==========
def next_employee_id(employees):
    ids = []
    for emp in employees:
        ids.append(emp["id"])    # 没有任何员工 → 从1001开始
    if not ids:
        return 1001 
    biggest = ids[0]
    for n in ids[1:]:
        if n > biggest:
            biggest=n
    return biggest+1  
# ========== 添加员工 ==========
def add_employee(employees,name,department,salary):
    emp = {
        "id":next_employee_id(employees),
        "name":name,
        "department":department,
        "salary":salary,
    }
    employees.append(emp)    # 加进内存名单
    save_employees(employees)  # 立刻存进文件
    return emp                   # 把新员工交出去，主程序用来显示工号

   # ========== 显示一名员工 ==========
def print_employee(emp):
    print(f"工号：{emp['id']}  姓名：{emp['name']}  部门：{emp['department']}  工资：{emp['salary']:.2f}") 
   
# ========== 显示全部员工 ==========
def show_all(employees):
    for emp in employees:
        print_employee(emp)
        
# ========== 按姓名搜索（支持模糊：输入“王”也能找到“王治国”）==========
def find_by_name(employess,keyword):
    result = []
    for emp in employess:
        if keyword in emp["name"]:
            result.append(emp)
    return result

# ========== 取出所有部门（用集合去重）==========
def get_departments(employees):
    departments = set()
    for emp in employees:
        departments.add(emp["department"])
    return departments

# ========== 按部门筛选 ==========
def filter_by_department(emloyees,department):
    result = []
    for emp in emloyees:
        if emp["department"] == department:
            result.append(emp)
    return result

  
# ========== 按工号删除 ==========
def delete_by_id(employees,emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)  #从名单中移除
            save_employees(employees)   #存回文件
            return True             #删除成功
    return False                #没有找到这个人

  # ========== 统计：总工资/平均/最高/最低 ==========
def get_stats(employees):
    total = 0
    for emp in employees:
        total += emp["salary"]       # total = total + 工资
    avg = total / len(employees)  

    highest = employees[0]
    lowest = employees[0]
    for emp in employees[1:]:
        if emp["salary"] > highest["salary"]:
                highest =emp
        if emp["salary"] < lowest["salary"]:
                lowest = emp
    return total,avg,highest,lowest
    
# ========== 安全输入整数（防止用户输入 abc）==========
def input_int (prompt):
    while True:
        try:
            return int((input(prompt).strip()))
        except ValueError:
            print("输入无效，请输入整数（例如1001）")

# ========== 安全输入工资（防止 abc / 负数）==========
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            print("工资不能是负数，请从新输入")
        except ValueError:
            print("输入无效，请输入数字（例如 8000）")


        

    
    