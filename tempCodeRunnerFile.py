n1=1
n2=1
count=2
print("斐波那契数列的前15项为:",end=' ')
print(n1,n2,end=' ')#输出前两项
while count<15:
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3
    count+=1