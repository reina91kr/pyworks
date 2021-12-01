#1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

# cal = Calculator()
# cal.add(10)

class UpgradeCalculator(Calculator):
    # def __init__(self):  추가되는 변수가 없을 땐 안 해도 됨
    #     super().__init__()

    def minus(self,val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#2

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
            return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

