#!/usr/bin/env python
# coding: utf-8

# # 1. DOWNLOAD THE DATASET

# # 2 LOAD THE DATASET
# 

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns
from scipy.sparse.construct import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from ast import increment_lineno
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib

data =pd.read_csv('abalone.csv')
data.head()


# # 3. PERFORM BELOW VISUALIZATIONS

# #### Univariate Analysis
# 

# In[18]:


sns.histplot(data.Height,kde=True)


# In[19]:


sns.histplot(data.Rings,kde=True)


# #### Bivariate analysis

# In[20]:


sns.scatterplot(data.Length,data.Height)


# # MULTIVARIATE ANALYSIS

# In[21]:


sns.pairplot(data)


# # 4. Perform descriptive statistics on the dataset.
# 

# In[22]:


data.describe(include='all')


# # 5. Check for Missing values and deal with them.

# In[23]:


sns.set(color_codes=True)
data.head()


# # 6. Find the outliers and replace the outliers

# In[26]:


matplotlib.rcParams['figure.figsize']=(11,6)
data.sample(10)


# # 7. Check for Categorical columns and perform encoding. 

# In[27]:


data.columns
headers=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
data.head()


# # 8. Split the data into dependent and independent variables.

# In[28]:


x=data.iloc[:,:-1].values
print(x)
y=data.iloc[:,-1]._values
print(y)


# # 9. Scale the independent variables

# In[29]:


d = data[['Length','Height']]
sns.heatmap(d.corr(), annot=True)
sns.set(rc={'figure.figsize':(20,20)})


# # 10. Split the data into training and testing

# In[31]:



x= data.iloc[:, 1:2].values
y= data.iloc[:,2].values

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print('Row count of x_train table'+'-'+str(f"{len(x_train):,}"))
print('Row count of y_train table'+'-'+str(f"{len(y_train):,}"))
print('Row count of x_test table'+'-'+str(f"{len(x_test):,}"))
print('Row count of y_test table'+'-'+str(f"{len(y_test):,}"))


# # 11. Build the Model

# In[32]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()


# # 12. Train the Model

# In[33]:


model.fit(x_train,y_train)


# # 13. Test the Model 

# In[34]:


prediction = model.predict(x_test)
prediction


# In[35]:


output = model.predict([[1.3]])
output


# In[ ]:




