#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("COVID-19_Case_Surveillance_Public_Use_Data.csv")


# In[8]:


df


# In[5]:


df['sex'].value_counts().plot()


# In[18]:


df['sex'].value_counts().plot(kind='bar')


# In[6]:


df.head()


# In[7]:


df.fillna(0,inplace=True)


# In[13]:


df['Race and ethnicity (combined)'].value_counts()


# In[12]:


df['Race and ethnicity (combined)'].value_counts().plot(kind='bar')


# In[15]:


df['age_group'].value_counts()


# In[17]:


df['age_group'].value_counts().plot(kind='bar')


# In[25]:


df['cdc_report_dt'].value_counts()


# In[26]:


df['cdc_report_dt'].value_counts().plot()


# In[28]:


df[df['cdc_report_dt'] == '2020/07/06']


# In[ ]:




