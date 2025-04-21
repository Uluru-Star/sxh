def gcd(a,b):
    if b>a:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
if __name__=='__main__':
    a,b=input('输入a,b的值:').split()
    print(gcd(int(a),int(b)))     