from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
import os

file = open('clf//iris_clf_Logistic.pkl','rb')
model = pickle.load(file)
def get_result(v1,v2,v3,v4):
        data = [v1,v2,v3,v4]
        input_data = [np.array(data)]
        predict = model.predict(input_data)
        if predict == 0:
            result = 'Iris-virginica'
        elif predict == 1:
            result = 'Iris-versicolor'
        elif predict == 2:
            result = 'Iris-setosa'
        else :
            return 'no result'
        return result

def get_clf_info():
    info = model.get_params() 
    return info
    
