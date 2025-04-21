#向文件中写入字符串
with open('data1.txt','w') as file:
    num1=file.write('白云满鄣来,黄尘暗天起。 关山四面绝,故乡几千里。')
    print('向文件中写入字符%d个'%(num1))
with open('data2.txt','w')as file:
    list1=[1,1]
    n1=n2=1
    count=2
    while count<10:
        n3=n1+n2
        list1.append(n3)
        n1=n2
        n2=n3
        count+=1
    print(list1)
    num2=file.write(str(list1))
    print('向文件中写入字符%d个\n'%(num2))

#读取文件中的内容
with open('data1.txt','r') as file:
    str1=file.read()
    print(str1)
with open('data1.txt','r') as file:
    for line in file:
        print(line)
with open('data2.txt','r') as file:
    list1=file.read()
    print(list1)