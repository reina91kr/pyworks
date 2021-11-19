#if ~elif ~else 구문
#놀이공원 입장료 계산 프로그램

age = int(input("나이를 입력하세요 : "))
charge = 0
if age < 8:
    print("미취학 아동입니다.")
    charge = 1000
elif age < 14:
    print("초등학생입니다.")
    charge = 2000
elif age < 20:
    print("중고등학생입니다.")
    charge = 2500
else:
    print("일반인입니다.")
    charge = 3000


print("입장료는 "+ str(charge) + "입니다.")
