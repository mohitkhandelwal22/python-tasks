#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# load data set in pandas module
data=pd.read_csv(r"C:\Users\lovel\OneDrive\Desktop\DAW\movies (1).csv")
data


# In[3]:


# head()functions use
data.head(20)


# In[4]:


data.info()


# In[5]:


data.describe()


# # to convert(imdb_votes)object to int

# In[6]:


data["imbd_votes"]=data['imbd_votes'].replace(",","",regex=True).astype(int)
data["imbd_votes"]


# In[7]:


data.info()


# # 2 find out which movie has the maximum number of votes and which genre it belong to and its durations

# In[8]:


data["imbd_votes"].max()


# In[9]:


data1=data.loc[data["imbd_votes"]==2711075]
data1[["title","imbd_votes","genre","duration"]]


# # 3 find out which movie has the minimum numbers of votes and which genre it belongs to and its durations

# In[10]:


data["imbd_votes"].min()


# In[11]:


data1=data.loc[data["imbd_votes"]==31167]
data1[["title","imbd_votes","genre","duration"]]


# # 4 find out movies of each genre which has maximum numbers of votes

# In[13]:


gp=data.groupby("genre").agg({"imbd_votes":max})
gp


# # 5 plot a graph to show the distrubution of genres in the top 20 movies?

# In[18]:


sns.set(style="whitegrid")
sns.scatterplot(data=data,x="imbd_rating",y="imbd_votes",hue="genre",palette="viridis")
plt.legend(bbox_to_anchor=(1.2,0,0.2,1))
plt.show()


# In[ ]:




