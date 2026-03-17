# 🏏 Cricbuzz LiveStats: Cricket Analytics Dashboard

## Project Overview

Cricbuzz LiveStats is an interactive cricket analytics dashboard built using **Python, SQL, and Streamlit**. The project integrates real-time cricket data from an API and combines it with a SQL database to provide meaningful insights on matches and player performance.

The application allows users to explore live match data, analyze player statistics, run SQL-based queries, and perform database operations through an intuitive web interface.

## Problem Statement

To build an end-to-end cricket analytics application that:

- Fetches and processes real-time cricket data
- Stores and manages data using a SQL database
- Provides interactive analytics through a dashboard
- Enables users to perform SQL-based analysis and CRUD operations

## Tools & Technologies

- Python
- Streamlit
- SQL (MySQL / SQLite)
- REST API
- Pandas
- JSON

## Project Workflow

### 1. Data Fetching (API Integration)

- Integrated Cricbuzz API using Python
- Fetched live match data, player stats, and series details
- Processed JSON responses for analysis

### 2. Database Integration

- Designed and connected a SQL database
- Stored match and player data
- Managed database operations through Python

### 3. Data Processing

- Cleaned and structured API data
- Converted raw JSON into tabular format
- Prepared data for SQL queries and dashboard display

### 4. Dashboard Development (Streamlit)

- Built a multi-page interactive dashboard
- Designed a user-friendly interface for analysis and navigation

## Key Features

### 🔴 Live Match Insights

- Real-time match updates
- Scorecards and match details
- Team and venue information

### 📊 Player Statistics

- Top performers in batting and bowling
- Performance comparisons
- Key player metrics

### 🧮 SQL Analytics Module

- Implemented SQL queries for cricket analytics
- Extracted insights such as:
  - Player performance
  - Team statistics
  - Match trends

### ⚙️ CRUD Operations

- Add, update, and delete records
- Form-based UI for database interaction

## Dashboard Pages

- **Home Page** – Project overview and navigation
- **Live Match Page** – Real-time match data and scorecards
- **Player Stats Page** – Performance insights and statistics
- **SQL Analytics Page** – Query-based cricket analysis
- **CRUD Page** – Data management interface

## Key Learnings

- API integration using Python
- Handling real-time JSON data
- SQL database design and querying
- Building dashboards using Streamlit
- End-to-end data pipeline development

## How to Run the Project

1. Install dependencies:

```bash
pip install -r requirements.txt

2. Run the Streamlit app:

streamlit run app.py

## Repository Structure

CRICBUZZ_DASHBOARD
│
├── app.py
├── api_handler.py
├── db_handler.py
├── load_data.py
├── check_db.py
├── test_api.py
├── sample_match_data.py
├── match_data.json
├── requirements.txt
├── pages/
├── data/
├── Cricbuzz.docx
└── .env

## Conclusion

This project demonstrates how real-time API data, SQL analytics, and interactive dashboards can be combined to build a complete analytics solution.

It highlights strong capabilities in:

- Data processing
- API integration
- SQL querying
- Dashboard development

making it a solid end-to-end data analytics project.
