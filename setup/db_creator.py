import sqlite3


def create_it():
    try:
        # connecting to the database
        connection = sqlite3.connect("redds_gallery.db")

        # cursor
        crsr = connection.cursor()

        # SQL command to create a table in the database
        sql_command = """CREATE TABLE gallery (
        painting_name VARCHAR(20) PRIMARY KEY,
        picture VARCHAR(100),
        description VARCHAR(150));"""

        # execute the statement
        crsr.execute(sql_command)

        # Save changes
        connection.commit()

        # close the connection
        connection.close()
    except Exception as e:
        print("Something went wrong in the process.")
        print(str(e))
