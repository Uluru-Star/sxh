x,y,z=input("输入三个数:").split()
if x>y:
    if x>z:
        print(x,max(y,z),min(y,z))
    else:
        print(z,max(x,y),min(x,y))
else:
    if y>z:
        print(y,max(x,z),min(x,z))
    else:
        print(z,max(x,y),min(x,y))