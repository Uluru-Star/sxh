#输出一定范围内的所有素数
import math
def is_prime(number):
    if number<=1:
        return False
    for i in range(2,int(math.sqrt(number)) + 1):
       if number%i==0:
           return False
    return True
 
for num in range(1,10):
        if is_prime(num):
           print(num,end=' ')