import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="mysecretpossword", host="127.0.0.1", port="5432", database="postgres")

    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM test")
    print(cursor.fetchall())
except:
    print("error")
