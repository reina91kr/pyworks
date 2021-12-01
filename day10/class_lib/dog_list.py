#Dog 클래스 만들기

#동시에 여러 객체에게 추가됨

# class Dog:
#     tricks = []  #클래스 리스트
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_trick(self, trick): #추가하기
#         self.tricks.append(trick)
#
#
# dog1 = Dog("Elsa")
# dog2 = Dog("Fido")
# dog1.add_trick("play dead")
# dog2.add_trick("roll over")
# print(dog1.tricks)
# print(dog2.tricks)

#개별 객체에게 지정해줄때

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog2 = Dog("Fido")

dog1.add_trick("play dead")
dog2.add_trick("roll over")

print(dog1.tricks)
print(dog2.tricks) 