import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.svm import SVR
import numpy as np
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import pickle
def predict(var):
       data=pd.read_csv('Capstone.csv')
       x=data.iloc[ : ,0:13]
       y=data.iloc[:,13:14]
       x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=10)
       svr=SVR(gamma='auto')
       par={'kernel':('linear','rbf','poly','sigmoid'),'degree':[1,2,3],'C':[1,2,3,4,6,7,8,9]}
       clfh=GridSearchCV(svr,par,cv=5)
       clfh.fit(x_train,y_train.values.ravel())
       pdh=clfh.predict(x_test)
       mean_squared_error(y_test,pdh)
       r2_score(y_test,pdh)
     #  p3=np.array([[3,1,2,0,1,1,0,1,1,0,1,1,2]])
       CGPA=clfh.predict(var)
       #print("\nYour CGPA WILL BE:\t",''.join(str(CGPA)))
       return CGPA

