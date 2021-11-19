#커피 자판기 프로그램
#커피 가격(money)가 400원, 커피 총 개수 (coffee) 5개,
#

coffee = 5
price = 400 
while True:
    money = int(input("돈을 입력하세요 : "))
    if money == price:
        print("커피가 나옵니다.")
        coffee -= 1
    elif money > price:
        print("거스름돈은", (money-price), "원 입니다")
        coffee -= 1
    else:
        print("돈이", (price-money), "원 부족합니다")
    print("남은 커피 양은 : ", coffee, "입니다.")

    if coffee  ==0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break
