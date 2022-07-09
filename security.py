import sqlite3

class security():
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        #连接数据库

    def finish(self):
        self.conn.commit()
        self.conn.close()
        #调用结束后关闭数据库连接
    
    def login(self, user, pw, iden):
        pwresult = self.c.execute('SELECT PASSWORD FROM SECURITY WHERE CODE=={} AND TEACHER=={}'.format(user, iden)).fetchall()
        if len(pwresult):
            if len(pwresult[0]):
                return pwresult[0][0]==pw
        else:
            return 0
