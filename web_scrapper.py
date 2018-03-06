# coding: utf-8

# Code by Mariana Castilho @mrncst
# 03/03/2018

# Import libraries
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import numpy as np

# Import all the urls generated via sitemap
website = pd.read_excel('file.xlsx')

# Inspect the import
website.head()
website['urls'] = website['urls'].astype(str)
website.head()
website.iloc[0]

# Create a function to call GET requests
def crawl(url):
    return requests.get(url)

# Download page
page = crawl(website.iloc[0,0])

# Check if status is 200, which means the request was successful
print page.status_code

# Creating necessary objects for while loop
i = 0
d = []
gtm_tag = '/gtm.js'

# Creating an empty list
df = []

# This loop will consult all the urls into the DataFrame we created from the sitemap file, request their codes and check if there's the tag we're looking from in every item in the df
while i < len(website):
    try:
        d = crawl(website.iloc[i,0])
        soup = bs(d.content, 'html.parser')
        script = soup.find_all('script')
        script_string = str(script)
        if script_string.index(gtm_tag) <> '[]':
            print 'Has GTM' 
            df.append(1)
    except ValueError:
        print 'Does not have GTM' 
        df.append(0)
    i = i + 1

# Check how it looks and create a new DataFrame to write an file
print df
df_done = pd.DataFrame(df)
df_done.columns = ['Check']
print df_done

# Write the final output in a file
df_done.to_csv('tag_audit.csv', sep='\t', encoding='utf-8')

# Check the tags in the GTM container
gtm_id = 'GTM-XXXXX' # Insert the GTM account id. It looks like GTM-XXXX
gtm_url = 'https://www.googletagmanager.com/gtm.js?id='
gtm = gtm_url + gtm_id

# Request GTM page
page_gtm = requests.get(gtm)

# Define de tags you want to find inside GTM
dbm = 'doubleclick'
fb = 'facebook'
twitter = 'twitter'

# Check the page for the tags you want tof ind
if page_gtm_string.find(dbm) >= 0:
    print 'DBM'
else:
    print 'No DBM'

if page_gtm_string.find(dbm) >= 0:
    print 'Facebook'
else:
    print 'No Facebook'
    
if page_gtm_string.find(twitter) >= 0:
    print 'Twitter'
else:
    print 'No Twitter'