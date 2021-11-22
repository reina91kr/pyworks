#리스트의 생성 및 관리

#정수형 리스트 생성 및 초기화
numbers=[10, 20, 30, 40]

#요소를 추가
numbers.append(50)
print(numbers)
print(type(numbers))

#요소 수정
numbers[1]=60
print(numbers)

#요소 삭제
# del numbers[2]
# ↑명령어로 삭제
# ↓함수로 삭제
# numbers.pop(2)
# ↓특정 요소 삭제
numbers.remove(40)
print(numbers)

#중간에 넣기 000.insert(위치, 넣을 숫자)
numbers.insert(1, 70)
print(numbers)

#요소의 개수
print(len(numbers))

#for ~ in 문
for i in numbers:
    print(i, end = ' ')
print()

#for ~ range문
n = len(numbers)
for i in range(0, n):
    print(numbers[i], end = ' ')
print()