import config
import mysql.connector as mysql
from mysql.connector import errorcode

class Database():
    """DB creates a database connection, creates tables and maintain contents"""

    def __init__(self):
        """Opens database connection from config.py"""

        # read connection parameters
        self.db_config = config.db_config

        # open db connection
        self.connect()


    def __enter__(self):
        """initialize with block"""
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """connection will be closed at end of with block"""
        self.close()


    def connect(self):
        """opens db connection"""

        # open connection
        self.db_connection = mysql.connect(**self.db_config)


    def close(self):
        """Close the db connection"""
        self.db_connection.close()


    def createTables(self):
        """Create all tables"""

        self.tables = config.tables

        try:
            self.cursor = self.db_connection.cursor()
            for name, sql in self.tables.items():
                self.cursor.execute(sql)
                print("Tabelle " + name + " erfolgreich erstellt")
        except mysql.Error as err:
            print(err.msg)
            raise


    def dropTables(self):
        """Create all tables"""

        self.tables = config.tables

        try:
            self.cursor = self.db_connection.cursor()
            for name, sql in self.tables.items():
                sql = "DROP TABLE " + str(name)
                self.cursor.execute(sql)
                print("Tabelle " + name + " erfolgreich gelöscht")
        except mysql.Error as err:
            print(err.msg)
            raise


    def test(self):
        self.cursor = self.db_connection.cursor()
        self.sql_command = "select * from start;"
        self.cursor.execute(self.sql_command)

        for row in self.cursor.fetchall():
            print(row[0])