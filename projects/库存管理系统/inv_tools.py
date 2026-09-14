import json
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR,"products.json")


def load_products():
    """把 products.json 读成一个列表；文件不存在或内容坏了就返回空列表。"""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("警告：products.json 格式不对，本次按空仓库处理，请检查该文件")
        return []

def save_products(products):
    """把商品列表整个写回 products.json。"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=2)


def next_product_id(products):
    """生成下一个商品编号：当前最大编号 + 1。"""
    if not products:
        return 1001
    biggest = products[0]["id"]
    for p in products[1:]:
        if p["id"] > biggest:
            biggest =p["id"]
    return biggest+1


def add_product(products, name, category,price, qty):
    """新建一件商品，追加进列表并返回它。注意：这里只改内存，不写盘。"""
    product = {
        "id": next_product_id(products),
        "name": name,
        "category": category,
        "price": price,
        "qty": qty,
    }
    products.append(product)
    return product

def find_by_name(products,keyword):
    """按名称模糊搜索：名称里只要含有关键字就算命中。"""
    result = []
    for p in products:
        if keyword in p["name"]:
            result.append(p)
    return result

def filter_by_category(products,category):
    """按分类筛选：分类必须完全相同才算命中。"""
    result = []
    for p in products:
        if p ["category"] == category:
            result.append(p)
    return result


def get_categories(products):
    """把仓库里出现过的分类去重后，按字母顺序返回。"""
    categories = set()
    for p in products:
        categories.add(p["category"])
    return sorted(categories)
    





      
    

