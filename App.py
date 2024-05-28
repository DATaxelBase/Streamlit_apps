#! /usr/bin/env python3
import streamlit as st
import numpy as np
import pandas as pd
import requests
from datetime import datetime
import re
import time
from bs4 import BeautifulSoup as bf

st.write("""
# News Scraper
Hello, let's scrape your sitemap
""")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(index = None,key = st.session_state.visibility,
    "What news period want you to scrap?",
    ("On date setting", "On month and year", "On year"),placeholder="Choose an option")
    


with col2:
    if option == "Full date seting":
        date = st.date_input("Pick a date",key ="visibility")
        st.write('Date :',date.year, date.month, date.day)
        month = st.number_input("Insert the month",key =st.session_state.disabled)
        year = st.number_input("Insert the year",key =st.session_state.disabled)
        year_only = st.number_input("Insert the year",st.session_state.disabled)

    elif option == "On month and year":
        date = st.date_input("Pick a date",key =st.session_state.disabled)
        month = st.number_input("Insert the month",key =st.session_state.visibility)
        year = st.number_input("Insert the year",key =st.session_state.visibility)
        year_only = st.number_input("Insert the year",st.session_state.disabled)
        st.write('Month :',int(month),'\t Year:', int(year))
    else:
        date = st.date_input("Pick a date",key =st.session_state.disabled)
        month = st.number_input("Insert the month",key =st.session_state.disabled)
        year = st.number_input("Insert the year",key =st.session_state.disabled)
        year_only = st.number_input("Insert the year",st.session_state.visibility)
        st.write('Year :',year_only)
  
