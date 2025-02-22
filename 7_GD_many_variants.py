from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.random.seed(2)

X = np.random.rand(1000,1)
y =4+3*X+ 0.2*np.random.randn(1000,1) #noise added

#Building Xbar
one = np.ones((X.shape[0],1)) #tạo ra ma trận với chỉ toàn số 1
Xbar = np.concatenate((one, X), axis=1) #gộp ma trận

A = np.dot(Xbar.T, Xbar) # Nhân ma trận Xbar.T với Xbar
b = np.dot(Xbar.T, y)
print(A)
print(np.linalg.pinv(A))
w_lr = np.dot(np.linalg.pinv(A), b) #Compute the (Moore-Penrose) pseudo-inverse (ma trận giả đảo) of a matrix
print('Solution found by formula: w = ', w_lr.T);

#Display result
w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 1, 2, endpoint=True) 
y0 = w_0 + w_1*x0

#Drawing the fitting line
plt.plot(X.T, y.T, 'b.') #data
plt.plot(x0, y0, 'y', linewidth = 2)
plt.axis([0, 1, 0, 10])
plt.show()

def grad(w):
    N = Xbar.shape[0]
    return 1/N *Xbar.T.dot(Xbar.dot(w)-y)

def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w), 2)**2






