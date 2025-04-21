import re
str="The parameters of C are 85, 74 and 8."
str1=re.sub(r'\d','**',str)
print(str1)