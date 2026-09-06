# 第九课：异常处理 try / except

# ========== 1. 基本结构：try + except ==========
# try：放"可能出错"的代码
# except：出错后执行这里的代码（救场）

print("===基本信息异常处理==")
try:
    num = int("abc")      # 故意写错：abc 不能转数字
    print("转换成功：",num)
except ValueError:
    print("出错了！abc 不能转成数字")
    print("程序没蹦，继续走\n")


# ========== 2. 捕获不同类型的异常 ==========
# 不同的错误有不同的"名字"（异常类型）
print("===多种异常分别处理===")
try:
    num = int("abc")
except ValueError:
    print("ValueError:转数字失败，内容不是数字")
except ZeroDivisionError:
    print("ZeroDivisionError:除以0了")
 # 通用兜底：不知道什么错，用 Exception 接住所有错误   
try:
    lst = [1,2,3]
    print(lst[99])  # IndexError：索引越界
except Exception as e:
    print("出错了，错误类型是：",type(e).__name__)
    print("错误信息：",e)

# ========== 3. else 和 finally ==========
# else：没出错才执行（try 成功后的"奖励"）
# finally：不管出没出错都执行（收尾工作，比如关文件）
print("===else和finally===")
def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("不能除以 0")
    else:
        print("除法成功",result)
    finally:
        print("finally:这一步无论如何都会执行")
safe_divide(10,2)  # 成功 → else 和 finally 都执行
safe_divide(10,0)   # 出错 → except 和 finally 执行，else 跳过


# ========== 4. 实战：防止 input 崩溃 ==========
# 用户输入不可控，异常处理是防崩溃的关键
print("===4.安全的输入")
while True:
    try:
        age = int(input("请输入你的年龄（输入的数字）："))
        break   # 成功转换就跳出循环
    except ValueError:
        print("输入无效，请重新输入数字")
print(f"你 {age} 岁，明年 {age + 1} 岁\n")

    # ========== 5. 实战：文件读取防错 ==========
# 文件不存在时程序会崩，用异常处理给出友好提示
print("===5.安全读取文件===")
try:
    with open("不存在为文件.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在，请检查文件名")
except Exception as e:
    print("读取出错:",e)
print("\n整个程序完全跑完，一次都没蹦")

    