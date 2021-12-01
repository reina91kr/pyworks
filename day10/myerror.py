#예외 만들기
#Exception 클래스를 상속받아야 함

class MyError(Exception):
    #pass
    def __str__(self):
        return "허용되지 않는 별명입니다."   #2. 에러가 불러들여짐

def say_nick(nick):
    if nick == '바보' or nick == '칠푼이':
        raise MyError()    # 1. 에러를 발생시킴
    print(nick)

try:                        #3 에러를 처리해줌
    say_nick('영웅')
    say_nick('바보')           # 여기서 에러가 나기 때문에 "허용되지 않는 별명입니다"는 1번만 표시됨
    say_nick('칠푼이')

except MyError as e:
    print(e)