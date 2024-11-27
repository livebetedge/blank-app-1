import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
st.title ('Buffalo Sabres Shot by Period Data')
st.write ('Please use the drop down menu below to select a player and see his recent shot data')
option = st.multiselect(
    'Player Name',
    ['Rasmus Dahlin', 'Dylan Cozens', 'JJ Peterka'])

if 'Rasmus Dahlin' in option:
    Rasmus_Dahlin_id = st.write('Rasmus Dahlin is a 1st period shot leader for the Buffalo Sabres')
   

