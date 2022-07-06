import psycopg2
from psycopg2.extras import RealDictCursor

USER = 'postgres'
PASSWORD = 'mysecretpossword'
HOST = 'postgres'
PORT = 5432
DATABASE = 'postgres'

def connect():
    try:
        return psycopg2.connect(host=HOST, port=PORT, user=USER, password=PASSWORD)
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def doTransaction(*commands, values:list=None):
    try:
        conn = connect()
        cur = conn.cursor()

        if values == None:
            for command in commands:
                cur.execute(command)
        else:
            for command, value in zip(commands, values):
                cur.execute(command, value)

        cur.close()
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def insert(command, value: tuple):
    doTransaction(command, values=[value])
            

def fetch(command: str):
    try:
        conn = connect()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute(command)

        return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    finally:
        if conn:
            cur.close()
            conn.close()
