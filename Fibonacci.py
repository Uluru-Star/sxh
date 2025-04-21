#输出斐波那契数列的前15项
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

#求第项斐波那契数
def fibonacci(i):
    x=1
    y=1
    n=2
    if i == 1 or i == 2:
        return 1
    while n<i:
        z=x+y
        n=n+1
        x=y
        y=z
    return z
print('\n第10项的数为：',fibonacci(10))

#求前n项之和
def sum(n):
    s=0
    for i in range(1,n+1):
        s+=fibonacci(i)
    return s

print('前10项之和为:',sum(10))
