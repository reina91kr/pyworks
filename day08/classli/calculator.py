#계산기 클래스 정의

class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self. x += y #self.x = self.x + y
        return self.x

    def sub(self,y):
        self.x -= y
        return self.x

c = Calculator()
print(c.add(10)) #0 + 10 = 10
print(c.sub(5)) # 10 - 5 = 5