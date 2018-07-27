"""
The backend that is tied to the redds gallery app
get_desc gets the description
get_pic gets the picture

written by: Matthew Lopez
"""
import sqlite3


def get_desc(title):
    """
    Getting the description from the database from the title that was passed in
    :param title: the (PRIMARY KEY) to find
    :return: new_desc, the description from the title
    """
    connection = sqlite3.connect("setup/redds_gallery.db")
    crsr = connection.cursor()
    crsr.execute("SELECT description FROM gallery WHERE painting_name=?", (title,))
    new_desc = crsr.fetchall()
    connection.close()
    return new_desc


def get_pic(title):
    """
    Find the picture tied to the title passed in
    :param title: the (PRIMARY KEY) to find the picture
    :return: pic_file, the picture that needs to be sent back
    """

    connection = sqlite3.connect("setup/redds_gallery.db")
    crsr = connection.cursor()
    crsr.execute("SELECT picture FROM gallery WHERE painting_name=?", (title,))
    pic_file = crsr.fetchall()
    connection.close()
    return pic_file
