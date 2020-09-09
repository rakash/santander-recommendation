import psycopg2
import os
from flask import Flask, request, make_response, jsonify
from sqlalchemy import select, Table , MetaData, text, create_engine
from flask_sqlalchemy import SQLAlchemy 
import numpy as np 
import sklearn
import _compat_pickle
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

app = Flask(__name__)
metadata = MetaData()

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
#db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
#cloud_sql_connection_name = os.environ.get['CLOUD_SQL_CONNECTION_NAME']

db = SQLAlchemy(app)

def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)
    return conn

def get_songs():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    #if os.environ.get('GAE_ENV') == 'standard':
    conn = pymysql.connect(#host='127.0.0.1',
                           #port=3306, 
                           user=db_user, 
                           password=db_password,
                           #unix_socket=unix_socket, 
                           db=db_name
                           #cursorclass=pymysql.cursors.DictCursor
                        )
    #conn = open_connection()
       
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM songs;')
        songs = cursor.fetchall()
        if result > 0:
            got_songs = jsonify(songs)
        else:
            got_songs = 'No Songs in DB'
    conn.close()
    return got_songs

def getCustomerDetails(id):
    DATABASE_URI= ''
    
    engine=create_engine(DATABASE_URI)
    connection=engine.connect()
       
    test = Table('test', metadata, autoload=True, autoload_with=engine)
    stmt_cc = select([test.c.age, test.c.sex_f])
    stmt=select([test])
    try:
        stmt=stmt.where(test.columns.id == id)
        results = connection.execute(stmt).fetchall()
    except NoResultFound:# as e:
        #print(e)
        raise('The specified item could not be found.')
        
    lst = []
    for row in results:
        for i in range(len(row)):
            lst.append(row[i])

    lst_final = []
    lst_final.append(lst)
    #aa = np.array(lst_final)
    return lst_final
    connection.close()


print(getCustomerDetails(1))
