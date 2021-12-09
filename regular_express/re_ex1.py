import re

#compile() - > byte코드 바꿈, 함수 매개변수로 정규식 사용

p = re.compile("[a-z]+")        #+가 없으면 한 글자만 찾음 / [a-z]+ 범위 안의 소문자
m = p.match("afternoon")        #일치 여부를 결과로 반환

print(m)

m2 = p.match("2021 python")
print(m2)                       #NONE: match가 일치하면 TRUE; 첫 글자가 일치하지 않으면 false (NONE)

s = p.search("2021 python")     #전체 문자에서 검색한 뒤 일치하는 내용을 찾음
print(s)