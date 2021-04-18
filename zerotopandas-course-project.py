#!/usr/bin/env python
# coding: utf-8

# # Store Sales Analysis
# 
# In this project we take a dataset of a Super Store and analyze its sales,of which category of which region and infer meaningful insights to the store in order to improve their overall Sales.

# ## Downloading the Dataset
# 
# We download the dataset from kaggle.

# In[68]:


get_ipython().system('pip install jovian opendatasets --upgrade --quiet')


# Let's begin by downloading the data, and listing the files within the dataset.

# In[69]:


# Change this
dataset_url = 'https://www.kaggle.com/rohitsahoo/sales-forecasting'


# In[70]:


import opendatasets as od
od.download(dataset_url)


# The dataset has been downloaded and extracted.

# In[71]:


data_dir = './sales-forecasting'


# In[72]:


import os
os.listdir(data_dir)


# Let us save and upload our work to Jovian before continuing.

# In[73]:


project_name = "zerotopandas-course-project-store-sales-analysis" # change this (use lowercase letters and hyphens only)


# In[74]:


get_ipython().system('pip install jovian --upgrade -q')


# In[75]:


import jovian


# In[76]:


jovian.commit(project=project_name)


# ## Data Preparation and Cleaning
# 
# Here we have taken the data of the sales of a store in different regions in order to explore and analyze various trends in the sales.

# Initially,read the data which is in the form of csv by using pandas library.By using the head() method,we can see the first few rows and columns of the dataset.

# In[77]:


import pandas as pd
data=pd.read_csv('train.csv')
data.head(5)


# Now in order to know how many rows and columns are present in the dataset, we make use of the .shape method and we can observe that there are 9800 rows and 18 columns

# In[78]:


data.shape


# In order to know the data types of each of the columns we can use .dtypes method. 

# In[79]:


data.dtypes


# We drop the duplicate values by using drop_duplicates() method. 

# In[80]:


data.drop_duplicates()


# Similarly we drop the null values by using dropna() method.After droping the null values we can observe that the total number of rows changed to 9789 rows.

# In[81]:


data.dropna()


# In[82]:


data.info()


# In[83]:


import jovian


# In[84]:


jovian.commit()


# ## Exploratory Analysis and Visualization
# 
# Here we analyze various trends in the Store Sales dataset.

# Let's begin by importing`matplotlib.pyplot` and `seaborn`.

# In[85]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# To find the average sales of the store,we compute the mean of the Sales column.

# In[86]:


average_sales = data['Sales'].mean()
print('The average sales(in$) of the store is: ',int(average_sales))


# Now obtain the regions with sales done above the average sales.We can observe that in total there are 2324 orders with Sales above the average sale price.

# In[87]:


sales_above_average=data[data['Sales']>230]
sales_above_average


# Similarly we can obtain the orders that are below the average Sale price.We can observe that there in 7476 orders in total whose Sales are less than the average sale price.

# In[88]:


sales_below_average=data[data['Sales']<230]
sales_below_average


# Here we can observe that in order whose Sales are above average sale price,majority of the orders belong to Consumer segment.

# In[89]:


sales_above_average['Segment'].value_counts().plot(kind='bar')


# Likewise we can observe that in order whose Sales are below average sale price,majority of the orders belong to Consumer segment.

# In[90]:


sales_below_average['Segment'].value_counts().plot(kind='pie')


# We can observe that most of the orders having sale price above average,were shipped by Standard Class

# In[91]:


sales_above_average['Ship Mode'].value_counts().plot(kind='bar')


# Similarly we can observe this thrend in order with sales below average sale price.

# In[92]:


sales_below_average['Ship Mode'].value_counts().plot(kind='pie')


# Let us save and upload our work to Jovian before continuing

# In[93]:


import jovian


# In[94]:


jovian.commit()


# #### Q1: In the sales_above _average table, find how many of them are office supplies.

# In[95]:


office_supplies=sales_above_average[sales_above_average['Category']=='Office Supplies']
office_supplies


# In[96]:


print('The orders above average sale price with the category of office supplies: ',office_supplies.Category.count())


# #### Q2: Of these office supplies find from which region these orders came from.

# In[97]:


office_supplies['Region'].value_counts().plot(kind='bar')


# #### Q3: In the sales_above _average table, find how many of them are of the category Furniture.

# In[98]:


furniture_sales=sales_above_average[sales_above_average['Category']=='Furniture']
furniture_sales


# In[99]:


print('The orders above average sale price with the category of furniture: ',furniture_sales.Category.count())


# #### Q4: Of the entire Store Sales data set,what is the category with most number of orders

# In[100]:


data['Category'].value_counts().plot(kind='pie')


# #### Q5: What is the sum of total sales pertaining to the office supplies?

# In[101]:


sales_office_supplies=data[data['Category']=='Office Supplies']
sales_office_supplies


# In[102]:


print('The sum of total sales(in$) pertaining to the office supplies: ',sales_office_supplies['Sales'].sum())


# Let us save and upload our work to Jovian before continuing.

# In[103]:


import jovian


# In[104]:


jovian.commit()


# ## Inferences and Conclusion
# 
# Hence we have analyzed and visualized the Store Sales dataset.Through our observations we can observe that:
# 
# 1.We calculated the average Sales of the Store in all the regions.
# 
# 2.We have segregated the sales done above average sale price and below average sale price.
# 
# 3.In the sales done above average sale price, we can observe that most of the orders belong to the Consumer segment.
# 
# 4.The mode of shipping of these orders also mostly Standard Class.
# 
# 5.We have obtained the number of orders of Office Supplies and the regions from which these have been ordered.
# 
# 6.We can also observe that the Category with most number of orders is Office Supplies.

# In[105]:


import jovian


# In[106]:


jovian.commit()


# ## References and Future Work
# 
# Therefore we can provide meaningful insights to the Store that, they need to maintain safety stock levels of Office Supplies which majorly constitute the Sales.
# 
# Also they need to do ground work due to the less number of orders originating from the South region.
# 
# They must also target the Home Office segment in order to improve their Sales.
# 

# In[107]:


import jovian


# In[ ]:


jovian.commit()


# In[ ]:




