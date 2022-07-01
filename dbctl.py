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
    CLASS INT NOT NULL,
    TOTAL INT NOT NULL,
    K INT NOT NULL,
    D INT NOT NULL,
    A INT NOT NULL,
    INRANK INT,
    OUTRANK INT);'''.format(self.name))
    def new_line(self, li):
        self.c.execute('INSERT INTO {} (CODE, CLASS, K, D, A, TOTAL) VALUES ({}, {})'.format(self.name, ','.join(li), sum(list(map(int, li[2:])))))
    def finish(self):
        classes = self.c.execute('SELECT DISTINCT CLASS FROM {}'.format(self.name)).fetchall()
        for i in classes:
            i = i[0]
            inrank = self.c.execute('SELECT ID FROM {} WHERE CLASS=={} ORDER BY TOTAL DESC'.format(self.name, i)).fetchall()
            for ii in range(len(inrank)):
                self.c.execute('UPDATE {} SET INRANK = {} WHERE ID=={}'.format(self.name, ii+1, inrank[ii][0]))
        outrank = self.c.execute('SELECT ID FROM {} ORDER BY TOTAL DESC'.format(self.name)).fetchall()
        for r in range(len(outrank)):
            self.c.execute('UPDATE {} SET OUTRANK = {} WHERE ID=={}'.format(self.name, r+1, outrank[r][0]))
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
