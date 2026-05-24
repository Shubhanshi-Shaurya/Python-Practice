import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error


#print(sk.__version__) 

#LINEAR REGRESSION 
####### data 1
diabetes=datasets.load_diabetes()

diabetes_x=diabetes.data

diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]

diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]

model=linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)

###testing the model
diabetes_y_predict= model.predict(diabetes_x_test)

print(mean_squared_error(diabetes_y_test,diabetes_y_predict))
print(model.coef_)
print(model.intercept_)


####### data 2
# diabetes_x=np.array([[1],[2],[3]])

# diabetes_x_train=diabetes_x
# diabetes_x_test=diabetes_x

# diabetes_y_train=np.array([[3],[2],[4]])
# diabetes_y_test=np.array([[3],[2],[4]])

# model=linear_model.LinearRegression()
# model.fit(diabetes_x_train,diabetes_y_train)

# ###testing the model
# diabetes_y_predict= model.predict(diabetes_x_test)

# print(mean_squared_error(diabetes_y_test,diabetes_y_predict))
# print(model.coef_)
# print(model.intercept_)

# plt.scatter(diabetes_x_test,diabetes_y_test)
# plt.plot(diabetes_x_test,diabetes_y_predict)
# plt.show()

# timestamp - video 12




