# 웹 서버 만들기

from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
# @ 애너테이션 - 프로그램을 넣어준다 '/'는 루트 경로를 의미 / 루트 경로, ip = 127.0.0.1:5000
def index():
    # return "<h1>Hello ~ Flask</h1>"
    return render_template('index.html') #html 파일을 불러들인것

@app.route("/register/", methods=['GET', 'POST'])
def register():
    #POST방식 : 클라이언트에서 서버로 리소스를 생성하거나 업데이트하기 위해 보낼때 사용 (보안이나 용량이 큰 경우 사용)
    if request.method == 'POST':            #POST 방식 : 보안 자료
        id = request.form ['id']            #HTML의 id값을 파이썬의 id로 설정
        name = request.form['name']
        pwd = request.form['passwd']

        return render_template('member_info.html', id=id, name=name, pwd=pwd)
            #다시 파이썬의 id를 다를 HTML로 보냄
    else:
        return render_template('register.html') #GET방식 (클라이언테어 서버로 정보를 요청) / 하이퍼링크

@app.route("/loop_index/")
def get_loopindex():
    items = ['a','b','c','d']
    return render_template('loop_index.html', items=items)


app.run(debug=True)     #개발중임을 표시 / 서비스 할 때 False로 변경해야 함
