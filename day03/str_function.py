#find()함수
s = "Hello, welcome to my website"
print(s.find('H')) #0 번 위치
print(s.find('ll')) # 첫번째 문자 위치
print(s.find('k')) #찾는 문자가 없으면 -1
s = s.find('welcome') #단어로 검색: welcome의 첫 문자위치 = 7에서 w가 시작`
print(s)

#strip()함수 - 양쪽 공백 제거
str1 = "    hi, soo!"
print(str1.strip())

txt = "          banana       "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#isnumeric() - 숫자인지 검사하는 함수
text = "123".isnumeric()
print(text) # True

text2 = "123ab".isnumeric()
print(text2) #False