import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
df = pd.read_csv("https://github.com/livebetedge/blank-app-1/blob/main/SabresShotData - 11.20.csv")  
st.title("Buffalo Sabres Shot Data")
st.write(df) 


   

