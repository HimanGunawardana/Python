#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[13]:


df = pd.read_csv(r"world_population.csv")
df


# In[14]:


#display allthe records which has a rank less than or equal to 10. rank eke agaya 0 th 10th athara
df[df['Rank'] <=10]


# In[15]:


#display all the details of the countries: Bangladesh & Brazil

countries = ['Bangladesh' , 'Brazil']
df[df['Country'].isin(countries)]


# In[16]:


#display all the records belong to the countries,containing the string 'United'
#United kiyala nama thiyana data sets(records)
df[df['Country'].str.contains('United')]


# In[17]:


#make the 'country' column as the index column in the dataframe.
df = df.set_index('Country')
df


# In[ ]:




