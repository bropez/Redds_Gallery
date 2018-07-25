import sqlite3

connection = sqlite3.connect('setup/redds_gallery.db')
crsr = connection.cursor()
crsr.execute("SELECT * FROM gallery")
ans = crsr.fetchall()
for i in ans:
    print(i)