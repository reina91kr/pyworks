#1~20 중 3의 배수
count = 0
sum = 0

for i in range(1, 21):
    if i % 3 == 0:
        count += 1
        sum += i
        print(i, end=' ')

avg = sum/count
print()
print()
print("3의 배수의 개수는", count)
print("3의 배수의 합계는", sum)
print("3의 배수의 평균은", avg)
