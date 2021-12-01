#파일 읽어와서 랜덤하게 자료 읽기
import random as r

f = open("c:/web_dev/pyfile/season.txt", 'r')     #파일 읽기 모드는 'r'

word = f.read().split()        #전체를 split: 공백 구분
w = r.choice(word)                  #random하게 choice하라는 명령문
print(w)

f.close()