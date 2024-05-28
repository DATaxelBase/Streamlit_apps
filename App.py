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


col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(index = None,
    label = "What news period want you to scrap?",placeholder="Choose an option",
    options =("On date setting", "On month and year", "On year"))
    


with col2:
    month = st.number_input("Insert the month",disabled = True)
    year = st.number_input("Insert the year",disabled = True)
    year_only = st.number_input("Insert the year",disabled = True)
    if option == "Full date seting":
        date = st.date_input("Pick a date",disabled = False)
        st.write('Date :',date.year, date.month, date.day)
        

    elif option == "On month and year":
        date.disabled = True
        month.disabled = False
        year.disabled = False
        year_only.disabled = True
        st.write('Month :',int(month),'\t Year:', int(year))
    else:
        date.disabled = True
        month.disabled = True
        year.disabled = True
        year_only.disabled = False
        st.write('Year :',year_only)
  
