for i in range(1,10):
    for j in range(1,i+1):                  #j的范围是1到i
        print(f"{j}x{i}={i*j}", end="\t")   #end="\t"是每次打印后不换行，而是换到下一列
    print()                                 #外层循环结束一次后换行