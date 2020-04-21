import psycopg2
import os

def get_connection():

    return psycopg2.connect(dsn='postgresql://test01:test01@localhost:15432/test01')


def select_all():

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    data_llist = cur.fetchall()
    key =['user_id','pass','user_name','regist_date','update_date']

    for data in data_llist:
        print(dict(zip(key, data)))
    print('*******')

