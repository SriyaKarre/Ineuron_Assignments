#!/usr/bin/env python
# coding: utf-8

# 1.What exactly is []?
# 
# Ans.The empty list value, which is a list value that contains no items.

# 2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[1]:


# solution by changing the value in index 3
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam


# Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.

# 3.What is the value of spam[int(int(3 * 2) / 11)]?

# In[2]:


spam = ['a', 'b','c','d']
spam[int(int('3' * 2) / 11)] # spam[int(33/11)] = spam[3]


# 4.What is the value of spam[-1]?

# In[3]:


spam = ['a', 'b','c','d']
spam[-1] # negative index # d


# 5.What is the value of spam[:2]?

# In[4]:


spam[:2] # c


# *Let's pretend bacon has the list [3.14, 'cat' 11, 'cat' True] for the next three questions.*

# 6.What is the value of bacon.index('cat')?

# In[6]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat') # it returns the index of first occurrence of 'cat'


# 7.How does bacon.append(99) change the look of the list value in bacon?

# In[7]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99) # append adds the item at the end of the list
bacon
     


# 8.How does bacon.remove('cat') change the look of the list in bacon?

# In[12]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat') # remove first occurrence of item
bacon
     


# 9.What are the list concatenation and list replication operators?

# Ans.( * ) is list replication operator ( + ) is list concatination operator

# In[10]:


l1 = [1,4]
l2 = [2,5]
# list concatination
l1+l2
     


# In[11]:


l1 = [7,4]

# list replication
l1*3


# 10.What is difference between the list methods append() and insert()?
# 

# Ans.append() Appends object to the end of the list
# insert() Insert object before index

# In[13]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99) # append adds the item at the end of the list
bacon


# In[14]:


# solution by inserting value in 3rd index
spam = [2, 4, 6, 8, 10]
spam.insert(2,'hello')
spam


# 11.What are the two methods for removing items from a list?

# In[16]:


#remove(item) - removeds first occurence of a item
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')
bacon
     


# In[17]:


#pop() - Remove and returns item at index (default last).
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.pop()
bacon


# 12.Describe how list values and string values are identical.
# 
# Ans.
# 1.Both lists and strings can be passed to len()
# 2.Have indexes and slices
# 3.Can be used in for loops
# 4.Can be concatenated or replicated
# 5.Can be used with the in and not in operators

# 13.What's the difference between tuples and lists?
# 
# Ans.Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets, [ and ]
# Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses, ( and )

# 14.How do you type a tuple value that only contains the integer 42?

# In[18]:


tuple = (42,)
tuple


# 15.How do you get a list value's tuple form? How do you get a tuple value's list form?

# In[3]:


l1 = [2,3]
l = tuple(l1)

l


# In[4]:


t1 = (3,4)
t = list(t1)
t


# 16.Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# Ans. They contain references to list values

# 17.How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# 
# Ans . The copy.copy() function will do a shallow copy of a list,
# The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list

# In[ ]:




