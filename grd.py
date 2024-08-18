# Gradient Descent Implementation

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

# Define a Function
def fun(x):
    return (1/10)*x**2+2*np.sin(x)

# Define the derivative of the function
def dfun(x):
    return (1/5)*x+2*np.cos(x)

# Set X Range
x = np.arange(0,20,0.1)

# Plot the Function
plt.figure(figsize=(8,5))
plt.plot(x,fun(x))
plt.title('Gradient Descent Implementation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()



# Calculate local minimum or maximum
e = 1
e_targ = 1E-5
eta = 0.1
x_old = 17
while e >= e_targ:
    x_new = x_old - eta*dfun(x_old)
    plt.scatter(x_new,fun(x_new),color = 'red', alpha = 0.2)
    e = abs(x_new-x_old)
    x_old = x_new

plt.show()


