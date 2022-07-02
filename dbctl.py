import sqlite3

class dbctl:
    def __init__(self, name):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        self.name = name
        self.c.execute('''CREATE TABLE {}
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODE INT NOT NULL UNIQUE,
    CLASS INT NOT NULL,
    INRANK INT,
    OUTRANK INT,
    TOTAL INT NOT NULL,
    K INT NOT NULL,
    D INT NOT NULL,
    A INT NOT NULL);'''.format(self.name))
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

class dbrqt:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        self.fresh_exams = self.c.execute("SELECT * FROM sqlite_master WHERE TYPE=='index'").fetchall()
        self.exams = []
        for i in self.fresh_exams:
            self.exams.append(i[2])
        self.exams.remove('SECURITY')

    def search(self, exam, code):
        return self.c.execute('SELECT INRANK, OUTRANK, TOTAL, K, D, A FROM {} WHERE CODE=={}'.format(exam, code)).fetchall()
