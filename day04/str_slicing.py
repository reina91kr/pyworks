#문자열 슬라이싱
s = "20211123cold"
year = s[:4]
day = s[4:8]
weather = s[8:]

print(year)
print(day)
print(weather)

print()

#주민번호
id_card = "881120-1068234"
yymmdd = id_card[:6]
num = id_card[7:]

#뒷번호를 숨기고 싶다면?
num_hidden = '*' * len(num)
print(yymmdd)
print(num)
print(yymmdd + '-' + num_hidden)

