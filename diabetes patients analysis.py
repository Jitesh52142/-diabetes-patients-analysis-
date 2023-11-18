#!/usr/bin/env python
# coding: utf-8

# # project : Diabetes patient analysis & visualization
# 
# importing libraries

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# # Load data set 

# In[2]:


data = pd.read_csv("diabetes.csv")


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


data.info()


# In[6]:


data.tail()


# In[7]:


data.shape


# In[8]:


data.dtypes


# In[9]:


data.isnull().sum()


# In[10]:


data.duplicated()


# In[11]:


data.drop_duplicates()


# In[12]:


data.dropna()


# In[13]:


data.describe()


# In[14]:


data.fillna(data.mean())


# In[15]:


data.max()


# In[16]:


data.min()


# In[17]:


correlation_matrix = data.corr()
print(correlation_matrix)


# In[18]:


outcome_grouped = data.groupby("Outcome").mean()
print(outcome_grouped)


# In[19]:


outcome_distribution = data['Outcome'].value_counts()
print("outcome_distribution")
print(outcome_distribution)


# In[20]:


average_age = data["Age"].mean()
print(f"Average Age: {average_age}")


# In[21]:


correlation =data["Glucose"].corr(data["Insulin"])
print(f"correlation between Glucose and Insuline: {correlation}")


# In[22]:


median_bmi_diabetes = data[data['Outcome']==1]['BMI'].median()
median_bmi_no_diabetes = data[data['Outcome']==0]['BMI'].median()
print(f"Median BMI for diabetes: {median_bmi_diabetes}")
print(f"Median BMI for no diabetes:{median_bmi_no_diabetes}")
      


# In[23]:


average_glucous_by_pregnancies = data.groupby('Pregnancies')['Glucose'].mean()
print("average_glucous_by_pregnancies")
print(average_glucous_by_pregnancies)


# In[24]:


standard_deviation_of_BloodPreasure = data[data['Age']>40]['BloodPressure'].std()
print(f"standard deviation of BloodPreasure for age > 40:{standard_deviation_of_BloodPreasure}")


# In[25]:


kurtosis_pdf = data['DiabetesPedigreeFunction'].kurtosis()
print(f"DiabetesPedigreeFunction.kurtosis : {kurtosis_pdf}")


# # Data Viualization

# In[26]:


plt.hist(data['Glucose'], bins=20)
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.title('Glucose Distribution')
plt.show()


# In[27]:


sns.countplot(data =data, x ='Outcome')
plt.xlabel('Outcome')
plt.ylabel('count')
plt.title('distribution of Outcome')
plt.show()


# In[28]:


sns.pairplot(data=data,hue='Outcome')
plt.show()


# In[29]:


sns.lineplot(data=data, x = 'Age',y = 'Pregnancies')
plt.xlabel('Age')
plt.ylabel('pregancies')
plt.title('Age vs pregnancies')
plt.show()


# In[30]:


sns.boxplot(data=data , x = 'Outcome' , y='Age')
plt.xlabel('Outcome')
plt.ylabel('Age')
plt.title('Age distribution by outcome')
plt.show()


# In[31]:


sns.scatterplot(data=data, x ='Glucose', y ='BMI', hue='Outcome')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.title('Glucose vs BMI')
plt.show()


# In[32]:


sns.violinplot(data=data, x='Outcome',y='Age')
plt.xlabel('outcome')
plt.ylabel('Age')
plt.title('Age Distribution by outcome')
plt.show()


# In[33]:


corr_matrix = data.corr()
sns.heatmap(corr_matrix,annot=True)
plt.title('corrilation matrix heatmap')
plt.show()


# In[34]:


sns.histplot(data['SkinThickness'],bins=20 , kde=True)
plt.xlabel('Skinthickness')
plt.ylabel('density')
plt.title('Skinthickness distribution')
plt.show()


# In[35]:


Outcome_counts = data['Outcome'].value_counts()
plt.pie(Outcome_counts , labels = ['No Diabetes', 'Diabetes'],autopct = '%1.1f%%')
plt.title('Outcome Distribution')
plt.show()


# In[36]:


sns.lineplot(data=data, x='Age', y= 'BMI' , hue='Outcome',ci=None)
plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('BMI by age')
plt.show()


# In[37]:


sns.scatterplot(data=data, x = 'Age', y = 'BMI',size= 'Insulin',hue = 'Outcome')
plt.xlabel = ('Age')
plt.ylabel = ('BMI')
plt.title('BMI vs Age (Insulin as Bubble size )')
plt.show()


# In[59]:


data['Glucose_bins'] = pd.cut(data['Glucose'],bins = [0,80,120,160,200,300],labels = ['<80', '80-120','120-160','120-200','200+'])
glucose_counts = data['Glucose_bins'].value_counts()
glucose_counts.plot(kind='bar')
plt.show()


# In[ ]:





# In[ ]:




