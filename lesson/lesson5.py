#第5课字符串的处理

#1.拼接 用+ 把字符串拼接起来
first = "王"
last = "治国"
full = first + last
print(full)

#2重复：用* 让字符串重复N遍
line = "=" * 10
print (line)

#3长度和索引(和列表一样，从0开始)
name = "python"
print(len(name))
print(name[0])
print(name[-1])

#4.切片：取一段，写法[开始:结束]，注意结束位置不包含
msg = "hello world"
print(msg[0:5])                    # hello（取 0~4）
print(msg[6:])                     # world（6 到结尾）
print(msg[:5])                     # hello（开头到 5
print(msg[::2])                    # hlowrd（每 2 个取一个）

#5.大小写转换
text = "Hello Python"
print(text.upper())
print(text.lower())
print(text.title())

#6.查找和替换
s = "我喜欢Python,Python真好"
print (s.find("Python"))
print(s.replace("Python", "AI"))

#7.split 切分 +join 合并（超长用）
data ="张三，李四，王治国"              
names = data.split("，")            #按逗号切成列表
print (names)                       # ['张三', '李四', '王治国']
print("、".join(names))              # 张三、李四、王治国

#8.格式化：f-string 把变量塞进字符串（最推荐）
age = 26
height = 1.75
print(f"我今年{age}岁,身高{height}米")

#9 去掉收尾空白+判断
word = "  hello  "
print(word.strip())             # hello（去掉两边空格）
print("abcd123".isalnum())      # True（是不是字母数字）
print("123".isdigit())           # True（是不是纯数字）