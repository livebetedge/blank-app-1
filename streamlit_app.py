import pandas as pd 
import numpy as npy 
import streamlit as st
import altair as alt
import requests
from io import BytesIO
df = pd.read_csv("./data/Shot Data by Period.xlsx-Sabres Shots")
