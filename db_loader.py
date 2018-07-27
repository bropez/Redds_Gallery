"""
Created to load the db that was created from db_creator
load_it loads the db with information from out2.csv

written by: Matthew Lopez
"""

import csv
import sqlite3


def load_it():
    """
    A method to fill the redds_gallery.db with information from out2.csv
    :return: none
    """
    # connect to the database
    connection = sqlite3.connect("redds_gallery.db")

    # cursor
    crsr = connection.cursor()

    with open('out2.csv') as csvfile:
        content_reader = csv.reader(csvfile)
        # what the command should look like
        # """INSERT INTO gallery VALUES (row[1], row[0], row[2]);"""
        for row in content_reader:
            if not row:
                pass
            else:
                crsr.execute("INSERT INTO gallery VALUES (?, ?, ?)", (row[1], row[0], row[2]))

    connection.commit()
    connection.close()