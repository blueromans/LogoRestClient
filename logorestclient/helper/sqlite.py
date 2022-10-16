import os
import sqlite3 as lite

from logorestclient.exceptions import LogoException

sql_path = f'{os.path.dirname(os.path.abspath(__file__))}/logo_rest.sqlite'


def initialize_sql_lite():
    try:
        with lite.connect(sql_path) as sqlite:
            cursor = sqlite.cursor()
            query = "CREATE TABLE IF NOT EXISTS jwt (token json)"
            cursor.execute(query)
            sqlite.commit()
    except Exception as e:
        raise LogoException(e)
