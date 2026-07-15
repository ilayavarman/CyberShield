import sqlite3

DATABASE = "database/cybershield.db"

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        website TEXT,

        ip_address TEXT,

        security_score INTEGER,

        risk_level TEXT,

        https TEXT,

        ssl_status TEXT,

        scan_date TEXT

    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")