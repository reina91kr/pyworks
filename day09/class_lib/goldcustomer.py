#Gold Customer 클래스 정의
from day09.class_lib.customer import Customer

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid,name)
        self.cgrade = "GOLD"
        self.bonus_ratio = 0.02
        self.sale_ratio = 0.1

    def calc_price(self, price):
        self.bonus_point += int(self.bonus_ratio * price)
        price -= int(self.sale_ratio * price)
        return price

    # def __str__(self):
    #     return "{}님의 등급은 {}이고, 보너스 포인트는 {}점, 할인된 가격은 {}입니다.".format(self.name, self.cgrade, self.bonus_point, self.price)
    #
