import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

conn = None
cursor = None

try:
    # Connect to TiDB without selecting a database
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "4000")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        ssl_ca=os.getenv("DB_SSL_CA"),
        ssl_verify_cert=True
    )

    print("TiDB Connection Successful!")

    cursor = conn.cursor()

    # Check available databases
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()

    print("\nDatabases visible to Flask connection:")

    for db in databases:
        print(db[0])

    # Check connection details
    cursor.execute("SELECT CURRENT_USER(), @@hostname, @@port")
    print("\nConnection Details:", cursor.fetchone())

except Exception as e:
    print("DATABASE ERROR:", e)

finally:
    if cursor:
        cursor.close()

    if conn:
        conn.close()

    print("\nDatabase connection closed.")
