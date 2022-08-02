# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:23:53 2022

@author: Pablo Moraga
"""


import pandas as pd
import json


data= '''
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85},
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77},
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]
'''


###   we convert from json to dataframe     / using pandas lib 

dataframe = pd.read_json(data)


###   we apply defination of BMI    and add new columns name bmi

"""
Formula 1 - BMI BMI(kg/m2) = mass(kg) / height(m)2
The BMI (Body Mass Index) in (kg/m2)
 is equal to the weight in kilograms (kg) divided by your height in meters squared (m)2.
For example, if you are 175cm (1.75m) in height and 75kg in
weight, you can calculate your BMI as follows: 75kg / (1.75m2) = 24.49kg/m2


""" 
###################
###################  QUESTION  N° 1 
###################
"""  Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk
     from Table 1 of the person and add them as 3 new columns
"""
###################



###   we apply defination of BMI    and add in dataframe new columns name bmi

dataframe['bmi'] = dataframe.apply(lambda x: x.WeightKg/(x.HeightCm/100)**2 , axis=1)


### we create a function for clasificate    Category and livel of Health risk 
### view defination in  table below 

"""
BMI Category            BMI Range (kg/m2)           Health risk

Underweight             18.4 and below               Malnutrition risk
Normal weight           18.5 - 24.9                  Low risk
Overweight              25 - 29.9                    Enhanced risk
Moderately obese        30 - 34.9                    Medium risk
Severely obese          35 - 39.9                    High risk
Very severely obese     40 and above                 Very high risk


"""


### Function category   ( x= bmi ) 
def categoria(x):
    if (x <= 18.4):                       return "Underweight"
   
    elif (x >= 18.5 and x <= 24.9):       return "Normal weight"
   
    elif (x >= 25 and x <= 29.9):         return "Overweight"
   
    elif ( x >= 30 and x <= 34.9):        return "Moderately obese"
   
    elif ( x >= 35 and x <= 39.9):        return "Severely obese"
   
    elif ( x >=40):                       return "Very severely obese"
   
    ### a check 
          
    for i in range (30,36,1):               print (i,categoria(i))
    
        
    for i in range (18,30,1):              print (i,categoria(i))
    
### 

def helthrisk(x):
    if ( x <= 18.4):                    return "Malnutrition risk"
    elif ( x >= 18.5 and x <= 24.9):    return "Low risk"
    elif ( x >= 25 and x <= 29.9):      return "Enhanced risk"
    elif ( x >= 30 and x <= 34.9):      return "Medium risk"
    elif ( x >= 35 and x <= 39.9):      return  "High risk"
    elif ( x >=40):                     return  "Very high risk"

  print ( helthrisk(90.7786))

    ### a check 
          
    for i in range (30,36,1):               print (i,helthrisk(i))
    for i in range (18,30,1):              print (i,helthrisk(i))

### create a copy of  original data
### new table data ( df ) for  add and tranform

df=dataframe

df.dtypes
""" 
Out[822]: 
Gender       object
HeightCm      int64
WeightKg      int64
bmi         float64
dtype: object

"""
###   Create new columns with category and helthrisk 

df['categoria_bmi']=df.bmi.apply(categoria)
df['Risk_bmi']=df.bmi.apply(helthrisk)

### 
###
###

###################
###################  QUESTION  N° 2
###################

"""
2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1, check this is consistent programmatically and add any other observations in
the documentation
"""

df['categoria_bmi'].value_counts()

df.groupby(['categoria_bmi']).agg('count')


############# checking  this is consistent programmatically

###################
###################  QUESTION  N° 3
###################
""" 
3) Create build, tests to make sure the code is working as expected and this can later be
added to an automation build / testing / deployment pipeline
"""
############ Create a new table with 10.000 records ( random )


import numpy as np
import pandas as pd
test_1 = pd.DataFrame(np.random.randint(50,200,size=(10000,2)), columns=list('HW'))

test_1['bmi'] = test_HeightCm.apply(lambda x: x.W/(x.H/100)**2 , axis=1)

###   Create new columns with category and helthrisk 

test_1['categoria_bmi']=test_HeightCm.bmi.apply(categoria)
test_1['Risk_bmi']=test_HeightCm.bmi.apply(helthrisk)



###################
###################  QUESTION  N° 4
###################
"""
4) Write a solid production-grade Python3 Program to solve this problem, imagine this will
be used in-product for 1 million patients. 

"""

def calculator_bmi(W,H ):
    
    b=(W/(H/100)**2)
    c=categoria(b)
    d=helthrisk(b)
      
    data =b,c, d
        
    return data

x = calculator_bmi(87,170)
print(x)

test_2 = pd.DataFrame(np.random.randint(50,200,size=(10000,2)), columns=list('HW'))

test_2.apply(lambda x: calculator_bmi(x['W'], x['H']),  axis=1)


###################
###################  QUESTION  N° 5
###################
"""

Check in the documentation, configuration, code and tests into github and please email
us the link with the URL pattern

"""


