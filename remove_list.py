#删除列表中重复的元素
list1=input("输入一个列表:").split()
list1=list(list1)
list2=[ ]
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print("去重后的列表为:",list2)
