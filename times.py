import time
import timeit
def gcd(a,b):
    if b>a:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
if __name__=='__main__':
    start_time = time.time()  # 记录开始时间
    print(gcd(1658,654))  #输出最大公约数
    end_time = time.time()  # 记录结束时间
    print(f"计算gcd(1658,654)的运行时间: {end_time - start_time} seconds")  # 输出计算耗时
    print(timeit.timeit(lambda:gcd(1658,654),number=100))
    print(f"输出当前日期和时间: {time.ctime()}")