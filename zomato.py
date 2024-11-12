#!/usr/bin/env python
# coding: utf-8

# <h1>Zomato Data Analysis

# <h3>__Importing necessary libraries__
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# <h3>Read the top 5 items

# In[5]:


data=pd.read_csv("Zomato data .csv")


# In[6]:


data.head()


# <h3>Remove the denominator and convert to float

# In[10]:


def handle_rate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)
data['rate']=data['rate'].apply(handle_rate)
data.head()
    


# <h3> Summary of the data

# In[11]:


data.info()


# In[12]:


data.describe()


# <h3> Type of Restaurant VS Count

# In[15]:


sns.countplot(x=data['listed_in(type)'])
plt.xlabel("Type of restaurant")


# <h3> Type of Restaurant VS Votes

# In[24]:


grouped_data=data.groupby("listed_in(type)")['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c="green",marker="o")
plt.xlabel("Type of Restaurant",c="blue",size=10)
plt.ylabel("Votes",c="blue",size=12)


# <h3> Restaurant with max votes

# In[28]:


max_votes=data['votes'].max()
restaurant_max_vote=data.loc[data['votes']==max_votes,'name']

print("Restaurants with max votes are:")
print(restaurant_max_vote)


# <h3>Online VS offline orders

# In[31]:


sns.countplot(x=data["online_order"])


# <h3> Distribution of Ratings

# In[35]:


plt.hist(data["rate"],bins=5)
plt.title("Ratings Distributions")


# <h3> Approximate cost for two people

# In[38]:


couple_data=data["approx_cost(for two people)"]
sns.countplot(x=couple_data)


# <h3> Ratings- Online VS Offline

# In[44]:


plt.figure(figsize=(6,6))
sns.boxplot(x="online_order",y="rate",data=data)


# <h3> Pivot table

# In[48]:


pivot_table=data.pivot_table(index="listed_in(type)",columns="online_order",aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True)


# In[ ]:




