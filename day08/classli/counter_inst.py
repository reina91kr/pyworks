#counter 클래스 만들기

class Counter:
    def __init__(self):
        self.x = 0
        self.x += 1     # 1 증가

    def getcount(self):
        return self.x

c1 = Counter()
print(c1.getcount()) #1

c2 = Counter()
print(c2.getcount()) #2