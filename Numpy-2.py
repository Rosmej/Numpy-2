
# coding: utf-8

# In[20]:


import numpy as np

Dataset =[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]

def movingaverage(values,window):
    weights=np.repeat(values,window)/window
    smas=np.convolve(values,weights,'valid')
    return smas

print(movingaverage(Dataset,3))

