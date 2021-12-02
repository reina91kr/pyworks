#입력받아 파일쓰기

with open ('input.txt','a') as f:
    text = input("저장할 내용을 입력해 주세요.")
    f.write(text)
    f.write('\n')


    