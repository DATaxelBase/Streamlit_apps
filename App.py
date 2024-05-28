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
Hello, let's scrape your sitemap.
""")


col1, col2 = st.columns(2)

with col1:
    option = st.radio(
    label = "What news period want you to scrap?",
    options =("On date setting", "On month and year", "On year"))
    


with col2:
    
    if option == "On date setting":
        date = st.date_input("Pick a date",disabled = False)
        st.write('Date :',date.year, date.month, date.day)
        url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(date.year)+"&mm="+str(date.month)+"&dd="+str(date.day)
        st.write(requests.get(url))
        

    elif option == "On month and year":
        month = st.number_input("Insert the month")
        year = st.number_input("Insert the year")
        st.write('Month :',int(month),'\t Year:', int(year))
        url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(year)+"&amp;mm="+str(month)
        st.write(requests.get(url))

    else:
        year_only = st.number_input("Insert the year")
        st.write('Year :',year_only)
        url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(year_only)
        st.write(requests.get(url))
        
  
