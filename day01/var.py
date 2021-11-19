#변수 사용하기 - 주석은 # 사용 

print('***회원가입***')
userid='hangul'
userpw='han1234'
name = '한글'
phone = '010-1234-5678'
age = 35

"""
print('아이디 :', userid)
print('비밀번호 :', userpw)
print('이름 :', name)
print('전화번호 :', phone)
print('나이 :', age)

"""
#,를 사용한 경우 표기됐을 때에도 띄어쓰기가 1칸 있음
# +를 사용한 경우 띄어쓰기가 없음
#또, +의 경우 문자&숫자의 연결이 까다로움 

print('아이디 :'+ userid)
print('비밀번호 :' + userpw)
print('이름 :' + name)
print('전화번호 :' + phone)
print('나이 :'+ str(age))

print('=' * 30)


