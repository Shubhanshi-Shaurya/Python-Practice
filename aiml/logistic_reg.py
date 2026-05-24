import sklearn as sk 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris=datasets.load_iris()
# print(iris['DESCR'])

########
x=iris['data'][:,3:]
y=(iris['target']==2).astype(int)

#####train 
clf=LogisticRegression()
clf.fit(x,y)
example=clf.predict(([[2.6]]))
print(example)

######plotting 
x_new=np.linspace(0,3,1000).reshape(-1,1)
y_prob=clf.predict_proba(x_new)
plt.plot(x_new,y_prob[:,1],"g-")
plt.show()






