#배송비 계산하기
#상품 가격이 20000원 미만이면 배송비 2500원 포함하고
#아니면 배송비 미포함
def get_price(unit_price,quantity):
    delivery_fee = 2500
    price = unit_price * quantity
    if price < 20000:
        price += delivery_fee
    return price

price1 = get_price(15000, 2)
print("상품1 가격: " + format(price1, ",") + "원 입니다")
price2 = get_price(5000,3)
print("상품1 가격: " + format(price2, ",")+ "원 입니다")

#format(n,",") = 1000단위에 ,넣기
#format(n,",d")로도 가능