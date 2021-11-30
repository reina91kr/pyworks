#Person 클래스 만들기
#접근제한 방법 : - 변수 이름 앞에 _(underscore)를 1개, 2개를 붙임
#속성이 private으로 바뀜
#접근 방법 - get + 변수이름, set + 변수이름()

class Person:
    def __init__(self):
        self._name = ""  #멤버 변수 초기화, 접근제한
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name

    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age

p1 = Person()
p1.setname("김하늘")
print(p1.getname())

p1.setage(25)
print(p1.getage())
    