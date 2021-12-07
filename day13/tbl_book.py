#book 테이블 만들기
import sqlite3

def getconn():
    con = sqlite3.connect("./output/sample.db")
    return con

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no     INTEGER     PRIMARY KEY         AUTOINCREMENT,
        title       TEXT        NOT NULL,  
        publisher   TEXT        NOT NULL, 
        page        INTEGER
    ) 
    """
    #AUTOINCREMENT - 자동 순번 (sequence)
    cur.execute(sql)
    conn.commit()
    print("book 테이블 생성")
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES ('웹 표준의 정석', '고경희', 600)"
    cur.execute(sql)
    conn.commit()
    conn.close()

#AUTOINCREMENT이기 때문에 맨 앞에 숫자 넣어주지 않음

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    rs = cur.fetchall()     #리스트로 변환
    # print(rs)               #리스트로 출력
    for i in rs :
        print(i)
    conn.close()

def del_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM book"
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('웹 표준의 정석', '고경희', 600))
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"        #책 번호로 검색
    cur.execute(sql, (1,))
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE book SET title =?, publisher = ?, page = ? WHERE book_no =? "
    cur.execute(sql, ("점프 투 파이썬2", "김명석", 500, 5))
    conn.commit()
    conn.close()

if __name__=="__main__":
    # create_table()
    insert_book()
    # del_book()
    # insert_book()
    select_book()
    # select_one()
    # update_book()


