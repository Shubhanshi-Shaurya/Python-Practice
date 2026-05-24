## PROJECT PROBLEM - WE ARE GIVEN A DATASET OF HOUSE PRICES WITH SOME FEATURES 
## OUR TASK IS TO CREATE A MODEL WHICH WILL PREDICT THE PRICE FOR ANY NEW HOUSE BY LOOKING AT THE FEATURES

## BREAKING THE PROBLEM - SUPERVISED LEARNING(AS FEATURES AND LEVEL ARE GIVEN) -> REGRESSION TASK -> BATCH LEARNING
## SELECTING A PERFORMANCE MEASURE - ROOT MEAN SQUARE ERROR(RMSE) (PREFFERED)
## CHECK FOR ASSUMPTIONS 

import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor


housing=pd.read_csv("aiml/data.csv")
# print(housing.head())
# housing.info()
# print(housing['CHAS'].value_counts())
# print(housing.describe())
# housing.hist(bins=50,figsize=(20,15))
# plt.show()

##TRAIN - TEST SPLITTING 
# def split_train_test(data,test_ratio):
#     np.random.seed(42)
#     shuffled=np.random.permutation(len(data))
#     test_set_size=int(len(data)*test_ratio)
#     test_indices=shuffled[:test_set_size]
#     train_indices=shuffled[test_set_size:]
#     return data.iloc[train_indices],data.iloc[test_indices]

# train_set,test_set=split_train_test(housing,0.2)
# print(len(train_set))
# print(len(test_set))

#train_set,test_set=train_test_split(housing,test_size=0.2,random_state=42)
split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(housing,housing['CHAS']):
    strat_train_set=housing.loc[train_index]
    strat_test_set=housing.loc[test_index]

housing=strat_train_set.copy()

## LOOKING FOR CORRELATIONS
# corr_matrix=housing.corr()
# corr_matrix['MEDV'].sort_values(ascending=False)
# attributes=["MEDV","RM","ZN","LSTAT"]
# scatter_matrix(housing[attributes],figsize=(12,8))
# plt.show()

##TRYING OUT ATTRIBUTE COMBINATIONS
# housing['TAXRM']=housing['TAX']/housing['RM']
# corr_matrix=housing.corr()
# corr_matrix['MEDV'].sort_values(ascending=False)

housing=strat_train_set.drop("MEDV",axis=1)
housing_labels=strat_train_set["MEDV"].copy()

##MISSING ATTRIBUTES
# housing.dropna(subset=['RM'])  #option 1
# housing.drop("RM",axis=1)      #option 2
#option 3 
# median=housing['RM'].median()
# housing['RM'].fillna(median)   
# housing.describe()   #before we started filling missing attributes

imputer=SimpleImputer(strategy="median")
imputer.fit(housing)
x=imputer.transform(housing)
housing_tr=pd.DataFrame(x,columns=housing.columns)

##SCIKIT - LEARN DESIGN
#PRIMARILY THREE TYPES OF OBJECTS - 
#ESTIMATORS - IT ESTIMATES SOME PARAMETER BASED ON A DATASET EG. IMPUTER.IT HAS A FIT METHOD AND TRANSFORM METHOD.FIT METHOD - FITS THE DATASET AND CALCULATES INTERNAL PARAMETERS.
#TRANSFORMERS - TRANSFORM METHOD TAKES INPUT AND RETURN OUTPUT BASED ON THE LEARNINGS FROM FIT().IT ALSO HAS A CONVENIENCE FUNCTION CALLED FIT_TRANSFORM() WHICH FITS AND THEN TRANSFORMS.
#PREDICTORS - LINEARREGRESSION MODEL IS AN EXAMPLE OF PREDICTOR.TWO COMMON FUNCTIONS - FIT() AND PREDICT().IT ALSO GIVES FUNCTION WHICH WILL EVALUATE THE PREDICTIONS.

##CREATING PIPELINE 
##FEATURE SCALING - TWO TYPES OF FEATURE SCALING METHODS - 1.MIN-MAX SCALING(NORMALIZATION) = (VALUE.MIN)/(MAX-MIN) , SKLEARN PROVIDES A CLASS CALLED MINMAXSCALER FOR THIS  2.STANDARDISATION = (VALUE-MEAN)/STANDARD DEVIATION , SKLEARN PROVIDES A CLASS CALLED STANDARD SCALER FOR THIS 
my_pipeline=Pipeline([
    ('imputer',SimpleImputer(strategy="median")),
    ('std_scaler',StandardScaler()),
])
housing_num_tr=my_pipeline.fit_transform(housing)

##SELECT AND TRAIN THE MODEL 
#LINEAR REGRESSION 
# model=LinearRegression()
# model.fit(housing_num_tr,housing_labels)
# some_data=housing.iloc[:5]
# some_labels=housing_labels.iloc[:5]
# prepared_data=my_pipeline.transform(some_data)
# print(model.predict(prepared_data))
# print(list(some_labels))
# housing_predictions=model.predict(housing_num_tr)
# lin_mse=mean_squared_error(housing_labels,housing_predictions)
# lin_rmse=np.sqrt(lin_mse)

# THIS MODEL GAVE BIG MARGIN ERRORS TO WE CHOOSE TO USE DECISION TREE REGRESSOR 

##DECISION TREE REGRESSOR 
model=DecisionTreeRegressor()
model.fit(housing_num_tr,housing_labels)
some_data=housing.iloc[:5]
some_labels=housing_labels.iloc[:5]
prepared_data=my_pipeline.transform(some_data)
print(model.predict(prepared_data))
print(list(some_labels))
housing_predictions=model.predict(housing_num_tr)
lin_mse=mean_squared_error(housing_labels,housing_predictions)
lin_rmse=np.sqrt(lin_mse)

#THIS IS CAUSING OVERFITTING 
#SO USING BETTER EVALUATION TECHNIQUE - CROSS VALIDATION 


#time stamp - 2:35:00






