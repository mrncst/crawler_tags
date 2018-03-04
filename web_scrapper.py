
# coding: utf-8

# In[2]:


# Code by Mariana Castilho
# 03/03/2018
# Import libraries
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import numpy as np


# In[3]:


# Import all the urls generated via sitemap
website = pd.read_excel('file.xlsx')


# In[4]:


# Inspect the import
website.head()


# In[5]:


website['urls'] = website['urls'].astype(str)
website.head()


# In[21]:


website.iloc[0]


# In[18]:


def crawl(url):
    return requests.get(url)


# In[22]:


# Download page
page = crawl(website.iloc[0,0])


# In[61]:


# Check if status is 200, which means the request was successful
print page.status_code


# In[63]:


# Creating necessary objects for while loop
i = 0
d = []
gtm_tag = 'gtm.js'


# In[64]:


# Creating an emty list
df = []


# In[65]:


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


# In[66]:


print df


# In[67]:


df_done = pd.DataFrame(df)
df_done.columns = ['Check']
print df_done

