#Student 클래스를 외부에서 사용 (모듈)

from classli.student import Student # from 지정경로 import 클래스 이름

"""
s = Student ("김하나", 3)
print(s)
"""

s = [
    Student("김하나", 3),
    Student("이두울", 1),
    Student("박세엣", 2)
]
"""
print(s[1])
print(s[2])
"""

print("******* 학생 명단 *******")
for i in s:
    print(i)