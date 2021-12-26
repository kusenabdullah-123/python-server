# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform


def connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="gomagame"

        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    return conn.cursor()
