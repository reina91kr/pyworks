#while ~ break문
"""
i = 0
while True:
    i += 1 # i++가 없음 
    if i > 10:  #if문이 11(false)일때 break 
        break

    print(i)
"""

#키가 'y'이면, "계속 반복", 'n'이면 반복 중단, 그 외의 키는 "정상 답변이 아닙"
"""
key = input("키: ")

if key =="y" and "Y":
    print("계속 반복")
elif key == "n" and "N":
    print("반복 중단")
else:
    print("정상 답변이 아닙니다.")
"""

key = input("키: ")

while True:
    if key =="y" and "Y":
        key = input("키 : ")
    elif key != ("y" or "n"):
        print("정상 답변이 아닙니다.")
        key = input("키 : ")

    if key == "n" and "N":
        break

