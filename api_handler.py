import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_recent_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    print("Fetching recent matches...")

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        raw_data = response.json()
        print(json.dumps(raw_data, indent=2))

        # Assuming your JSON is stored in a variable called `raw_data`
        match_list = raw_data.get("typeMatches", [])
        cleaned_matches = []

        for match_type in match_list:
            for series in match_type.get("seriesMatches", []):
                # Some entries may have "seriesAdWrapper" wrapping actual matches
                series_data = series.get("seriesAdWrapper", series)
                for match in series_data.get("matches", []):
                    info = match.get("matchInfo", {})
                    score = match.get("matchScore", {})
                    venue = info.get("venueInfo", {})
                    match_id = info.get("matchId", "")

                    # Extract teams
                    team1 = info.get("team1", {}).get("teamName", "")
                    team2 = info.get("team2", {}).get("teamName", "")

                    # Extract venue details
                    venue_name = venue.get("ground", "")
                    venue_city = venue.get("city", "")

                    # Match status
                    status = info.get("status", "")
                    result = info.get("stateTitle", "")
                    date = info.get("startDate", "")

                    # Scores
                    team1_score = score.get("team1Score", {}).get("inngs1", {})
                    team2_score = score.get("team2Score", {}).get("inngs1", {})

                    cleaned_matches.append({
                        "Match ID": match_id,
                        "Team 1": team1,
                        "Team 1 Runs": team1_score.get("runs", ""),
                        "Team 1 Wickets": team1_score.get("wickets", ""),
                        "Team 1 Overs": team1_score.get("overs", ""),
                        "Team 2": team2,
                        "Team 2 Runs": team2_score.get("runs", ""),
                        "Team 2 Wickets": team2_score.get("wickets", ""),
                        "Team 2 Overs": team2_score.get("overs", ""),
                        "Venue": f"{venue_name}, {venue_city}" if venue_name or venue_city else "",
                        "Date": date,
                        "Status": status,
                        "Result": result
                    })
        df = pd.DataFrame(cleaned_matches)
        print("Cleaned DataFrame:")
        print(df)
        return df
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return pd.DataFrame([{"Error": str(e)}])


import requests, os, pandas as pd, time
from dotenv import load_dotenv

load_dotenv()

# ✅ Function to fetch batting & bowling data for a single match
def get_player_stats(match_id):
    url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id}/scard"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"⚠️ Match {match_id} failed, status {response.status_code}")
            return pd.DataFrame(), pd.DataFrame()

        data = response.json()
        batting_data, bowling_data = [], []

        for innings in data.get("scorecard", []):
            # Batting
            for player in innings.get("batsman", []):
                batting_data.append({
                    "Match ID": match_id,
                    "Innings ID": innings.get("inningsid", ""),
                    "Player": player.get("name", ""),
                    "Runs": player.get("runs", ""),
                    "Balls": player.get("balls", ""),
                    "Fours": player.get("fours", ""),
                    "Sixes": player.get("sixes", ""),
                    "Strike Rate": player.get("strkrate", ""),
                    "How Out": player.get("outdec", "")
                })

            # Bowling
            for bowler in innings.get("bowler", []):
                bowling_data.append({
                    "Match ID": match_id,
                    "Innings ID": innings.get("inningsid", ""),
                    "Player": bowler.get("name", ""),
                    "Overs": bowler.get("overs", ""),
                    "Runs Conceded": bowler.get("runs", ""),
                    "Wickets": bowler.get("wickets", ""),
                    "Economy": bowler.get("econ", "")
                })

        return pd.DataFrame(batting_data), pd.DataFrame(bowling_data)

    except Exception as e:
        print(f"❌ Error for match {match_id}: {e}")
        return pd.DataFrame(), pd.DataFrame()


# ✅ Function to loop through all matches in your summary DataFrame
def build_full_stats(summary_df, limit=None):
    all_batting, all_bowling = [], []

    match_ids = summary_df["Match ID"].tolist()
    if limit:  # for testing small batch first
        match_ids = match_ids[:limit]

    for match_id in match_ids:
        print(f"Fetching stats for Match ID: {match_id}")
        bat_df, bowl_df = get_player_stats(match_id)

        if not bat_df.empty:
            all_batting.append(bat_df)
        if not bowl_df.empty:
            all_bowling.append(bowl_df)

        time.sleep(1)  # 🕒 avoid rate limits

    return (
        pd.concat(all_batting, ignore_index=True) if all_batting else pd.DataFrame(),
        pd.concat(all_bowling, ignore_index=True) if all_bowling else pd.DataFrame()
    )
