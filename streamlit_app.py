import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
df = pd.read_csv("https://github.com/livebetedge/blank-app-1/blob/main/Sabres%20Shot%20Data%20-%2011.20.csv")  
st.title("Buffalo Sabres Shot Data")
st.write(df) 


   

