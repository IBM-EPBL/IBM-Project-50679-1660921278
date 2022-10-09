#!/usr/bin/env python
# coding: utf-8

# # 1. Download the dataset
# 

# # 2. Load the dataset.
# 

# In[5]:


import numpy as np
import pandas as pd
data = pd.read_csv("Churn_Modelling.csv")


# In[6]:


data


# # 3. Visualizations.

# ###  Univariate Analysis
# 

# In[7]:


import seaborn as sns
sns.histplot(data.EstimatedSalary,kde=True)


# ### Bi - Variate Analysis

# In[9]:


import matplotlib.pyplot as plt
sns.scatterplot(data.Balance,data.EstimatedSalary)
plt.ylim(0,20000)


# #  Multi - Variate Analysis
# 

# In[11]:


import seaborn as sns
data=pd.read_csv("Churn_Modelling.csv")
sns.pairplot(data)


# # 4. Perform descriptive statistics on the dataset.

# In[12]:


data=pd.read_csv("Churn_Modelling.csv")
data.describe(include='all')


# # 5. Handle the Missing values.

# In[13]:


from ast import increment_lineno
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


sns.set(color_codes=True)
data=pd.read_csv("Churn_Modelling.csv")
data.head()


# # 6. Find the outliers and replace the outliers

# In[15]:





# In[26]:


matplotlib.rcParams['figure.figsize']=(1,10)
data.sample(5)


# # 7. Check for Categorical columns and perform encoding.

# In[27]:


data.columns

headers=['RowNumber','CustomerID','Surname','CreditScore','Geography',
 'Gender','Age','Tenure','Balance','NumofProducts','HasCard'
 'IsActiveMember','EstimatedSalary','Exited']

data.head()


# # 8. Split the data into dependent and independent variables.

# In[28]:


x = data.iloc[:,:-1].values
print(x)
y = data.iloc[:,-1]._values
print(y)


# # 9. Scale the independent variables 

# In[37]:



d = data[['Balance','Age']]
sns.heatmap(d.corr(), annot=True)
sns.set(rc={'figure.figsize':(40,40)})


# # 10. Split the data into training and testing

# In[39]:


from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split

x=data.iloc[:, 1:2].values
y=data.iloc[:,2].values

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print('Row count of x_train table'+'-'+str(f"{len(x_train):,}"))
print('Row count of y_train table'+'-'+str(f"{len(y_train):,}"))
print('Row count of x_test table'+'-'+str(f"{len(x_test):,}"))
print('Row count of y_test table'+'-'+str(f"{len(y_test):,}"))


# In[ ]:




