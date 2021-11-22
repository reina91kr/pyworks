#점수의 합계와 평균, 최고점수, 최저 점수

score = [70, 80, 90, 20, 40]
sum = 0
count = len(score)
avg = 0.0

#점수의 합계
for i in score:
    sum += i

#평균 계산
avg = sum / count

#최고 점수
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i

#최저 점수
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i

print("합계 :", sum)
print("평균 :", avg)
print("최고 점수 :", max_v)
print("최저 점수 :", min_v)
