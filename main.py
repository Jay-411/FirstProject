import config
import mysql.connector as mariadb

db_host = config.mariadb_host
db_port = config.mariadb_port
db_database = config.mariadb_database
db_user = config.mariadb_username
db_pw = config.mariadb_pw


db_connection = mariadb.connect(user=db_user, password=db_pw, host=db_host, database=db_database, port=db_port)
cursor = db_connection.cursor()


sql_command = "select * from start;"
#sql_command = "insert into start(name) values ('test')"

cursor.execute(sql_command)

for row in cursor.fetchall():
    print(row[0])


db_connection.close()