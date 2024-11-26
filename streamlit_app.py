import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
#function to load Shot data

# Function to load 2024 shot data from GitHub 
@st.cache_data
def load_2024_data():
    base_url = "https://github.com/livebetedge/blank-app-1/blob/main/Shot%20Data%20By%20Period.xlsx%20-%20Sabres%20Shots.csv"
    combined_data = pd.DataFrame()
    columns_to_keep = ['Date', 'Player Name', 'Postion', 'Team', 'Opponent', 'Period 1 - SOG','Period 2 - SOG', 'Period 3 - SOG', 'Total SOG']

    for month in range(10, 12):  
        file_name = f'Shot Data by Period.xlsx - Sabres Shots.csv'
        file_url = f"{base_url}{file_name}"
        try:
            response = requests.get(file_url)
            response.raise_for_status()
            file_content = BytesIO(response.content)
            data = pd.read_csv(file_content, usecols=columns_to_keep)
            combined_data = pd.concat([combined_data, data], ignore_index=True)
        except requests.exceptions.HTTPError as http_err:
            st.warning(f"HTTP Error for file: {file_name} - {http_err}")
        except Exception as e:
            st.error(f"Error loading file {file_name}: {e}")
# Load the data
data = load_2024_data()

# Ensure data is loaded before continuing
if not data.empty:
    st.title("Buffalo Sabres Shot by Period Data")

    # Combine search bar and dropdown for player selection
    all_players = sorted(data["player_name"].dropna().unique())
    player_name = st.selectbox(
        "Search or select a player:",
        options=["Type a name or select..."] + all_players
    )

    if player_name and player_name != "Type a name or select...":
        player_data = data[data["player_name"] == player_name]

    
