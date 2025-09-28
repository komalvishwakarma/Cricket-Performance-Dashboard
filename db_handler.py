import sqlite3
import os

def get_connection():
    os.makedirs("data", exist_ok=True)
    db_path = os.path.join("data", "cricket.db")
    return sqlite3.connect(db_path)

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS match_summary (
            match_id TEXT PRIMARY KEY,
            team1 TEXT,
            team2 TEXT,
            venue TEXT,
            date TEXT,
            status TEXT,
            result TEXT,
            team1_runs INTEGER,
            team2_runs INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_stats (
            match_id TEXT,
            innings_id INTEGER,
            player TEXT,
            runs INTEGER,
            balls INTEGER,
            fours INTEGER,
            sixes INTEGER,
            strike_rate REAL,
            how_out TEXT,
            overs REAL,
            wickets INTEGER,
            economy REAL
        )
    """)

    conn.commit()