import sqlite3
import logging
import pandas as pd


class database_manager:
    def __init__(self):
        self.conn = sqlite3.connect("../../sqlite_database/missing_masterpieces_db.db")

    def create_miss_pieces_table_from_raw_csv(self):
        try:
            self.conn.execute(
                """CREATE TABLE MISS_PIECES (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                CREATION INT NOT NULL,
                AUTHOR CHAR(50),
                LOST INT NOT NULL,
                URL TEXT);"""
            )
        except Exception as e:
            logging.info(f"Table already exists: {e}")
        try:
            self.add_piece_from_raw_csv()
            self.conn.commit()
        except Exception as e:
            logging.warning(f"Fail to load records: {e}")
        self.conn.close()

    def add_piece_from_raw_csv(self):
        df = pd.read_csv("raw_pieces.csv")
        for index, row in df.iterrows():
            try:
                self.conn.execute(
                    f"INSERT INTO MISS_PIECES (ID,NAME,CREATION,AUTHOR,LOST,URL) VALUES ({row['piece_id']}, \
                    '{row['name']}', \
                    {row['created']}, \
                    '{row['author']}', \
                    {row['lost']},\
                    '{row['url']}')"
                )
            except Exception as e:
                logging.info(f"Piece probably exists: {e}")

    def get_all_records(self):
        cursor = self.conn.execute(
            f"SELECT id, name, creation, author, lost, url from MISS_PIECES"
        )
        pieces_dico = list()
        for row in cursor:
            pieces_dico.append(
                {
                    "piece_id": row[0],
                    "name": row[1],
                    "author": row[3],
                    "creation_date": row[2],
                    "lost_date": row[4],
                    "url": row[5],
                }
            )

        self.conn.close()
        return pieces_dico
