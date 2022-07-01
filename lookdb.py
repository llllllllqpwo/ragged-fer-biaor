import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('SELECT * FROM {}'.format(input()))
values = c.fetchall()
print(values)
conn.commit()
conn.close()