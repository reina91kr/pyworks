#문자열 함수 - 특별한 1차원 리스트
#나열된 문자를 list타입으로 변경하는 split function

s = 'banana,grape,apple'
x = s.split(',')

print(x)
print()

print(x[0])
print()

for i in x:
    print(i)

print()

s2 = 'a:b:c:d'
y2 = s2.split(':')

print(y2)

print()

a = '윤지 철수 영희'
z = s.split(' ')

print(a)
print()

# 두 수를 동시에 입력 받아 더하기

n1, n2 = input("국어, 점수 입력: 예) 10, 40").split(',')
add = int(n1) + int(n2)
print(add)
