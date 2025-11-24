import sqlite3
from datetime import datetime
import os

class DatabaseManager:
    def __init__(self, db_path="data/site_logs.db"):
        # Ensure data directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS violations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            violation_type TEXT,
            confidence REAL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log_violation(self, violation_type, confidence):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO violations (timestamp, violation_type, confidence) VALUES (?, ?, ?)"
        self.conn.execute(query, (timestamp, violation_type, confidence))
        self.conn.commit()
        print(f"[LOG] Violation recorded: {violation_type} at {timestamp}")

    def close(self):
        self.conn.close()