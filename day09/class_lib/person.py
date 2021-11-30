#Person 클래스

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {}, 나이 : {}".format(self.name, self.age)


if __name__ == "__main__": #자기 프로그램이 run할 때만 사용하도록 함
    p = Person("김하늘", 27)
    print(p)