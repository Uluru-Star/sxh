print("所有的水仙花数有：")
for i in range(100,1000):
    x=i//100
    y=(i-x*100)//10
    z=i-x*100-y*10
    if i==x**3+y**3+z**3:
        print(i)