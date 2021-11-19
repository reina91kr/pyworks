# for num in (1,2,3,4,5)
# for num in range (1, 6, 1)  / 1과 6의 범위에서 1씩 증가 / 1,2,3,4,5 * 마지막 숫자는 반드시 범위보다 1개 더 큰 수여야 한다.

"""
for i in (1,2,3,4,5):
    print(i) 
"""

for i in range (1,6,1): #range(초기값, 종료값-1, 증감값)
    print(i, end=' ')
    
print("\n")
#1부터 10까지의 홀수 출력

for i in range (1,11,2):
    print(i, end=' ')

print("\n")

for i in range (1,11):
    if i % 2 != 0:
        print(i, end =' ')
        
#1부터 10까지의 합계 출력

print("\n")

sum_v=0

for i in range (1,11):
    sum_v += i
    print("i =", i, ", sum =", sum_v)

print("sum =", sum_v)
