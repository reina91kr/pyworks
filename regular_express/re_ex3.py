import re

str = "Two is too"
m1 = re.findall("T[ow]o", str)      #Two

print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE)       #대소문자 구분 X

print(m2)

m3 = re.findall("t[^w]o",str)       #too  ^ = not 

print(m3)