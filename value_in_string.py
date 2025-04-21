def func(str):
    letters=0
    digits=0
    other=0
    for char in str:
        if char.isalpha(): # 检查是否是字母
            letters+=1
        elif char.isdigit(): # 检查是否是数字
            digits+=1
        else:
            other+=1 # 其他类型的字符
    return letters,digits,other

if __name__=='__main__':
    str='gfvja56451238/;.12'
    letters, digits, others = func(str)
    print(f"字母个数: {letters}")
    print(f"数字个数: {digits}")
    print(f"其他字符个数: {others}")
