from class_lib.customer import Customer
from class_lib.goldcustomer import GoldCustomer
from day09.class_lib.vipcustomer import VIPCustomer


#객체 생성
c = Customer(101, "놀부")
g = GoldCustomer(201, "흥부")
v = VIPCustomer(301, "제비", 1004)

#구입내역
cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(20000)

#제품 지불 비용 출력
print("{}님의 지불비용은 {}원 입니다.".format(c.getname(), cost_c))
print("{}님의 지불비용은 {}원 입니다.".format(g.getname(), cost_g))
print("{}님의 지불비용은 {}원 입니다.".format(v.getname(), cost_g))

#객체 정보
print(c)
print(g)
print(v)
