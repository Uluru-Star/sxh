#知道年份和天数，求这天是几月
year=int(input("输入年份："))
n=int(input("输入天数："))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29
month = 1
day = n
while day > days_in_month[month - 1]:
    day = day- days_in_month[month - 1]
    month = month + 1
print("该年的第",n,"天是",month,"月",day,"日")