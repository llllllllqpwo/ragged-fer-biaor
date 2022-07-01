import sqlite3, hashlib

password = '1'
md5 =  hashlib.md5(password.encode('utf8')).hexdigest()
conn = sqlite3.connect('test.db')

c = conn.cursor()
# c.execute('DELETE FROM SECURITY')
# c.execute('INSERT INTO SECURITY (CODE, NAME, PASSWORD) VALUES (21377266, \'LUHUA\', \'FAQ\')')
# c.execute('SELECT * FROM SECURITY')
values = c.fetchall()
print(values)

c.execute('''CREATE TABLE SECURITY
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CODE INT NOT NULL UNIQUE,
    NAME TEXT NOT NULL,
    PASSWORD CHAR(32) NOT NULL,
    TEACHER INT DEFAULT 0);''')

conn.commit()
conn.close()