#자리 배치 프로그램

#고객수 / 열(좌석) = 행(줄)의  갯수를 구해서 for문으로 배치

cust = int(input("고객 수를 입력하세요 : "))
col = int(input("열의 수를 입력하세요 : "))
row = int(cust / col) #몫

#나머지가 있는 경우와 없는 경우
if (cust % col) == 0:
    row = cust//col
else:
    row = cust//col+1
    
    for i in range (0,row):
        for j in range (1, col+1):
            seat = i * col + j
            if seat > cust:
                break
            print("좌석" + str(seat), end='')
        print()

        print()
        




