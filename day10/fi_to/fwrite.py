#파일 쓰기

f=open("c:/web_Dev/pyfile/file.txt",'w')        #("경로", 모드) * 쓰기모드 = 'w'
f.write("하늘이 파랗다.\n")     #파이썬은 편리한게 한글, 영문, 한자가 다 구분되어서 들어감
f.write("Thank you!\n")
f.write("社員\n")
f.write("45\n") #f.write는 str만 사용 가능

f.close() #파일 닫기