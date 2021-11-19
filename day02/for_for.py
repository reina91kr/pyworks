#중첩 for문

#5행 5열에 문자출력

for i in range(0,5): # 1,2,3,4,5 = 5열
    for j in range(0,5):   #1,2,3,4,5 = 5행
        print("$", end=' ')
    print() # 다음칸으로 내리기 (행 바꾸기)

print()

# 직각 삼각형 모양
for i in range (0,5):
    for j in range (0, i+1):
        print("$", end=' ')
    print()

print()

#역직각 삼각형 모양
for i in range (0,5):
    for j in range (0, 5-i):
        print("$", end=' ')
    print()

print()

#1씩 증가하는 숫자 넣기 
for i in range(0,5): 
    for j in range(1,6):
        num = (i * 5) + j
        print(num,"\t", end='')
    print() 

print()

