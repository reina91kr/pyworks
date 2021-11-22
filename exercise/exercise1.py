#146
#1

a = "Life is too short, you need python"

if "wife" in a: print("wife")
if "python" in a and "you" not in a: print("python")
if "shirt" not in a: print("shirt")
if "need" in a: print("need")
else: print(none)

#2
result = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print("합 :", result)

#3
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i)

#4
for i in range (1, 101):
    print(i, end=" ")
print()

#5
score = [70, 60, 55, 75, 95, 90, 80, 90, 85, 100]
count = len(score)
avg = sum(score)/count

print("총 평균:", avg)

#6
numbers = [1,2,3,4,5]
result = []

for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

print("numbers :", numbers)
print("results :", result)




