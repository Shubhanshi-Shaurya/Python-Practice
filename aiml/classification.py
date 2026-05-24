import sklearn as sk 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import datasets 
from sklearn.neighbors import KNeighborsClassifier

######## loading datasets 
iris=datasets.load_iris()
# print(iris.DESCR)           #printing description of the dataset 
features=iris.data
labels=iris.target 
print(features[0],labels[0])

#####training 
clf=KNeighborsClassifier()
clf.fit(features,labels)

preds=clf.predict([[31,1,1,1]])
print(preds)

#


