#!/usr/bin/env python
# coding: utf-8

# Basic Python
# 

# 1.Split the string

# In[8]:


s = "This is kumar!"
out = s.split()
print(out)


# 2.Use .format() to print the following string.

# In[4]:


planet = "Mercury"
diameter = 78654
print("The diameter of {planet} is {diameter} kilometesrs".format(planet="Earth",diameter=12742))


# 3.In this nest dictionary grab the word "hello"

# In[3]:


Nest_Dic= {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(Nest_Dic['k1'][3]['tricky'][3]['target'][3])


# Numpy

# In[7]:


import numpy as np


# 4.1 Create an array of 10 zeros?

# In[1]:


ARR_Z = [0] * 10
print (ARR_Z)


# 4.2 Create an array of 10 fives?

# In[5]:


ARR_t = [5]*10
print(ARR_t)

5. Create an array of all the even integers from 20 to 35

# In[6]:


import numpy as np
Array_E=np.arange(20,35,2)
print(Array_E)

6. Create a 3x3 matrix with values ranging from 0 to 8

# In[7]:


import numpy as np
Matrix_three =  np.arange(0,9).reshape(3,3)
print(Matrix_three)

7. Concatenate a and b
a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
# In[8]:


import numpy as np
First = np.array([24, 27, 80])
Second = np.array([47, 95, 36])
print(np.concatenate((First,Second)))

Pandas8. Create a dataframe with 3 rows and 2 columns

# In[14]:


import pandas as pd


# In[16]:


array=[["d1","d2"],["d3","d4"],["d5","d6"]]
dataframe = pd.DataFrame (array,columns=['   column1','   column2'])
print(dataframe)

9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[17]:


import pandas as pd
dates = pd.date_range('1-1-2023','2-10-2023',freq = 'D')
for val in dates:
  print(val);

10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[18]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[19]:



dataframe = pd.DataFrame(lists, columns = ['c1', 'c2','c3'])

print(dataframe)

