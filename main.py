import pymysql
from config import host, user, password, db_name
import pymysql.cursors
import mysql.connector

Connection = pymysql.connect(
    host='127.0.0.1',
    user= 'root',
    passwd= 'root',
    database='db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )

mycursor = Connection.cursor()

""" mycursor.execute('CREATE DATABASE users') """

""" mycursor.execute('SHOW DATABASES')
for db in mycursor:
    print(db) """

    