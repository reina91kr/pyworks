#구구단 함수 정의

def print_gugu(dan):
    for i in range (1, 10):
        x = dan * i
        print("%d x %d = %d" % (dan, i, x))

print_gugu(6)