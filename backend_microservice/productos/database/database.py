import mysql.connector
from mysql.connector import pooling
from core.config import DATABASE_CONFIG

class Database:
    _connection_pool = None

    @staticmethod
    def initialize_pool():
        if not Database._connection_pool:
            Database._connection_pool = pooling.MySQLConnectionPool(
                pool_name=DATABASE_CONFIG["pool_name"],
                pool_size=DATABASE_CONFIG["pool_size"],
                pool_reset_session=True,
                host=DATABASE_CONFIG["host"],
                database=DATABASE_CONFIG["database"],
                user=DATABASE_CONFIG["user"],
                password=DATABASE_CONFIG["password"],
            )

    @staticmethod
    def get_connection():
        if not Database._connection_pool:
            Database.initialize_pool()
        return Database._connection_pool.get_connection()

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor(dictionary=True)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            if exc_type is None:
                self.connection.commit()  # Commit si no hay excepciones
            else:
                self.connection.rollback()  # Rollback en caso de error
            self.connection.close()
