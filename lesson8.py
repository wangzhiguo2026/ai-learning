# 第八课：读写文件

# ========== 1. 写文件 ==========
# open("文件名", "w")：打开文件准备写。w = write（写）
# 注意：w 模式会"清空重写"——如果文件已有内容，会被覆盖
file = open("notes.txt", "w", encoding="utf-8")
file.write("第一行：今天学了读写文件\n")
file.write("第二行：王治国加油\n")
file.write("第三行：离 AI 应用越来越近了\n")
file.close()

print("文件写入完成")

# ========== 2. 读文件（read：一次全读）==========
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
print("--- 整个文件内容 ---")
print(content)

# ========== 3. 读文件（readlines：按行读成列表）==========
file = open("notes.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
print("--- 按行读 ---")
print(lines)

for line in lines:
    print("读到一行:", line.strip())

# ========== 4. with 语句（推荐写法，自动关文件）==========
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("--- with 读取 ---")
print(content)

with open("new_notes.txt", "w", encoding="utf-8") as file:
    file.write("用 with 写的文件\n")
    file.write("自动关闭，很安全\n")
print("new_notes.txt 写入完成")

# ========== 5. 追加模式 a（不覆盖，接着写）==========
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("第四行：追加的内容\n")
print("已追加一行")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

# ========== 6. 实战：成绩单存档 ==========
students = {"张三": 92, "李四": 58, "王治国": 75}

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("姓名,分数,评级\n")
    for name, score in students.items():
        if score >= 60:
            level = "及格"
        else:
            level = "不及格"
        file.write(f"{name},{score},{level}\n")

print("report.txt 已生成，内容如下：")
with open("report.txt", "r", encoding="utf-8") as file:
    print(file.read())
