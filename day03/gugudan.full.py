#구구단 전체 출력

# dan = 4
# for i in range (1,10):
#     print(dan*i)

for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', (j*i))
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print(j*i, end=" ")
    print()