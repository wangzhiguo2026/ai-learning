# ============================================
# project1_employee.py —— 员工档案系统 · 主程序
# 职责：显示菜单、问用户要做什么
# ============================================

import emp_tools as et          # 把工具模块导入进来12


def show_menu():
    print("\n========== 员工档案管理系统 ==========")
    print("1. 添加员工")
    print("2. 查看全部员工")
    print("3. 按姓名搜索")
    print("4. 按部门筛选")
    print("5. 统计部门数据")
    print("6. 删除员工（按工号）")
    print("7. 退出系统")


def main():
    employees = et.load_employees()          # 启动时先读文件
    print(f"系统已加载 {len(employees)} 名员工")

    while True:                              # 不选0就一直循环
        show_menu()
        choice = input("请输入操作编号：").strip()

        if choice == "1":
            # ---- 添加 ----
            name = input("请输入姓名：").strip()
            if not name:
                print("姓名不能为空")
                continue
            department = input("请输入部门：").strip()
            salary = et.input_float("请输入工资：")
            emp = et.add_employee(employees, name, department, salary)
            print(f"添加成功！工号：{emp['id']}")

        elif choice == "2":
            # ---- 查看全部 ----
            if not employees:
                print("还没有员工，请先添加")
            else:
                et.show_all(employees)

        elif choice == "3":
            # ---- 按姓名搜索 ----
            keyword = input("请输入姓名或姓名关键字：").strip()
            result = et.find_by_name(employees, keyword)
            if result:
                et.show_all(result)
            else:
                print("没有找到符合条件的员工")

        elif choice == "4":
            # ---- 按部门筛选 ----
            departments = et.get_departments(employees)
            if not departments:
                print("还没有员工，请先添加")
                continue
            print("现有部门：", "、".join(sorted(departments)))
            dept = input("请输入要查看的部门：").strip()
            result = et.filter_by_department(employees, dept)
            if result:
                et.show_all(result)
            else:
                print("该部门暂时没有员工")

        elif choice == "5":
            # ---- 统计 ----
            if not employees:
                print("还没有员工，无法统计")
                continue
            total, avg, highest, lowest = et.get_stats(employees)
            print(f"员工人数：{len(employees)} 人")
            print(f"工资总额：{total:.2f}")
            print(f"平均工资：{avg:.2f}")
            print("工资最高：", end="")
            et.print_employee(highest)
            print("工资最低：", end="")
            et.print_employee(lowest)

        elif choice == "6":
            # ---- 删除 ----
            emp_id = et.input_int("请输入要删除的员工工号：")
            if et.delete_by_id(employees, emp_id):
                print(f"工号 {emp_id} 已删除")
            else:
                print(f"没有找到工号 {emp_id}")

        elif choice == "7":
            print("已退出系统，数据已保存到 employees.csv")
            break

        else:
            print("没有这个选项，请输入 0~6 的数字")


# 只有“直接运行这个文件”时才执行 main()
# 如果以后别的文件 import project1_employee，不会一进来就跑菜单
if __name__ == "__main__":
    main()
