#거북이 대표 게임

#각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import turtle as t
import random as r

# t.shape('turtle') # 거북이 모양 바꾸기

"""  t 이동시키기 연습
t.up()  # 선 없애주기
#좌표 이동 함수 - t.goto(x,y)
t.goto(0, 200) # 좌표 위치 변경 / 단, 선이 나옴
t.goto(0, -200) 
t.goto(200, 0)
t.goto(-200, 0)
"""

#화살표 머리 각도 조정하는 함수 (설정)
def turn_up():  #위쪽 화살키를 누르면,
    t.left(2)   #머리각도가 왼쪽으로 2이동

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()   #거북이가 바라보는 각도 저장

    while t.ycor() > 0: #거북이의 y좌표(y-cordinator)가 0보면 크면(땅위에 있는 동안)
        t.forward(15) #앞으로 직진
        t.right(5) # 가면서 오른쪽으로 5도만큼 방향 바꾸기

    t.sety(r.randint(10, 100)) #성공 또는 실패 text를 표시할 위치 지정

    #while 반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target, 0) #거북이와 목표지점과의 거리
    if d < 25:
        t.color('blue')
        t.write("Good!", False, "center", ("", 13)) #명중했을 때 표시
        #글자쓰기 함수("문자열", 위치 이동 않음, 가운데정렬, 글꼴 크기)
    else:
        t.color('red')
        t.write("Bad!", False, "center", ("", 13))  # 실패패했을 때 표시
        t.color('black')
        t.goto(-200, 10) #처음 위치로 돌려보내기
        t.setheading(ang) # 처음 각도로 돌려보내기

#땅 그기
t.goto(-300, 0)
t.goto (300, 0)


#목표지점 만들기
target = r.randint(50, 150) #목표 지점은 50~150 사이의 임의의 수
t.color('green')
t.pensize(2)
t.up() #선 올리기
t.goto(target -25, 2)
t.down() # 선 내리기
t.goto(target +25, 2)

#거북이 초기 위치 설정
t.color('black')  #거북이를 검은색으로 변경
t.up()
t.goto(-200, 10)
t.setheading(20) #화살표 머리 각도

#화살표 머리 각도 조절하기 (동작)
t.onkeypress(turn_up, "Up") #위쪽 화살표 눌렀을 때 동작 실행
t.onkeypress(turn_down, "Down") #아래쪽 화살표 눌렀을 때 동작 실행
t.onkeypress(fire, "space") #발사함수 실행
t.listen() #키보드 연결하기

t.mainloop()

