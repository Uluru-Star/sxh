import re

L = ["123456789101112","123456789101112562","12345678910111256X","12345678910111256245632"]
reg = r"^\d{15}$|^\d{17}[\dX]$"
for l in L:
    result = re.findall(reg,l)
    if result:
        print("合法")
    else:
        print("不合法")