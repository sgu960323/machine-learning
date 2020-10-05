# -*- coding: utf-8 -*-
"""XOR_perceptron.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yxXzmNL72Bbpzpmsuov8DUvj1xNVx5Ir

import modules
"""

import numpy as np
import matplotlib.pyplot as plt

"""make sigmoid function as activation function"""

def sigmoid(x):
  return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
  return x*(1-x)

"""make data"""

#input
x=np.array([[0, 0],
           [0, 1],
           [1, 0],
           [1, 1]])
#output
y=np.array([[0], [1], [1], [0]])
fig, ax=plt.subplots()
for i in range(4):
  if y[i][0]==0:
    ax.plot(x[i][0], x[i][1], marker='o', color='blue')
  else:
    ax.plot(x[i][0], x[i][1], marker='o', color='red')

"""initialize hyper_parameter"""

learning_rate=0.1
epoch=15000

weight_hidden=np.random.uniform(size=(2, 2))
bias_hidden=np.random.uniform(size=(1, 2))

weight_out=np.random.uniform(size=(2, 1))
bias_out=np.random.uniform(size=(1, 1))

initial_h=sigmoid(x.dot(weight_hidden)+bias_hidden)
initial_y=sigmoid(initial_h.dot(weight_out)+bias_out)

"""Train"""

for i in range(epoch):
  hidden_input=sigmoid(x.dot(weight_hidden)+bias_hidden)
  y_pred=sigmoid(hidden_input.dot(weight_out)+bias_out)

  Error=((y-y_pred)**2)/2
  if i%500==0:
    print('Epoch', i, ':', Error.sum())
  
  gradient_y_pred=(y_pred-y)*(y_pred*(1-y_pred))
  gradient_out_weight=hidden_input.T.dot(gradient_y_pred)
  gradient_out_bias=np.sum(gradient_y_pred, axis=0, keepdims=True)
  gradient_hidden=gradient_y_pred.dot(weight_out.T)*(hidden_input*(1-hidden_input))
  gradient_hidden_weight=x.T.dot(gradient_hidden)
  gradient_hidden_bias=np.sum(gradient_hidden, axis=0, keepdims=True)

  weight_out=weight_out-learning_rate*gradient_out_weight
  bias_out=bias_out-learning_rate*gradient_out_bias
  weight_hidden=weight_hidden-learning_rate*gradient_hidden_weight
  bias_hidden=bias_hidden-learning_rate*gradient_hidden_bias

"""Result"""

print('Input')
print(x)
print('Label')
print(y)
print('Before deep learning')
print(initial_y)
print('After deep learning Output')
print(y_pred)