#将大于2的偶数n表示为两个素数之和
import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
       if n%i==0:
         return False
       else:
           return i
       
def isgdbh(num):
    if num<=2 or num%2!=0:
        return False
    for i in range(3,num//2+1):
            if isprime(i) and isprime(num-1):
                print(f'{num}={i}+{num-1}',end=' ')
                
print(isprime(5))