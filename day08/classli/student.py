#생성자(cosntructor)
class Student:
    def __init__(self, name, grade):
        self.name = name # 외부에서 name을 가져오는 것
        self.grade = grade

    def __str__(self):
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)
s1 = Student("콩쥐", 1)
print(s1)

s2 = Student("팥쥐", 2)
print(s2)