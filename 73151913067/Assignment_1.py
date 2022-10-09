#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[2]:


s = "Hi there Sam!"


# In[3]:


out = s.split()
print(out)


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[4]:


planet = "Earth"
diameter = 12742


# In[5]:


print("The diameter of {planet} is {diameter} kilometesrs".format(planet="Earth",diameter=12742))


# ## 3. In this nest dictionary grab the word "hello"

# In[6]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[7]:


print(d['k1'][3]['tricky'][3]['target'][3])


# # Numpy

# In[8]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[9]:


arr = [0] * 10
print (arr)


# In[10]:


arr1 = [5]*10
print(arr1)


# ## 5. Create an array of all the even integers from 20 to 35

# In[12]:


import numpy as np
even_arr=np.arange(20,35,2)
print(even_arr)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[13]:


import numpy as np
matrix =  np.arange(0,9).reshape(3,3)
print(matrix)


# ## 7. Concatenate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[14]:


import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a,b)))


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[15]:


import pandas as pd


# In[21]:


array=[["d1","d2"],["d3","d4"],["d5","d6"]]
dataframe = pd.DataFrame (array,columns=['   column1','   column2'])
print(dataframe)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[27]:


import pandas as pd
dates = pd.date_range('1-1-2023','2-10-2023',freq = 'D')
for val in dates:
  print(val);


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[29]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[30]:


import pandas as pd

dataframe = pd.DataFrame(lists, columns = ['c1', 'c2','c3'])

print(dataframe)


# In[ ]:




