import sqlite3

conn = sqlite3.connect("data/cricket.db")
cursor = conn.cursor()

cursor.execute("SELECT status, COUNT(*) FROM match_summary GROUP BY status")
print("Status breakdown:", cursor.fetchall())

cursor.execute("SELECT result FROM match_summary WHERE status = 'Completed' LIMIT 10")
print("Sample results:", cursor.fetchall())

conn.close()