import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
# Updated URL to the raw CSV content
raw_url = 'https://raw.githubusercontent.com/livebetedge/blank-app-1/main/Sabres%20Shot%20Data%20-%2011.20.csv'  
df = pd.read_csv(raw_url)
print(df)

   

