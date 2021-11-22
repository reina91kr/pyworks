#점수의 합계와 평균, 최고점수, 최저 점수
#간단하게 만드는 법

score = [70, 80, 90, 20, 40]

# #점수의 합계
# for i in score:
#     if max < i:
#         max = i
#     if min > i:
#         min = i

print("sum :", sum(score))
print("max :", max(score))
print("min :", min(score))
print("avergage ", sum(score)/len(score))
