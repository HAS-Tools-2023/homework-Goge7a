#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)

# 1.1 What is the length of x? 
print(x.size)
# Comprehension question is this an attribute or a method or a function of x? How do we know?
# It is an attribute since there are no parenthesis 
#%%
# 1.2 Get the first value out of x and print it: 
x[0]
#%%
# 1.3. Get the last value out of x and print it?
x[26]
#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?
x[:5]
x[22:]

#%%
# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
y = None
print(y)

#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 

#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])
y[1,1]
#%%
# 2.3. Get the first row out of y and print it?

# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 

#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)

# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get its size (i.e. with two lines of code). And next where you combine thos commands into one line of code

#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns that has values 0-9


# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 

# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   (Hint: you could do this with either addition or multiplication)

#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))

# 4.1 Use 'sum' to print the total of z

#Comprehension question -- is 'sum' a function a method or an attribute?  

#%%
# 4.2. Print the sum along the first dimension of z?

## Comprehension question -- is the 'first dimension' the rows or the columns of z? 


# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numberd did you get back?)

# How does this compare to the shape of z? 

#%%
#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np
# %%
a = np.array([5,7,9,7,6,4,5])
b = np.array([6,3,4,8,9,7,1])
c = np.zeros(7)

for i in range(7):
   c[i]=max(a[i],b[i])
print(c)
    
    
# %%
a = np.array([5,7,9,7,6,4,5])
b = np.array([6,3,4,8,9,7,1])
c = np.zeros(7)
