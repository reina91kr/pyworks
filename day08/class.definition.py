#클래스
#멤버변수 = 명사
#함수변수 = 동사
# 명사가 동사한다 와 같이 사용

class Student:
    def __init__(self): #항상 사용해야 함
        self.name = "콩쥐"
        self.grade = 1
        print("생성자 함수")
    def learn(self):
        print("수업을 듣습니다.")

Student()