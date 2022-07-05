import psycopg2

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

def doTransaction(*commands):
    try:
        conn = connect()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
            

def fetch(command: str):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(command)
        records = cur.fetchall()

        print('record print')
        print(records)

        return records
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    finally:
        if conn:
            cur.close()
            conn.close()
