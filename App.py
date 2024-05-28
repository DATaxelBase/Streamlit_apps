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
        if date.month < 10 and date.day < 10:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(date.year)+"&amp;mm="+'0'+str(date.month)+"&amp;dd="+'0'+str(date.day)
        elif date.month > 10 and date.day < 10:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(date.year)+"&amp;mm="+str(date.month)+"&amp;dd="+'0'+str(date.day)
        elif date.month < 10 and date.day > 10:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(date.year)+"&amp;mm="+'0'+str(date.month)+"&amp;dd="+str(date.day)
        else:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(date.year)+"&amp;mm="+str(date.month)+"&amp;dd="+str(date.day)
            
        

    elif option == "On month and year":
        month = st.number_input("Insert the month")
        year = st.number_input("Insert the year")
        st.write('Month :',int(month),'\t Year:', int(year))
        if month < 10:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(int(year))+"&amp;mm="+'0'+str(int(month))
        else:
            url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(int(year))+"&amp;mm="+str(int(month))
        
    else:
        year_only = st.number_input("Insert the year")
        st.write('Year :',year_only)
        url = "https://www.ndtv.com/sitemap.xml/?yyyy="+str(int(year_only))

req =st.button("Query website", type="secondary")
if req:
    st.write(url)
    st.write(requests.get(url))
else:
    st.write("Test website")
  
