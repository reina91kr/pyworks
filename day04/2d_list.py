#2차원 리스트
a = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print("리스트의 크기(행) :", len(a)) # 10, 30, 50
print("리스트의 크기(행) :", len(a[0])) #10, 20
print("리스트의 크기(행) :", len(a[1])) # 30, 40
print("리스트의 크기(행) :", len(a[2]))  # 50, 60
print(a)

#리스트 추가
a.append([70, 80])

print('*' * 10)
#출력
for x, y in a :
    print(x, y)

print('*' * 10)
#중첩 for
for i in range (0, len(a)):
    for j in range (0, len(a[i])):
        print(a[i][j], end=' ')
    print()

#합계와 평균 계산하기
sum_v = 0
avg = 0.0
count= 0

for i in range (0, len(a)):
    for j in range (0,len(a[i])):
        sum_v += a[i][j]
        count += 1
    print()


avg = sum_v / count
print("합계 : {}점".format(sum_v))
print("평균 : {}점".format(avg))

