import sqlite3
import logging

conn = sqlite3.connect("../sqlite_database/missing_masterpieces_db.db")


def create_miss_pieces_table():
    try:
        conn.execute(
            """CREATE TABLE MISS_PIECES (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            CREATION INT NOT NULL,
            CREATOR CHAR(50),
            LOST INT,
            URL TEXT);"""
        )

    except Exception as e:
        logging.warning(f"Table alreayd exists: {e}")


def add_piece():
    try:
        conn.execute(
            f"INSERT INTO MISS_PIECES (ID,NAME,CREATION,CREATOR,LOST, URL) VALUES (1, \
            'Chez Tortoni', \
            1875, \
            'Manet', \
            1990, \
            'https://upload.wikimedia.org/wikipedia/commons/f/f3/Rembrandt_Christ_in_the_Storm_on_the_Lake_of_Galilee.jpg')"
        )

        conn.execute(
            "INSERT INTO MISS_PIECES (ID,NAME,CREATION,CREATOR,LOST, URL) VALUES (2, 'Le Christ dans la tempête sur la mer de Galilée', 1633, 'Rembrandt', 1990, 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Rembrandt_Christ_in_the_Storm_on_the_Lake_of_Galilee.jpg')"
        )
    except Exception as e:
        print(f"Problem while adding piece: {e}")


# add_piece()
conn.commit()

cursor = conn.execute("SELECT id, name, creation, creator, lost from MISS_PIECES")
print(cursor)
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("CREATED = ", row[2])
    print("CREATOR = ", row[3])
    print("LOST = ", row[4])

conn.close()
