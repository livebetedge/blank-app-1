import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
url = 'https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv'
df = pd.read_csv(url,index_col=0)
#df = pd.read_csv(url)

print(df.head(5))
