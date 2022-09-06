import pandas as pd
import datetime as dt
import uuid 
import numpy as np

## 1. Load data into python
#slm = School Leanning Modalities
slm = pd.read_csv('hha-data-cleaning\data\School_Learning_Modalities.csv')

## 2. get a count of the number of rows and columns
slm.shape

## 3. Print out of the column names 
list(slm)

## clean the data

## 4. Cleans the column names
## 5. Cleans the strings that might exist within each column (remove all special characters and whitespace ' ' from column names)
slm.columns = slm.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(slm)

## 6. Assesses white space or special characters (replace all whitespace in column names with an underscore)
slm.columns = slm.columns.str.replace(' ', '_')

############## COLUMN TYPES ##############


# get list of column types 
## want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
slm.dtypes

##7. Converts the column types to the correct types (e.g., DOB field is datetime and not object) 

# convert date column to datetime format
slm['Week'] = pd.to_datetime(slm['Week'])
# convert date column to datetime format like this: '%Y_%M_%D'
slm['Week'] = pd.to_datetime(slm['Week'], format='%Y_%M_%D')
# determine if date is on weekday or weekend
slm['Week'] = slm['Week'].dt.dayofweek

##8. Look for duplicate rows and remove duplicate rows 
slm.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)



########## MISSING DATA ##########

##9. Assess missingness (count of missing values per column) (get a count of missing values in each column)
slm.isnull().sum()

####### ADDING DATA #######

## 10. New Data Field
#adding a new column of boolean values based on another column data 
slm['modality_inperson'] = np.where(slm["Learning_Modality"] == 'In Person', True, False)

# confirm the new column and that it is a boolean
slm.dtypes

slm.to_csv(hha-data-cleaning/data/School_Learning_Modatilities_Cleanversion.csv)
