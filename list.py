#输出你名字的Unicode码值，并转换为汉字
name=input("输入你的名字:")
print("姓名中每个字符的Unicode码值为:")
for char in name:
    print(ord(char))
unicode_num=[ord(char) for char in name]#从循环里取值生成Unicode新列表
named=''
for num in unicode_num:
    named +=chr(num)
print("转换为汉字为:",named)