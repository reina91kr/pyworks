#Student 클래스 만들기
#클래스는 self 키워드를 사용
#def init() - 생성자(constructor) 함수 사용

class Student:
    def __init__(self):
        self.name = "콩쥐" #멤버 변수
        self.grade = 1
        print("생성자 함수입니다.") #우선되는 명령

    def learn(self):
        return "수업을 듣습니다."

s = Student()  #Student 클래스의 객체(instance) s 생성
print("이름 : " + s.name)
print("학년 : " + str(s.grade))
print(s.learn())