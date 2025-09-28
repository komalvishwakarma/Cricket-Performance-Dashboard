import streamlit as st

st.set_page_config(page_title="Cricket Analytics Dashboard", layout="wide")

# 🏠 Title and Introduction
st.title("🏏 Cricket Analytics Dashboard")
st.markdown("""
Welcome to the **Cricket Analytics Dashboard** — a multi-page web application designed to explore, analyze, and manage cricket data interactively.

This project is ideal for:
- 📊 Data analysts and sports enthusiasts
- 🧠 SQL learners and dashboard developers
- 🛠️ Anyone curious about cricket performance insights
""")

# 🧰 Tools & Technologies
st.header("🧰 Tools & Technologies")
st.markdown("""
- **Streamlit** for interactive UI and multi-page navigation  
- **SQLite** for local database storage  
- **Pandas** for data manipulation  
- **SQL** for querying and analytics  
- **Python** for backend logic and API integration  
""")

# 📂 Folder Structure
st.header("📂 Project Structure")
st.code("""
CRICBUZZ_DASHBOARD/
├── app.py or Home.py              # Main entry point
├── pages/
│   ├── sql_queries.py             # SQL Analytics Explorer
│   ├── crud_operations.py         # Create, Read, Update, Delete interface
│   ├── live_match.py              # Live match viewer
│   ├── sql_analytics.py           # Predefined query dashboard
├── utils/
│   └── db_connection.py           # Centralized DB connection
├── data/
│   └── cricket.db                 # SQLite database
├── sample_match_data.py          # Offline mock data
├── load_data.py                  # One-time ingestion script
""", language="bash")


# 🧭 Navigation Guide
st.header("🧭 Navigation Guide")
st.markdown("""
Use the sidebar to explore:
- **SQL Queries**: Run custom and predefined SQL queries  
- **CRUD Operations**: Add, update, or delete player/match records  
- **Live Match Viewer**: View recent match scorecards  
- **SQL Analytics**: Explore 25+ advanced cricket insights  
""")

# ✅ Final Message
st.success("You're all set to explore cricket like never before!")