#! /usr/bin/env python3

import streamlit as st


st.write("""
# My first app 
Hello *world!*
""")
date = st.date_input("Pick a date")


import numpy as np
import pandas as pd
import requests
import re
import time
from bs4 import BeautifulSoup as bf
url = 'https://www.ndtv.com/sitemap.xml/?yyyy=2024&mm=05&dd=26'
response = requests.get(url)
soup = bf(response.content, 'xml')
url_blocks = [i.get_text() for i in soup.find_all('loc')]
df_templates={'url':url_blocks,}
df = pd.DataFrame(df_templates,columns=['url'])
df['url_domain'] = df['url'].apply(lambda x :x.split('/')[3])
## For india-news domains
common_url = list(df.loc[~(df.url_domain == "education") & ~(df.url_domain == "sitemap")]['url'])
titles = []
articles_body = []
date = []
for el in common_url:
    resp = requests.get(el)
    if re.findall('''[0-9]+''',str(resp))[0] == '200': 
        soup = bf(resp.content, 'lxml')
        try:
            titles.append([i.get_text() for i in soup.find("h1",class_ = "sp-ttl")][0])
        except:
            print(el)
        articles_body.append(soup.find_all('div',itemprop = "articleBody")[0].get_text())
        date_full = soup.find_all('span',itemprop = "dateModified")[0].get_text()
        try:
            date.append(date_full.split('Updated: ')[1])
        except:
            try:
                date.append(date_full)
            except:
                date.append(" ")
                print(el)
                continue
        #time.sleep(1)
    else:
        print('Issue with this website :'+el)
education_url = list(df.loc[(df.url_domain == "education")]['url'])
for ele in education_url:
    resp = requests.get(ele)
    if re.findall('''[0-9]+''',str(resp))[0] == '200': 
        soup = bf(resp.content, 'lxml')
        try:
            titles.append([i.get_text() for i in soup.find("h1",class_ = "sp-ttl")][0])
        except:
            try:
                test = re.findall('''[a-zA-Z][\w\W]+''',soup.find("h1").get_text())[0]
                titles.append(test)
            except:
                print('Title new pattern :',ele)
                continue
        try:
            articles_body.append(soup.find_all('div',class_ = "Art-exp_wr")[0].get_text())
        except:
            try:
                articles_body.append(" ".join([i.get_text() for i in soup.find_all('div',itemprop = "articleBody")[0].find('div')]))
            except:    
                print('New article body pattern',ele)
                continue
        try:
            date_full = soup.find_all('span',itemprop = "dateModified")[0].get_text()
            date.append(date_full.split('Updated: ')[1])
        except:
            try:
                date_full = soup.find_all('span',itemprop = "dateModified")[0].get_text()
                date.append(date_full)
            except:
                try:
                    date.append(soup.find_all('span',class_ = "LvbTpBig_lnk")[0].get_text())
                except:
                    print('New date pattern',ele)
                    continue
        #time.sleep(1)
    else:
        print('Issue with this website :'+el)


df_articles={'Title':titles,
            'Content':articles_body,
            'Date':date}

df_extract = pd.DataFrame(df_articles,columns=['Title','Content','Date'])
df_extract.head()
