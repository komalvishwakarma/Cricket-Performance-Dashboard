import pandas as pd

def get_sample_matches():
    data = [
        {
            "Match ID": "130001",
            "Team1": "India",
            "Team2": "Australia",
            "Venue": "Wankhede, Mumbai",
            "Date": "2025-09-01",
            "Status": "Completed",
            "Result": "India won by 5 wickets",
            "Team 1 Runs": 245,
            "Team 2 Runs": 242
        },
        {
            "Match ID": "130002",
            "Team1": "Pakistan",
            "Team2": "Sri Lanka",
            "Venue": "Gaddafi Stadium, Lahore",
            "Date": "2025-09-03",
            "Status": "Completed",
            "Result": "Sri Lanka won by 3 runs",
            "Team 1 Runs": 198,
            "Team 2 Runs": 201
        }
    ]
    return pd.DataFrame(data)


def get_sample_player_stats(match_id):
    if match_id == "130001":
        batting = pd.DataFrame([
            {"match_id": match_id, "innings_id": 1, "player": "Rohit Sharma", "runs": 72, "balls": 50, "fours": 8, "sixes": 2, "strike_rate": 144.0, "how_out": "c Smith b Starc"},
            {"match_id": match_id, "innings_id": 1, "player": "Virat Kohli", "runs": 65, "balls": 55, "fours": 6, "sixes": 1, "strike_rate": 118.2, "how_out": "b Zampa"}
        ])
        bowling = pd.DataFrame([
            {"match_id": match_id, "innings_id": 1, "player": "Jasprit Bumrah", "overs": 10, "wickets": 3, "economy": 4.2},
            {"match_id": match_id, "innings_id": 1, "player": "Ravindra Jadeja", "overs": 10, "wickets": 2, "economy": 5.0}
        ])
        return batting, bowling
    else:
        return pd.DataFrame(), pd.DataFrame()