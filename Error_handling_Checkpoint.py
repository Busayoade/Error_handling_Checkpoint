#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Index error,
try:
    mylist=[14, "hello", 967]
    mylist[6]
except IndexError:
    print("There is an error")


# In[12]:


#IndexError is an exception in python that occurs when we try to access an element from a list or
#tuple from an index that is not present in the list.
try:
    import Pandas as pd
    import NumPy as np
except:
    print("This is an IndexError")


# In[11]:


#Syntax errors are mistakes in the code that violate the rules of the programming language
try:
    print("python errors")
except SyntaxError:
    print("Invalid syntax")


# In[13]:


#A KeyError generally means the key doesn't exist
try:
    mydictionnary={True:"hello",False:"bye", '3':"python"}
    mydictionnary['True']
except:
    print("Error")


# In[15]:


#Indentation error
try:
    i=14
    while i<78:
        print(i)
        i+=1
except:
    print("error")


# In[16]:


#Indentation error is a common error in Python 
#coding that occurs when tabs or spaces are misplaced or used incorrectly
try:
    it=iter([1,2,3])
    next(it)
    next(it)
    next(it)
    next(it)
except:
    print("An error occured")


# In[23]:


#The TypeError object represents an error when an operation could not be performed, 
#typically (but not exclusively) when a value is not of the expected type
try:
    '15'+15
except:
    print("This is a type error")


# In[ ]:





# In[22]:


#NameError is a kind of error in Python that occurs when executing a function, variable, library, or
#string without quotes that have been typed in the code without any previous Declaration. 
try:
    int("python")
except:
    print("This a name error")


# In[21]:


#A ZeroDivisionError in Python occurs when we try to divide a number by 0.
try:
    x=19/0
except:
    print("This is a zero division error ")


# In[ ]:




