# 홑따옴표, 쌍따옴표로 감싸서 문자열을 표기
say ="'힘내세요!'라고 말했습니다."
print(say)


#여러 줄 입력하기

song1 = """
동해물과 백두산이\n 마르고 닳도록
하느님이 보우하사 우리나라 만세

남산 위에 저 소나무 철갑을 두른 듯
바람서리 불변함은 우리 기상일세
"""

print(song1)
print('-'*40)

#이스케이프 문자
table = """
이름\t나이\t지역
김화성\t21\t화성
이옥성\t31\t옥성
"""

print(table)

'''
\n = 줄바꿈 (br)
\t = 테이블 + 선맞추기
'''

head = 'Python'
tail = " is fun!"
print(head + tail)
print(head*2)
