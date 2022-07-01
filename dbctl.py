import sqlite3

class dbctl:
    def __init__(self, name):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        self.name = name
        print(name)
        self.c.execute('''CREATE TABLE {}
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODE INT NOT NULL UNIQUE,
    TOTAL INT NOT NULL,
    K INT NOT NULL,
    D INT NOT NULL,
    A INT NOT NULL);'''.format(self.name))
    def new_line(self, li):
        self.c.execute('INSERT INTO {} (CODE, K, D, A, TOTAL) VALUES ({}, {})'.format(self.name, ','.join(li), sum(list(map(int, li[1:])))))
    def finish(self):
        self.conn.commit()
        self.conn.close()

# password = '1'
# md5 =  hashlib.md5(password.encode('utf8')).hexdigest()
# conn = sqlite3.connect('test.db')

# c = conn.cursor()
# # c.execute('DELETE FROM SECURITY')
# # c.execute('INSERT INTO SECURITY (CODE, NAME, PASSWORD) VALUES (21377266, \'LUHUA\', \'FAQ\')')
# # c.execute('SELECT * FROM SECURITY')
# # values = c.fetchall()
# # print(values)

# c.execute('''CREATE TABLE SECURITY
#     (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     CODE INT NOT NULL UNIQUE,
#     NAME TEXT NOT NULL,
#     PASSWORD CHAR(32) NOT NULL,
#     TEACHER INT DEFAULT 0);''')
