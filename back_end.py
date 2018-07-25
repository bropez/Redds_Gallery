import sqlite3


def get_desc(title):
    connection = sqlite3.connect("setup/redds_gallery.db")
    crsr = connection.cursor()
    crsr.execute("SELECT description FROM gallery WHERE painting_name=?", (title,))
    new_desc = crsr.fetchall()
    connection.close()
    return new_desc