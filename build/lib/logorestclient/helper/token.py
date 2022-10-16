import os
import sqlite3 as lite

from logorestclient.exceptions import LogoException
from logorestclient.serializer import Serializer

sql_path = f'{os.path.dirname(os.path.abspath(__file__))}/logo_rest.sqlite'


def get_token():
    try:
        with lite.connect(sql_path) as sqlite:
            cursor = sqlite.cursor()
            query = """SELECT token FROM jwt"""
            cursor.execute(query)
            token_dict = cursor.fetchone()
            if token_dict is not None:
                token_dict = Serializer.loads(token_dict[0])
            return token_dict
    except Exception as e:
        raise LogoException(e)


def update_token(token):
    try:
        with lite.connect(sql_path) as sqlite:
            cursor = sqlite.cursor()
            query = "insert into jwt values (?)"
            cursor.execute(query, [Serializer.dumps(token)])
            sqlite.commit()
    except Exception as e:
        raise LogoException(e)
