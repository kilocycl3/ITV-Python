#!/usr/bin/env python
# coding: utf-8

# In[22]:


my_dict = {'name': 'John', 1: [2, 4, 3],"sal":38000,"location":'mumbai'}

print(f"Given dictionary is {my_dict}")


# In[23]:


print(f"\nGet all keys from dictionary: {my_dict.keys()}")


# In[24]:


print(f"\nGet all values from dictionary: {my_dict.values()}")


# In[25]:


print(f"\nGet all key: values pairs from dictionary: {my_dict.items()}")


# In[26]:


my_dict.update({"pincode": 400093})
print(f"\nUpdated dictionary after inserting pincode is {my_dict}")


# In[27]:


my_dict.update({"name": "Amit"})
print(f"\nUpadating the name from `John` to `Amit` in the dictonary: {my_dict}")


# In[28]:


print(f"\nPopping the salary from dictonary: {my_dict.pop('sal')}")


# In[29]:


print(f"\nPopping key-value pair from dictonary: {my_dict.popitem()}")


# In[31]:


print(f'\nGiven dictonary is {my_dict}')
print(f"Accessing the second element from list in the dictonary: {my_dict[1][1]}")


# In[32]:


copied_dict = my_dict.copy()

print(f"\n Copy of dictionary is {copied_dict}")


# In[33]:


copied_dict.clear()

print(f"\n Copy of dictionary after removing all elements: {copied_dict}")


# In[ ]:




