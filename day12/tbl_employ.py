import sqlite3
def getconn():                                  #반복을 막기 위해 함수 활용 가능
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

def select_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")   #db 연결 시작 / 객체 생성
    conn = getconn()
    cur = conn.cursor()                         #db 작업(삽입, 삭제, 추가, 변경) 객체
    sql = "SELECT * FROM employee ORDER BY emp_id"  #오름차순 (ASC 생략됨)
    cur.execute(sql)                            #db 작업 실행 (검색)
    rs = cur.fetchall()                         #db 모든 자료 가져오기 (result set)
    # print(rs)
    for i in rs:
        print(i)
    conn.close()                                #db 연결 종료

def insert_emp():
    conn = getconn()                                                    #db 연결 객체 생성
    cur = conn.cursor()                                                 #db 작업 객체
    #입력방법 1 칼럼값을 직접 입력
    #sql = "INSERT INTO employee VALUES ('e1006','손흥민',30,50000)"      #data 추가
    #입력방법 2 * 더 많이 사용하는 방법
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"      #data 추가
    cur.execute(sql, ('e1002','추신수',34,40000))
    conn.commit()                                                       #커밋 실행 - 필수
    conn.close()                                                        #커밋 종료 - 필수

def select_one():
    conn = getconn()
    cur = conn.cursor()
    #방법 1
    #sql = "SELECT emp_id, name FROM employee WHERE salary = 40000"
    #방법 2
    sql = "SELECT name,salary FROM employee WHERE emp_id = ?"
    cur.execute(sql,('e1004',)) # 튜플이기 때문에 1개를 명시할 때 콤마(,) 명시해야 함
    rs = cur.fetchone()     #한명의 자료를 가져올때
    print(rs)
    conn.close()


def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age = ? WHERE emp_id = ? "
    cur.execute(sql, (33, 'e1005'))
    conn.commit()
    conn.close()

def del_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = ?"
    cur.execute(sql, ('e1004',))
    cur.execute(sql, ('e1006',))
    conn.commit()
    conn.close()

if __name__ =="__main__":
    #insert_emp()
    select_emp()
    # select_one()
    update_emp()
    # del_emp()


