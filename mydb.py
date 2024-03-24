import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    auth_plugin='mysql_native_password',
)

cursor=dataBase.cursor()
cursor.execute('CREATE DATABASE UserData')
print('Data base created!!!')