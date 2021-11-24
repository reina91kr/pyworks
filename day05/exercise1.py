#연습문제
#1

score = [80, 75, 55]

avg = sum(score)/len(score)

print(avg)

#2
n = 13

if n % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#3
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print(yymmdd)
print(num)

#4
pin = "881120-1068234"
gender = int(pin[7:8])
print(gender)
if gender == 1:
    print("남성입니다.")
else:
    print("여성입니다.")

#5
a = "a:b:c:d"
b = a.replace(a, "a#b#c#d")
print(b)

#6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#8
a = (1, 2, 3)
a = a + (4,)
print(a)

#10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b = [1, 2, 3]
a[1] = 4
print(b)
print(a)
