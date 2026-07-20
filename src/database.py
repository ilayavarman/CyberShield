import sqlite3
from datetime import datetime

DATABASE = "database/cybershield.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(
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


def save_scan(
    website,
    ip_address,
    security_score,
    risk_level,
    https,
    ssl_status
):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scans
    (
        website,
        ip_address,
        security_score,
        risk_level,
        https,
        ssl_status,
        scan_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        website,
        ip_address,
        security_score,
        risk_level,
        https,
        ssl_status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()