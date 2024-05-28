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
option = st.selectbox(
    "What news period want you to scrap?",
    ("On date setting", "On month and year", "On year"))

if option =="Full date seting":
  date = st.date_input("Pick a date")
  st.write('Date :',date.year, date.month, date.day)
elif option == "On month and year":
  month = st.number_input("Insert the month")
  year = st.number_input("Insert the year")
  st.write('Month :',int(month),'\t Year:', int(year))
else:
  year_only = st.number_input("Insert the year")
  st.write('Year :',year_only)
  
