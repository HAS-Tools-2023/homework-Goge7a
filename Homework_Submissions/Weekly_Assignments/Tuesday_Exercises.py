#%%
import pandas as pd
import numpy as np
import urllib
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LinearRegression

#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum of 
# the dataframe
# If you have time try doing it with and without a for loop 
# (You can either use the function inside your fo loop or put a for loop inside your function)

def mean_column(array): 
    calculate_mean = np.mean(data, axis=0)
    return(calculate_mean)




#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
iris_df = pd.read_csv("iris_df.csv" ,  index_col ='species')
 
# %%
# 1. How do you view the "unique" species in the `iris_df` index?
unique = np.unique(iris_df.index)
# %%
# 2. How do you "locate" only rows for the `versicolor` species?
iris_df.loc['versicolor']
# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
mean_column = iris_df.groupby('species').mean()
iris_df.groupby(iris_df.index).mean()
# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
ax = plt.axes()
ax.scatter(iris_df.loc['versicolor']['sepal length (cm)'],
            iris_df.loc['versicolor']['petal length (cm)'],  marker='o')
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.set_title('Versicolor')

#%%
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)
ax = plt.axes()
iris_type='versicolor'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'], iris_df.loc[iris_type]
           ['petal length (cm)'],  marker='o', color='tomato', label='versicolor')
iris_type = 'setosa'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'], iris_df.loc[iris_type] ['petal length (cm)'],  marker='o', color='darkcyan', label=iris_type)
iris_type = 'virginica'
ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'], iris_df.loc[iris_type]['petal length (cm)'],  marker='o', color='darkviolet', label=iris_type)
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.set_title(iris_type)
ax.legend()

#%%
# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color and use this to function to modify the code you make in 5
def iris_scatter(iris_type, plot_color):
    ax.scatter(iris_df.loc[iris_type]['sepal length (cm)'], iris_df.loc[iris_type]['petal length (cm)'],  marker='o', color=plot_color, label=iris_type)


ax = plt.axes()
iris_scatter(iris_type='versicolor', plot_color='tomato')
iris_scatter('setosa', 'darkcyan')
iris_scatter('virginica', 'darkviolet')
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.legend()


# %%
