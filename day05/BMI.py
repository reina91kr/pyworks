#연습문제
#BMI 계산하기

name = input("이름을 입력하세요.")
height = float(input("키(cm)를 입력하세요."))
weight = float(input("몸무게(kg)를 입력하세요"))
h_m = height/100

BMI = weight / (h_m * h_m)

print("{}의 BMI는 {:.1f} 입니다.".format(name, BMI))
print("%s님의 BMI는 %.2f입니다." % (name, BMI))

if BMI < 20:
    print("저체중입니다.")
elif BMI < 25:
    print("정상입니다.")
elif BMI < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")
