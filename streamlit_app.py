import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
st.title ('Buffalo Sabres Shot by Period Data')
st.write ('Please use the drop down menu below to select a player and see his recent shot data')
st.selectbox (label = 'Player Name', option = ['Rasmus Dahlin', 'Dylan Cozens'])
