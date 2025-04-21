#使用装饰器对上述两个函数传入参数进行合法性检查，边长或长宽有0或负数的直接返回提示
def check_parameters(func):
    def wrapper(*args):
        if any(arg <= 0 for arg in args):
            return "提示：参数中存在负数或零"
        else:
            return func(*args)
    return wrapper

@check_parameters
def triangle(x,y,z):
    n=x+y+z
    return n
@check_parameters
def rectangle(m,n):
    s=2*(m+n)
    return s

print(rectangle(-10, 11))  
print(rectangle(7, 11))    
print(triangle(2, 3, 4))   
print(triangle(2, 3, -3))