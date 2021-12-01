#with ~ as 사용 - f.close 사용 x
#구구단 파일 쓰기

with open('99.txt', 'w') as f:       #상대경로  as 객체 이름 붙이기 * 같은 폴더에 저장됨
    dan = 4
    for i in range (1, 10):
        f.write("%d x %d = %d \n" % (dan, i, i*dan))
    f.write("\n")

with open('99.txt', 'a') as f:       #추가할 땐 'a'
    dan = 5
    for i in range(1, 10):
        f.write("%d x %d = %d \n" % (dan, i, i * dan))
    f.write("\n")

with open('99total.txt', 'w') as f:       #상대경로  as 객체 이름 붙이기 * 같은 폴더에 저장됨
    for dan in range (2,10):
        for i in range (1, 10):
            f.write("%d x %d = %d \n" % (dan, i, i*dan))
        f.write("\n")

