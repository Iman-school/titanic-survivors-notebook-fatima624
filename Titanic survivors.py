#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as rp
import pandas as pd



# In[2]:


df= pd.read_csv('titanic-passengers.csv', sep=';')
df.head()


# In[3]:


df.info()


# In[5]:


df.isnull()


# In[6]:


df.isnull().sum()


# In[12]:


df['Age'].isnull().sum()


# In[9]:


df['Cabin'].isnull().sum()


# In[10]:


df['Embarked'].isnull().sum()


# In[ ]:




