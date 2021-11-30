#클래스 변수
class Counter:
    x = 0   #클래스 변수(self를 사용하지 않음)

    def __init__(self):
        Counter.x += 1  #클래수 변수이므로 클래스 이름으로 직접 입력

    def getcount(self):
        return self.x

c1 = Counter()
print(c1.getcount()) #1

c2 = Counter()
print(c2.getcount()) #2

c3 = Counter()
print(c3.getcount()) #3