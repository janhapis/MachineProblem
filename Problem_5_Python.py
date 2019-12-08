from math import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import *

n = np.arange(0,200)
x = eval(input("Enter x(n): "))

def y(n):
    if n == 0:
        return -1.5*x[n]+2*x[n+1]-0.5*x[n+2]
    elif n > 0 and n <= 198:
        return 0.5*x[n+1]-0.5*x[n-1]
    elif n == 199:
        return 1.5*x[n]-2*x[n-1]+0.5*x[n-2]

n = np.arange(0,200)      
Y = []

for i in np.arange(0,200):
    Y.append(y(i))
    
plt.plot(n,x, 'b-', label="x(n)")
plt.plot(n,Y, 'r-',label="y(n)")
plt.title('Graphs of x(n) & y(n)')
plt.xlabel('n')
plt.ylabel('x(n) & y(n)')
plt.legend(loc="upper right")
plt.grid()