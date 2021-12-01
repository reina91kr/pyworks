#예외처리(exception 클래스)

try:
    x = int(input("숫자를 입력하세요 :"))
    print(x)            #ValueError

except ValueError:      #ValueError (as e) 클래스 생성 (생략 가능)
    print("유효한 숫자가 아닙니다. 숫자를 입력해 주세요.")
