#!/usr/bin/env python
# coding: utf-8

# 
# # Linear Rigression

# Linear regression is used for finding linear relationship between target and one or more predictors. There are two types of linear regression- Simple and Multiple.

# ![alt text](data:image/png;base64,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)

# The core idea is to obtain a line that best fits the data. The best fit line is the one for which total prediction error (all data points) are as small as possible. Error is the distance between the point to the regression line.

# ### Support Libraries

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ### Importing Data

# In[3]:


dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
dataset.head()


# #### Intercept Calculation
# 
# ![alt text](https://miro.medium.com/max/228/1*1evY0PuCUENCpDP_QRplig.png)
# 
# #### Co-efficient Formula
# 
# ![alt text](https://miro.medium.com/max/359/1*Cx1Yej9zLVI1O16I3mODqA.png)

# ## Linear Regression Model

# In[10]:


X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values

# mean of our inputs and outputs
x_mean = np.mean(X)
y_mean = np.mean(Y)

#total number of values
n = len(X)

# using the formula to calculate the b1 and b0
numerator = 0
denominator = 0
for i in range(n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2
    
b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)

#printing the coefficient
print('Slope of the line = {:.3f} \nConstant Coefficient = {:.3f} '.format(b1, b0))


# ### Plotting the Regression Line

# In[13]:


#plotting values 
x_max = np.max(X) + 100
x_min = np.min(X) - 100
#calculating line values of x and y
x = np.linspace(x_min, x_max, 1000)
y = b0 + b1 * x
#plotting line 
plt.plot(x, y, color='red', label='Linear Regression')
#plot the data point
plt.scatter(X, Y, color='c', label='Data Point', alpha=0.5)
# x-axis label
plt.xlabel('Head Size (cm^3)')
#y-axis label
plt.ylabel('Brain Weight (grams)')
plt.legend()
plt.show()


# ## R-Square Scoring

# ![alt text](https://miro.medium.com/max/1432/1*WCaWmRreXCQxLez4yYOy5w.png)

# In[15]:


sumofsquares = 0
sumofresiduals = 0
for i in range(n) :
    y_pred = b0 + b1 * X[i]
    sumofsquares += (Y[i] - y_mean) ** 2
    sumofresiduals += (Y[i] - y_pred) **2
    
score  = 1 - (sumofresiduals/sumofsquares)
print('Acuuracy of the model = {:.4f}%'.format(score*100))

