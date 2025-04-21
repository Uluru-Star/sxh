s=["1","2","7","a","c","n"]
length=len(s)
str=[]
for i in range(length):
    for j in range(length):
        if i!=j:
          for k in range(length):
            if i!=k and j!=k:
               for l in range(length):
                  if i!=l and j!=l and k!=l:
                     str.append(s[i]+s[j]+s[k]+s[l])#运用索引，则得用s[i]来表示列表
print(f"总共有 {len(s)} 个不同的字符串：")
for s in str:
    print(str)