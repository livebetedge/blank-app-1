import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
url = 'https://github.com/livebetedge/blank-app-1/blob/main/Shot%20Data%20By%20Period.xlsx%20-%20Sabres%20Shots.csv'
df = pd.read_csv(url,index_col=0)
#df = pd.read_csv(url)

print(df.head(5))
