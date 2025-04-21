a=0x356e
num=int(a)
print("输出a的十进制数:%d"%num)

#用两种方法将一个数逆置
reverse=0
while a>0:
    b=a%10
    a=a//10
    reverse=reverse*10+b
print('数字类型运算结果: %s'%reverse)
str=str(num)
print('字符串运算结果:',str[::-1])