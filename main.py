import config
import mysql.connector as mariadb

db_config = config.db_config

db_connection = mariadb.connect(**db_config)
cursor = db_connection.cursor()


sql_command = "select * from start;"
#sql_command = "insert into start(name) values ('test')"

cursor.execute(sql_command)

for row in cursor.fetchall():
    print(row[0])


db_connection.close()