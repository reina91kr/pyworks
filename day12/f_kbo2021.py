#2021kbo.txt만들기

with open('kbo2021.txt','w') as f:
    team = ['NC', '키움', '기아', '삼성', '두산', '롯데']

    #리스트를 파일에 쓰기
    for i in team:
        f.write(i + '\n')

