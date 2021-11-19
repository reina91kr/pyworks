year = int(input("연도를 입력하세요 : "))

#윤년은 4년마다 오고, & 100으로 나누어 떨어지지 않으나 400년으로 나누어 떨어지는 경우

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(str(year) + "년은 윤년입니다.")
else:
    print(str(year) + "년은 평년입니다.")
