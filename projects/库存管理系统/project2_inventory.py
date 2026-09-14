import inv_tools as it

# project2_inventory.py —— 商品库存管理系统主程序
# 职责：显示菜单、问用户要数据、调用 inv_tools 干活
def show_menu():
    print("\n========== 商品库存管理系统 ==========")
    print("1. 商品入库")
    print("2. 查看全部商品")
    print("3. 按名称搜索")
    print("4. 按分类筛选")
    print("5. 商品出库")
    print("6. 库存统计与预警")
    print("7. 退出系统")

def input_float(prompt):
    """安全读一个小数：输错就重问，不允许负数。"""
    while True:
        try:
            valus = float(input(prompt).strip())
            if valus <= 0:
                print("单价必须大于0，请重新输入")
                continue
            return valus
        except ValueError:
            print("输入无效，请输入数字（例如5.5）")

def input_int (prompt):
    """安全读一个整数：输错就重问，不允许负数。"""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print("不能是负数，请重新输入")
                continue
            return value
        except ValueError:
            print("输入无效，请输入整数（例如120）")


def print_product(p):
    """把一件商品按固定格式打印成一行。"""
    print(f"编号：{p['id']}  名称：{p['name']}  分类：{p['category']}  "
          f"单价：{p['price']:.2f}  库存：{p['qty']}")

def show_list(products):
    """把一批商品打印出来；如果是空的，给个提示。"""
    if not products:
        print ("没有符合条件的商品")
        return
    for p in products:
        print_product(p)
def main():
    products = it.load_products()
    print(f"系统已经启动，当前仓库里有{len(products)} 件商品")
    while True:
        show_menu()
        choice = input("请输入操作编号：").strip()

        if choice == "1":
            name = input("请输入商品名称：").strip()
            if not name:
                print("商品名称不能为空")
                continue
            category = input("请输入商品分类：").strip()
            price = input_float("请输入单价：")
            qty  = input_int("请输入库存量：")
            product = it.add_product(products, name, category, price, qty)
            it.save_products(products)
            print("入库成功！新商品编号", product["id"])
        
        elif choice == "2":
            show_list(products)

        elif choice == "3":
            keyword = input("请输入商品名称或者关键字：").strip()
            show_list(it.find_by_name(products,keyword))

        elif choice == "4":
            categories = it.get_categories(products)
            if not categories:
                print("仓库还是空的，请先入库")
                continue
            print("现有分类：", "、".join(categories))
            category = input("请输入要查看的分类：").strip()
            show_list(it.filter_by_category(products,category))
            
        elif choice ==  "7":
                print("已退出系统，数据已保存")
                break
            
        else:
            print("这个功能下一步在做")
if __name__ == "__main__":
    main()
    








