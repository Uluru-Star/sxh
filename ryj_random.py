import random
from collections import Counter #计数器模块

data_tuple=()
for i in range(20):
    data_tuple=data_tuple+(random.randint(1,10),)
print('随机生成的元组：',data_tuple)

counters=Counter(data_tuple)#统计元组中每个元素的次数
for number, count in counters.items():  #counters.items()获取字典的key和value
    print(f"整数 {number} 出现了 {count} 次")