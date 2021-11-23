# 리스트의 복사
a1 = [1,2,3,4]
a2 = [] #1. 빈리스트 생성
a2_2 = []
a3 = []

a1.append(5)
print(a1)

#2. a1에서 a2로 복사 저장
for i in a1:
    a2.append(i)

print(a2)

#3. a1의 2배 수로 저장
for i in a1:
    a2_2.append(i * 2)

print(a2_2)

#4. a1의 숫자 중 홀수만 저장
for i in a1:
    if i % 2 == 1:
        a3.append(i)

print(a3)


