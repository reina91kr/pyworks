#112
#1
# name = input("이름을 입력하세요")
# score1 = int(input("국어 점수를 입력하세요"))
# score2 = int(input("영어 점수를 입력하세요"))
# score3 = int(input("수학 점수를 입력하세요"))
# score = [score1, score2, score3]
#
# avg = sum(score)/len(score)
# print(name, "님의 평균점수는", avg, "점 입니다.")
#
# #2
# n = int(input("숫자를 입력하세요"))
#
# if n % 2 == 0: print ("짝수입니다.")
# else: print("홀수입니다.")

#3 주민등록번호 분석하기
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin [7:]
print("19" + yymmdd)
print(num)

#생년월일로 표기
name = input("이름을 입력하세요")
pin = input("주민등록번호를 입력하세요.")

yy = pin[:2]
mm = pin[2:4]
dd = pin[4:6]
sex = pin[7:8]

print("19"+str(yy)+"년")
print(str(mm)+"월")
print(str(dd)+"일")

print(name,"님은 ", "19"+str(yy)+"년", str(mm)+"월", str(dd)+"일", "에 태어났습니다.")

if sex == 1 or sex == 3:
    print(name, "님은", "남성입니다.")
elif sex == 2 or sex == 4: print(name,"님은", "여성입니다.")