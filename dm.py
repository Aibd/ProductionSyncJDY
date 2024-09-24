import pyodbc
import configparser

class DatabaseManager:
    def __init__(self):
        self.config_file = 'config.ini'
        self.config = self.load_config()
        self.connection = self._connect()

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file, encoding='utf-8')
        return config['database']

    def __enter__(self):
        self.connection = self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def _connect(self):
        connection_string = f"""
                    DRIVER={{SQL Server}};
                    SERVER={self.config['server']};
                    DATABASE={self.config['database']};
                    UID={self.config['username']};
                    PWD={self.config['password']};
                    Encrypt=no;
                """
        return pyodbc.connect(connection_string)

    def execute_query(self, command):
        with self.connection.cursor() as cursor:
            cursor.execute(command)
            return cursor.fetchall()

    def execute_many(self, command, datalist):
        with self.connection.cursor() as cursor:
            cursor.executemany(command, datalist)
            self.connection.commit()

    def execute_delete(self,tablename, interid, entryid):
        sql = f"DELETE FROM {tablename} WHERE interid = ? AND entryid = ?"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (interid, entryid))
            self.connection.commit()
            return cursor.rowcount

    def execute(self, command):
        with self.connection.cursor() as cursor:
            cursor.execute(command)
            self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()

