import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
# c.execute('SELECT * FROM {}'.format(input()))
c.execute("SELECT * FROM sqlite_master WHERE TYPE=='index'")
values = c.fetchall()
print(values)
conn.commit()
conn.close()