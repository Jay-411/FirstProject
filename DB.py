import config
import mysql.connector as mariadb

class Database():
    """DB creates a database connection, creates tables and maintain contents"""

    def __init__(self):
        """Opens database connection from config.py"""

        # read connection parameters
        self.db_config = config.db_config

    def connect(self):
        """opens db connection"""

        # open connection
        self.db_connection = mariadb.connect(**self.db_config)


    def close(self):
        """Close the db connection"""
        self.db_connection.close()

    def test(self):
        self.cursor = self.db_connection.cursor()
        self.sql_command = "select * from start;"
        self.cursor.execute(self.sql_command)

        for row in self.cursor.fetchall():
            print(row[0])