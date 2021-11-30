#employee() 클래스

from day09.class_lib.person import Person

class Employee(Person): #아무것도 안할땐 pass 사용
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)   #부모 멤버 super()함수로 명시
        self.employeeID = employeeID  #자기 멤버 초기화
    def __str__(self): #부모 __str__()함수 상속 - 재정의 (overriding)
        return super().__str__() + ", 사번: {}".format(self.employeeID)

e = Employee("이강", 25, 101)

print(e)
print("이름 : " + e.name) #부모 멤버에 접근 가능
print("나이 : " + str(e.age))
print("사번 : " + str(e.employeeID))
