#counter 클래스 만들기

class Counter:
#멤버변수
    def __init__(self):
        self.x = 0      # 시작을 0으로 초기화함
        self.x += 1     # 1 증가
#함수변수
    def getcount(self):
        return self.x

#인스턴스 변수
c1 = Counter()
print(c1.getcount()) #1

c2 = Counter()
print(c2.getcount()) #1

c3 = Counter()
print(c3.getcount()) #1