import os
import pymysql
from contextlib import contextmanager
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseConnection:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT"))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def wait_for_db(self, max_tries: int = 20, retry_interval: int = 3):
        logger.info(f"Waiting for database {self.host}: {self.port}...")

        for attempt in range (max_tries):
            try:
                connection = pymysql.connect(
                    host = self.host
                    user = self.user
                    password = self.password
                    port = self.port
                )
                connection.close()
                logger.info("Connection to Database was successful, database is ready.")
                return True
            except pymysql.Error as e:
                logger.warning(f"Failed connecting to database, database not ready yet: {e}")
                time.sleep(retry_interval)
        raise Exception("Database Connection Failed, max attempt exceeded")

    def get_connection(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                charset="utf8bm4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            return connection
        except pymysql.Error as e:
            logger.error(f"Failed to connect: {e}")
            raise

    @contextmanager
    def get_cursor(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            yield cursor
            connection.commit()

        except Exception as e:
            connection.rollback()
            logger.error(f"Query failed: {e}")
            raise
        
        finally:
            cursor.close()
            connection.close()

db = DatabaseConnection()

