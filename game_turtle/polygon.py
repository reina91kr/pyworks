# 다각형 그리기
import turtle as t

def polygon(n):    # n - 변의 수
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d): # d - 거리
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)  #도형 호출 (실행)
polygon(5)

t.up()          #선 올리기 (선 안보이게 하는 것)
t.forward(100)
t.down()        #선 내리기 (선이 다시 보이게 하는 것)

polygon2(3, 100)
polygon2(5, 100)


t.mainloop()
