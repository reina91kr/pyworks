#파일 읽기

# readline = 첫줄로 불러오기
# readlines = list로 불러오기
import random as r

f = open("c:/web_dev/pyfile/season.txt", 'r')     #파일 읽기 모드는 'r'

season = f.readline()     #첫 줄 읽기
print(season)

seasons = f.readlines()     #전체 라인 읽기
print(seasons)

# readline, readlines 같이하면 첫 줄이 readlines에서 안 나옴

print(seasons[0])
print(seasons[-1])

# 전체 읽기
for seasons in seasons:
    print(seasons.strip())  #strip : 공백 제거


f.close()