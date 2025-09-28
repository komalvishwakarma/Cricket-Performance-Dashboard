from api_handler import get_recent_matches, get_player_stats
from db_handler import get_connection, create_tables
import pandas as pd

def insert_match_summary(conn, row):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO match_summary (
            match_id, team1, team2, venue, date, status, result, team1_runs, team2_runs
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row["Match ID"], row["Team 1"], row["Team 2"], row["Venue"], row["Date"],
        row["Status"], row["Result"], row.get("Team 1 Runs"), row.get("Team 2 Runs")
    ))
    conn.commit()

def insert_player_stats(conn, bat_df, bowl_df):
    cursor = conn.cursor()

    for _, row in pd.concat([bat_df, bowl_df], ignore_index=True).iterrows():
        cursor.execute("""
            INSERT INTO player_stats (
                match_id, innings_id, player, runs, balls, fours, sixes,
                strike_rate, how_out, overs, wickets, economy
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row.get("match_id"), row.get("Innings"), row.get("Player"),
            row.get("Runs"), row.get("Balls"), row.get("Fours"), row.get("Sixes"),
            row.get("Strike Rate"), row.get("Dismissal"), row.get("Overs"),
            row.get("Wickets"), row.get("Economy")
        ))
    conn.commit()

# ✅ Main ingestion logic
if __name__ == "__main__":
    conn = get_connection()
    create_tables(conn)

    summary_df = get_recent_matches()
    if summary_df.empty:
        print("⚠️ No matches found. Aborting.")
    else:
        for _, row in summary_df.iterrows():
            match_id = row["Match ID"]
            print(f"📌 Inserting match: {match_id}")

            # 🔧 Normalize status and result
            raw_status = row["Status"]

            if "won" in raw_status.lower():
                row["Status"] = "Completed"
                row["Result"] = raw_status.split(" won")[0].strip()
            elif "abandoned" in raw_status.lower():
                row["Status"] = "Abandoned"
                row["Result"] = None
            elif "draw" in raw_status.lower():
                row["Status"] = "Draw"
                row["Result"] = None
            else:
                row["Status"] = "Other"
                row["Result"] = None

            # ✅ Insert cleaned match summary
            insert_match_summary(conn, row)

            # 🏏 Player stats ingestion
            bat_df, bowl_df = get_player_stats(match_id)
            if not bat_df.empty:
                bat_df["match_id"] = match_id
            if not bowl_df.empty:
                bowl_df["match_id"] = match_id

            insert_player_stats(conn, bat_df, bowl_df)

        print("✅ All data inserted into cricket.db")
    conn.close()