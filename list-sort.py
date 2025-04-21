#冒泡排序
list1 = [40, 65, 62, 52, 13]
N = len(list1)
for i in range(N-1):
    for j in range(N-i-1):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)

#选择排序
list1 = [40, 65, 62, 52, 13]
N = len(list1)
for i in range(N-1):
    for j in range(i+1,N):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)

#简单排序
list1 = [40, 65, 62, 52, 13]
N = len(list1)
result = []
for i in range(N):
    max_ele = max(list1)
    result.append(max_ele)
    list1.remove(max_ele) #删除list1中最大值
print(result)

#最简单排序
list1 = [40, 65, 62, 52, 13]
list1.sort()
list1.reverse()
print(list1)
