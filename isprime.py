#判断一个数是否是素数
import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
       if n%i==0:
         return True
    
if __name__=='__main__':
    n=input('输入一个整数:')
    if isprime(int(n)):
       print('%s是素数'%(n))
    else:
       print('%s不是素数'%(n))