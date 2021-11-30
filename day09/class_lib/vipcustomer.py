#VIP Customer 클래스 생성하기
from day09.class_lib.customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.cgrade = "VIP"
        self.agent = agent
        self.bonus_point = 0
        self.bonus_ratio = 0.05
        self.sale_ratio = 0.1

    def calc_price(self, price):
        price -= int(price*self.sale_ratio)
        self.bonus_point = int(price*self.bonus_ratio)
        return price

    def __str__(self):
        return super().__str__() + "\n 전문 상담원 ID는 {}입니다.".format(self.agent)