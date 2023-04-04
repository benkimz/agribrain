import os
import sqlite3
from unittest import result

from agscripts.passwords import password_hash

SQL_DIR = "./database/sql/"
DBS_DIR = "./database/"
DEFAULT_DB = "{}agribrain.db".format(DBS_DIR)

def sql_parser(script_name: str):
    sql_path = os.path.join(SQL_DIR, f"{script_name}.sql")
    assert os.path.exists(sql_path), "SQL script does not exit"
    with open(sql_path, mode="r", encoding="utf-8") as rctx:
        sql = rctx.read()
    return sql

class UserEntry:
    def __init__(self, username, location, useremail, password):
        self.username = username
        self.location = location
        self.useremail = useremail
        self.password = password
        self.conn = sqlite3.connect(DEFAULT_DB)
        self.cursor = self.conn.cursor()

        self._create_table_if_not_exists()
        self._save_user()

    def _create_table_if_not_exists(self):
        self.cursor.execute(sql_parser("users"))
        self.conn.commit()

    def _save_user(self):
        query = """
                    INSERT INTO users (
                        username, 
                        location, 
                        useremail, 
                        password
                    ) VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(query, 
                            (self.username, self.location, self.useremail, self.password))
        self.conn.commit()
        
def user_info(useremail: str):
    try:
        conn = sqlite3.connect(DEFAULT_DB)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT username, location, useremail, password 
            FROM users WHERE useremail='{}'
            """.format(useremail))
        result = cursor.fetchone()
        if result:
            return result
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()
      
      
class RemoteCollection:
    def __init__(self, arc_name, chair, location, farmers_capacity, products) -> None:
        self.arc_name = arc_name
        self.chair = chair 
        self.location = location
        self.farmers_capacity = farmers_capacity
        self.products = products
        self.conn = sqlite3.connect(DEFAULT_DB)
        self.cursor = self.conn.cursor()
        
        self._create_table_if_not_exists()
        self._save_arc()
        
    def _create_table_if_not_exists(self):
        self.cursor.execute(sql_parser("arcs"))
        self.conn.commit()  
        
    def _save_arc(self):
        query = """
                    INSERT INTO arcs (
                        arcname, 
                        location, 
                        chair, 
                        capacity, 
                        products
                    ) VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(query, 
                            (
                                self.arc_name, 
                                self.location, 
                                self.chair, 
                                self.farmers_capacity, 
                                self.products
                            ))
        self.conn.commit()      
        
def fetch_arcs():
    try:
        conn = sqlite3.connect(DEFAULT_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM arcs")
        results = cursor.fetchall()
        if results:
            return results
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()        