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

def doTransaction(*commands, values=None):
    try:
        conn = connect()
        cur = conn.cursor()

        if values == None:
            for command in commands:
                cur.execute(command)
        else:
            for command, value in zip(commands, values):
                print(command, value)
                cur.execute(command, value)

        cur.close()
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def execute(command, value):
    doTransaction(command, values=[value])

def executeMany(command, values, fields: int):
    try:
        conn = connect()
        cur = conn.cursor()

        args_str = ','.join(cur.mogrify('(' + ','.join(['%s'] * fields) + ')', value).decode('utf-8') for value in values)
        cur.execute(command + ' ' + args_str)

        cur.close()
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
            

def fetchAll(command: str, value=None):
    try:
        conn = connect()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        if value == None:
            cur.execute(command)
        else:
            cur.execute(command, value)

        return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    finally:
        if conn:
            cur.close()
            conn.close()

def fetchOne(command: str, value):
    try:
        conn = connect()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute(command, value)

        return cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    finally:
        if conn:
            cur.close()
            conn.close()

def fetchById(command: str, id: int):
    return fetchOne(command + ' WHERE id = %s', [id])
