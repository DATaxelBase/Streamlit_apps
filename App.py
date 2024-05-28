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
# My first app 
Hello *world!*
""")
date = st.date_input("Pick a date")
#print(date)
st.write('Date :',date.year, date.month, date.day)
