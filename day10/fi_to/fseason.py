#파일에 리스트 자료 구조 저장하기

season = ['봄', '여름', '가을', '겨울']

f = open("c:/web_dev/pyfile/season.txt", 'w')
for i in season:
    f.write(i + "\n")

f.close()

try:
    f = open("c:/web_dev/pyfile/season.txt", 'r')
    season = f.read()
    print(season)

except FileNotFoundError:
    print('파일을 열 수 없습니다.')
