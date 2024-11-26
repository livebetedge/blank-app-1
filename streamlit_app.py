import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
st.title ("Buffalo Sabres Shot by Period Data")
st.write ("Please use the dropdown to filter players and see recent shot data")
st.selectbox (label = 'Player Name', options = ['Rasmus Dahlin', 'Tage Thompson', 'Jason Zucker','Alex Tuch','Dylan Cozens'])
#function to load Shot data
