#If 조건문
age = int(input("나이를 입력하세요 : "))
print("나이는 ", age, " 입니다.")

if age < 8:
    print ("학교에 갈 나이가 아닙니다.")

elif age >= 8 and age < 13:
    print("초등학교에 갈 나이입니다.")

elif age >=13 and age < 17 :
    print("중학교에 갈 나이입니다.")

elif age >=17 and age < 20 :
    print("고등학교에 갈 나이입니다.")
    
else :
    print("성인입니다.")

print('-'*40)

#if ~else 구문
speed = int(input("속도를 입력하세요 : "))
if speed > 50:
    print("속도 위반, 과태료 10만원")
else:
    print("안전속도 준수")
