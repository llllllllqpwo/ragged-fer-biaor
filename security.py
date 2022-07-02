import sqlite3

class security():
    def __init__(self):
        # password = '1'
# md5 =  hashlib.md5(password.encode('utf8')).hexdigest()
        self.conn = sqlite3.connect('test.db')

        self.c = self.conn.cursor()
# c.execute('DELETE FROM SECURITY')
# c.execute('INSERT INTO SECURITY (CODE, NAME, PASSWORD) VALUES (21377266, \'LUHUA\', \'FAQ\')')
# c.execute('SELECT * FROM SECURITY')
        # values = self.c.fetchall()
        # print(values)

        # self.c.execute('''CREATE TABLE SECURITY
        #     (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        #     CODE INT NOT NULL UNIQUE,
        #     NAME TEXT NOT NULL,
        #     PASSWORD CHAR(32) NOT NULL,
        #     TEACHER INT DEFAULT 0);''')
    def finish(self):
        self.conn.commit()
        self.conn.close()
    
    def login(self, user, pw, iden):
        pwresult = self.c.execute('SELECT PASSWORD FROM SECURITY WHERE CODE=={} AND TEACHER=={}'.format(user, iden)).fetchall()
        if len(pwresult):
            if len(pwresult[0]):
                return pwresult[0][0]==pw
        else:
            return 0
