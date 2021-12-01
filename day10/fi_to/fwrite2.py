#파일 쓰기

f=open("c:/web_Dev/pyfile/file_num.txt",'w')
f.write("%d\n" % 45)
f.write("%.2f\n" % 12.34)
f.write("%d\n" % (45+1))

times = "%d x %d = %d" % (3,4,12)   # 변수 생성도 가능
f.write(times + "\n")

i = 3
j = 4
times = "%d x %d = %d" % (i, j, i*j)
f.write(times + "\n")

f.close() #파일 닫기