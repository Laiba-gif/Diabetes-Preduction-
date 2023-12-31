# -*- coding: utf-8 -*-
"""DIABETETES PREDICTION

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1noqqPp0QOc8EmVzbNK9VajQKMUMvjF2s

# ***DIABETETES PREDICTION ***

Laiba Kashif (B19203038)

## **OBJECTIVES**

1. Import the diabetes data.
2. Check whether it has null values.
3. Check how many columns and rows the dataset has.
4. Check each columns datatype
5. Generates statistics for each columns.
6. Check the data imbalance
7. Explore each varaiable and identify the shape and outliers.
8. Create scatterplotes for each varaibale to viusualize the relationship.
9. Generate correlation for each variable.
10. Visualize the correlation.
11. Get an idea how the target variable is different for each columns of diabetic and non-diabetics patient.
12. Create X and Y vaariables for machine learning.
13. Split the data set in test and train.
14. Run the below mentioned model and find accuracy , classification report and confusion matric a. LOGISTIC REGRESSION b.SVM
15. making predication through model
16. finds variable that impact most .

# DATA DESCRIPTION
* **Pregnancies**: Number of times pregnant.

* **Glucose**: A normal fasting blood glucose level is lower than 95 mg/dL (5.3 mmol/L). One hour after drinking the glucose solution, a normal blood glucose level is lower than 180 mg/dL (10 mmol/L). Two hours after drinking the glucose solution, a normal blood glucose level is lower than 155 mg/dL (8.6 mmol/L)
*  **BloodPressure** diastolic pressure (the bottom number) is the pressure of the blood in your arteries between beats, when your heart relaxes,normal range is 80 and below
* **SkinThickness** The average TSF thickness was 18.7 ± 8.5 mm. Women have much higher TSF thickness than men (23.6 ± 7.5 mm vs 14.3 ± 6.8 mm). The mean BMI, MAMC, and MUAC were 27.6 ± 3.4 kg/m2, 18.7 ± 8.5 mm, 26.4 ± 4.1 cm, and 32.3 ± 4.6 cm, respectively
* **Insulin** Before a meal: 80 to 130 mg/dL. Two hours after the start of a meal: Less than 180 mg/dL
* **BMI** Body mass index, normal range 18.5 to 24.9
* **Diabetes Pedigree Function** indicates the function which scores likelihood of diabetes based on family history.

### **IMPORTING LIBRARIES**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

"""### **IMPORTING DATASET**"""

data = pd.read_csv("/content/diabetes1.csv")

"""## **EXPLORING DATA**"""

data.isna().sum()

data.head()

data.iloc[0]

data.shape

data.info()

data.columns

data.describe()

"""**describe** **function** **tells** **us**:

* The mean value is less then the median in case of: '**BloodPressure', 'SkinThickness', 'BMI**'
* The mean value is more then the median in case of: '**Pregnancies', 'Glucose', 'Insulin', 'DiabetesPedigreeFunction', 'Age'**
and much more in case of: '**Insulin', 'DiabetesPedigreeFunction',**
* There is notably a large difference between **75th** **percentile and max values** of the predictors: 'Pregnancies', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction' 'Age'
* The observations 1 and 2 suggests that there are extreme values-**Outliers** in our data set.
Target variable/Dependent variable ('Outcome') is discrete, categorical, binary in nature. (0 = No disease, 1 = Disease
"""

data["Outcome"].value_counts()

"""This outcome shows that "0" represent non-diabetes persons and "1" represent diabetes persons. by this outcome observed that diabetes value is half of non diabetes so we can say that there is a diabete person but our model is also predicting that here is a non diabetic person as well. so we have a chance of good prediction."""

data["Outcome"].value_counts(normalize= True)

"""bascically this outcome gives the absoulate value, that 65% value incidacte non diabetics persons and almost 35% value represent diabetics one.

## **DATA VISUALISATION**
"""

sns.countplot(x='Outcome',data= data)

"""plot above outcome,0 has more values and 1 has less values as non diabetes persons is half of diabete one."""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.Pregnancies[data.Outcome==0])
sns.distplot(data.Pregnancies[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
plt.title('Pregnancies vs Diabetes')
sns.boxplot(data = data , x = 'Outcome', y = 'Pregnancies', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.show()

"""**Diabetes is more common in women who have had more pregnancies**"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.Glucose[data.Outcome==0])
sns.distplot(data.Glucose[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'Glucose', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('Glucose vs Diabetes')
plt.show()

"""**People with diabetes have much higher blood glucose levels**"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.BloodPressure[data.Outcome==0])
sns.distplot(data.BloodPressure[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'BloodPressure', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('BloodPressure vs Diabetes')
plt.show()

"""Here in the Blood Pressure variable we can see a slight difference above the positive value but nothing too discrepant.
People with diabetes have slightly higher blood pressure
"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.SkinThickness[data.Outcome==0])
sns.distplot(data.SkinThickness[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'SkinThickness', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('SkinThickness vs Diabetes')
plt.show()

"""Practically the same thing in both values"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.Insulin[data.Outcome==0])
sns.distplot(data.Insulin[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'Insulin', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('Insulin vs Diabetes')
plt.show()

"""Here we have a slight difference of Insulin in the positive value, but I believe that nothing too discrepant"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.BMI[data.Outcome==0])
sns.distplot(data.BMI[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'BMI', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('BMI vs Diabetes')
plt.show()

"""This BMI variable is a bit interesting, it has the same pattern as the glucose variable but a little lighter.
 People with diabetes have higher **BMI**
"""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.DiabetesPedigreeFunction[data.Outcome==0])
sns.distplot(data.DiabetesPedigreeFunction[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'DiabetesPedigreeFunction', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('DiabetesPedigreeFunction vs Diabetes')
plt.show()

"""Another interesting variable, we have some higher values ​​that have a positive value."""

plt.figure(2)
plt.figure(figsize=(15,9))
plt.subplot(121)
sns.distplot(data.Age[data.Outcome==0])
sns.distplot(data.Age[data.Outcome==1])
plt.legend(['Non Diabetic', 'Diabetic'])
plt.subplot(122)
sns.boxplot(data = data , x = 'Outcome', y = 'Age', palette='rocket').set_xticklabels(['Without Diabetes', 'Diabetes'])
plt.title('Age vs Diabetes')
plt.show()

"""**Older people, especially those over 30, are more prone to diabetes**

**From that graph we can see:**

* "Pregnancies", "Insulin", "DiabetesPedigreeFunction" and "Age" have a right-skewed distribution.
* *In contrast, "Glucose," "BloodPressure," "SkinThickness" and "BMI" have a normal distribution.*
* *We can see that the ages of our patients ranged from just over 10 to even 90 years old, showing a very high range of age*
*  It is also interesting to note that having more pregnancies correlates with a higher likelihood of being diagnosed with diabetes

**Looking at the boxplot**

our continuous variables we can see that we have some variables that have some outliers, but I believe that this is not something very worrying, for now we will continue without removing them

## ***Create scatter charts between the pair of variables to understand the relationships***
"""

sns.pairplot(data,hue='Outcome')
ax=plt.figure(figsize=(15,12))
plt.show()

"""The scatter plot is said to be in a relation with the variables if the points are in a narrow band (up/down) describing the type of relationship



 *   Through the pairplot, we observe in the **pregnancies** column that women who are pregnant more than 10-12 times are more likely to have diabetes which in result have higher glucose levels.

*   Also people who have diabetes have higher minimum **Glucose** levels than people who don't, in other cases people who have higher **SkinThickness** and lower **Insulin** levels tend to develop diabetes.

* The **BMI** serves as an measure to indicates the ideal range of Body Mass of an individual, the ideal range is **18.5 to 24.9**, people with diabetes have higher ranges resulting to obese or extremely obese states.

*  There are also some cases in the data which pictures the diabetes are through family history. Though **BMI** and **DiabetesPedigreeFunction** shows some relationship which could mean that structure of a body can be genetic which if not cared can result to diabetes.

* We see people develop diabetes in their twenties and atmost their seventies, no cases are seen above **70-75** which can state that the people who had diabetes were cured or they did not survive past it.

* People with diabetes have higher **Glucose** min-mid-max levels
*  People with **Glucose** levels above 125 and **BloodPressure** between 40 to 110

# ***Perform correlation analysis. Visually explore it using a heat map***
"""

data.corr()

"""for visualization we use corelation matrix in this we fin the corelation between different variables."""

corr_matrix = data.corr()
ax=plt.subplots(figsize=(15,12))
sns.heatmap(corr_matrix,fmt='.2f',annot=True,linecolor='white',linewidths=0.5)
plt.show()

"""The correlation heatmap signifies the correlation between the variables,

*  **0** indicates neutral
*  **1** indicates positive correlation
* **-1** indicates negative correlations.


The 1.00 values are the same variables which are cross referenced in the heatmap, they are always positively related to themselves.

* If we take a look into our graphs above we can make some observations:

2 of the 3 features which we considered in our intitial assumptions proven to be indeed the most significant ones having connection to the disease:

* Glucose level
* BMI
Diabetes Pedigree function although ended up not so descriptive as we anticipated towards the Outcome, being only the 5th if we sort our correlations.

The 4 most significant indicators in diabetes incidence according to correlation to the Outcome:

* Glucose level
* BMI
*  Age
* Pregnancies

***With a value of 0.49, the highest correlation with "Outcome" is with "Glucose." This is followed, as we noted from the previous graphs, by "BMI" and "Age"***

**checking the mean values of depending on their category (0 or 1)**
"""

data.groupby('Outcome').mean()

"""In below chart it is the general overview of the given data set "0" represents  non diabetes and "1" represents diabetes.This table shows the means of pesons having diabetes and non daibetes

***We explored the data in depth and understood how they behave. It is time to look for a model that can make reliable predictions on that dataset.***
"""

X = data.drop(columns='Outcome', axis=1)
Y = data['Outcome']

"""## **DATA STANDARDIZATION**"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
Standardized_data = scaler.transform(X)
print(Standardized_data)

X= Standardized_data
Y= data['Outcome']
print(X)
print(Y)

"""### **TRAIN TEST SPLIT**"""

from sklearn.model_selection import train_test_split



X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=.2,random_state=123)

print(X.shape,X_train.shape,X_test.shape)

"""# **LOGISTIC REGRESSION MODEL** **EVALUATION**"""

from sklearn.linear_model import LogisticRegression

logreg= LogisticRegression()

logreg.fit(X_train , Y_train)

logreg_predict = logreg.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(Y_test, logreg_predict)

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

print(classification_report(Y_test, logreg_predict))

"""ACCURACY SCORE OF LOGISTIC REGRESSION IS **79%**"""

print(confusion_matrix(Y_test, logreg_predict))

"""* True Positive --> 87
* True Negative --> 35
* False Positive --> 9
* False Negative --> 23
* precision --> 122 / (122 + 9) = 0.93
* recall --> 122 / (122 + 23) = 0.84

* Model's true predicts

True positive is 87, It means our model predict 1 and the true label was 1. Model successfully predict 87 diabetics.


True negative is 35. It means our model predict 0 and the true label was 0. Model successfully predict 35 non-diabetics.
* Model's false predicts

False positive is 9. It means our model predict 1 and the true label was 0. So the patient wasn't diabetic but model said "he/she is diabetic."

False negative is 23. It means our model predict 0 and the true label was 1. So the patient was diabetic but model said "he/she is not diabetic."

# **# SVC MODEL EVALUTION**
"""

from sklearn import svm

svm_model = svm.SVC(kernel='linear')

svm_model.fit(X_train, Y_train)

Y_pred= svm_model.predict(X_test)

accuracy_score(Y_test,Y_pred)

print(classification_report(Y_test,Y_pred ))

"""SUPPORT VECTOR MACHINE SHOWS **81%** ACCURACY RESULTS"""

print(confusion_matrix(Y_test,Y_pred ))

"""* True Positive --> 88
*True Negative --> 37
* False Positive --> 8
* False Negative --> 21
* precision --> 125 / (125 + 8) = 0.93
* recall --> 125 / (125 + 21) = 0.85

* Model's true predicts

True positive is 88, It means our model predict 1 and the true label was 1. Model successfully predict 88 diabetics.


True negative is 37. It means our model predict 0 and the true label was 0. Model successfully predict 37 non-diabetics.
* Model's false predicts

False positive is 9. It means our model predict 1 and the true label was 0. So the patient wasn't diabetic but model said "he/she is diabetic."

False negative is 21. It means our model predict 0 and the true label was 1. So the patient was diabetic but model said "he/she is not diabetic."

The results are very similar to each other.
#**## I choose SVC as the model.SVC shows 81 % accuracy where as logistic regression shows 79% accuracy . In fact support vector machines allow good tuning, and having little data they perform very well, both in time factor and metrics**

# **### MAKING PREDICTIVE SYSTEM**
"""

input_data = (5,123,73,19,175,25.8,0.587,51)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
print(std_data)
prediction = svm_model.predict(std_data)
print(prediction )
if (prediction [0] == 0):
  print("the person is not diabetic")
else:
  print("the person is daibetic")

"""# **IMPORTANT FEATURE**"""

from sklearn.inspection import permutation_importance
importances = pd.Series(permutation_importance(svm_model, X_test, Y_test, random_state=123).importances_mean, index=X_test.columns)
importances.sort_values(ascending=False, inplace=True)

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(x=importances.values, y=importances.index, ax=ax , linewidth=2, edgecolor="black")

ax.set_xlabel("Permutation Importance")
ax.set_title("Feature Importances - SVC")

plt.show()

"""The most important feature, as prediction during is "**Glucose**". It is followed, surprisingly, by "**BMI**," which is the second most important.
Note that with these data, the columns "**Insulin**" and "**Skinthickness**" have a least values

# **OVERVIEW**
In this project we are going to evaluate the diabetic patient data wheater the patient is diabetic or
not.
STEPS EVOLVE IN MAKING THE MODEL:

IMPORT THE DIABETES DATA:
Data = pd.read_csv(“/content diabetes1.csv”)
CHECK WHETHER IT HAS NULL VALUES:
•CODE: data.isna().sum()
This data contain no null values.how ever data can be different it May not contain null values at this
stage.
CHECK HOW MANY COLUMNS AND ROWS THE DATASET HAS:
•CODE: data.head()
This will give us the rows and columns of the data set.
However we can access any particular row or column by using indexing the data set.
•CODE: data.iloc[0]
This will give us the zero row of the data.
Data.shape tells the data contain 768 rows and 9 columns.

CHECK EACH COLUMNS DATA TYPE:
CODE: data.info()
This will tells the data columns contain float values or it is an integer.
We can also get the names of the columns in a list format by using “data.columns”

GENERATES STATISTICS FOR EACH COLUMNS:
•CODE: data.describe()
It will divide the data into rows and columns defining statistically.This help us to look into data in more
depth providing the mean, median,SD, The percentiles , maximum and minimum values which can
help in interpretation.
CHECK THE DATA IMBALANCE:
•CODE: data[“Outcome”].value_counts()
Variable 0 which is 500 shows person has diabetics and 1 which is 268 shows nondiabetics.
To get the percentage we can use the code “data[“Outcome”].value_counts(normalize= True)
Further we can visualize this data graphically by using the code”sns.countplot(x=’Outcome’,data=
data)”.

EXPLORE AND IDENTIFY THE SHAPE AND OUTLIERS:
We have visualize the data by making histogram and box plot for each column in the data i-e
‘Pregnancies’, ‘Glucose’, ‘BloodPressure’, ‘SkinThickness’, ‘Insulin’,’BMI’, ‘DiabetesPedigreeFunction’,
‘Age’, ‘Outcome’.
Which detect the outliers in each column the normality in histogram bell shape curved in each
column.outlier is a value or observation that is distinct from the other observation which should be
removed.

CREATE SCATTER PLOT FOR EACH VARAIBALE TO VIUSUALIZE THE RELATIONSHIP:
•CODE: sns.pairplot(data,hue=’Outcome’)
Shows the scatter plots of the columns in the dataset.

PERFORM CORRELATION ANALYSIS 9.VISUALLY EXPLORE IT USING A HEAT MAP:
CODE: data.corr()
This gives the table with shows the correlation among the variable.we have visualize this by making a
correlation matrix for better understanding.

GET AN IDEA HOW THE TARGET VARIABLE IS DIFFERENT FOR EACH COLUMNS OF DIABETIC AND NONDIABETIC S PATIENT:
CODE: data.groupby(‘Outcome’).mean()
Which shows the outcome 0 and 1 is significantly different for each column.

CREATE X AND Y VAARIABLES FOR MACHINE LEARNING:
We have divide the data into two variables shown below
X = data.drop(columns=’Outcome’, axis=1)
Y = data[‘Outcome’]

SPLIT THE DATA SET IN TEST AND TRAIN:
Import the library sk.learn
From sklearn.model_selection import train_test_split
We have divided the data for testing and training .
MODELING
Firstly we have applied logistics regression Then SVM
To both the variables.
Logreg= LogisticRegression()
Logreg.fit(X_train , Y_train)
We have checked the accuracy of our model by using
From sklearn.metrics import accuracy_score
Accuracy_score(Y_test, logreg_predict)
0.7922077922077922
The model produces 79% accuracy which is convenient to proceed further.

.CLASSIFICATION REPORT AND CONFUSION MATRIX:
From sklearn.metrics import classification_report
From sklearn.metrics import confusion_matrix
Which tells about the performance of the classification by using formula.
then we check the prdiction and most imortant features in our data set .
"""