#예외처리 미루기

#1.

# class Animal:
#     def cry(self):
#         print('소리를 낸다')
#
# class Dog(Animal):
#     pass
#
# dog = Dog()
# dog.cry()
#

#2
#새로운 객체가 추가되었는데, 같은 내용이 나옴

# class Animal:
#     def cry(self):
#         # print('소리를 낸다')
#         raise NotImplementedError  # 구현하지 않으면 에러 발생
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass

# dog = Dog()
# cat = Cat()
# dog.cry()
# cat.cry()

# 더이상 pass를 사용해서 넘길 수 없게 됨 / 무조건 만들어줘야 함

#3
#raise 사용

class Animal:
    def cry(self):
        raise NotImplementedError

class Dog(Animal):
    def cry(self):
        print("왈~ 왈~")

class Cat(Animal):
    def cry(self):
        print("야옹~야옹~")

dog = Dog()
cat = Cat()
dog.cry()
cat.cry()