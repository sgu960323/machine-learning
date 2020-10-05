# -*- coding: utf-8 -*-
"""Simple_Logistic_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CUmjnycsSs0Ev5CTdzotfcnVGg2ULSPI

Import Modules
"""

import numpy as np
import matplotlib.pyplot as plt

"""Setting Data"""

data=np.array([[2, 0], 
               [4, 0], 
               [6, 0], 
               [8, 0], 
               [10, 0], 
               [12, 0], 
               [14, 1], 
               [16, 1], 
               [18, 1],
               [20, 1]])
x=data[:, 0].reshape((10, 1))
y=data[:, 1].reshape((10, 1))
fig, ax=plt.subplots()
for i in range(data.shape[0]):
  ax.plot(x[i][0], y[i][0], marker='o', color='blue')

"""Setting Hyperparameter"""

learning_rate=0.01
epoch=20000
weight=np.random.rand(1, 1)
bias=np.random.rand(1)

"""Make sigmoid function"""

def sigmoid(x):
  return 1/(1+np.exp(-x))

"""Make Cost Function(Cross-Entropy cost function)"""

def error_function(W, b):
  y_pred=x.dot(W)+b
  y_pred=sigmoid(y_pred)
  return (-np.sum(y*np.log(y_pred)+(1-y)*np.log(1-y_pred)))

"""Derivative of Error(using numerical derivative)"""

def numerical_derivative(f, W, b):
  h=1e-4
  grad=np.zeros((1, 2))
  w_fx1=f(float(W)+h, b)
  w_fx2=f(float(W)-h, b)
  grad[0, 0]=(w_fx1-w_fx2)/(2*h)
  b_fx1=f(W, float(b)+h)
  b_fx2=f(W, float(b)-h)
  grad[0, 1]=(b_fx1-b_fx2)/(2*h)
  return grad

"""Predict"""

def predict(x):
  test=x*weight+bias
  test=sigmoid(test)
  print(test)
  if test>0.5:
    return 1
  else:
    return 0

"""Training"""

for i in range(epoch):
  grad=numerical_derivative(error_function, weight, bias)
  weight=weight-learning_rate*grad[0, 0]
  bias=bias-learning_rate*grad[0, 1]
  if i%500==0:
     print('Epoch=', i, ' error_value=', error_function(weight, bias), "W=", weight, "b=", bias)

print(predict(7))