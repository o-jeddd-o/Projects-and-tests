import matplotlib.pyplot as plt
import numpy as np

# Define the sin function
def my_sin(x):
    return np.sin(x)

# Define the 1st, 3rd, 5th, and 7th order Taylor series approximations
def taylor_sin_1(x):
    return x
def taylor_sin_3(x):
    return x - (x**3)/6
def taylor_sin_5(x):
    return x - (x**3)/6 + (x**5)/120
def taylor_sin_7(x):
    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Plot the sin function and the Taylor series approximations
plt.plot(x, my_sin(x), label='sin(x)')
plt.plot(x, taylor_sin_1(x), label='1st order Taylor')
plt.plot(x, taylor_sin_3(x), label='3rd order Taylor')
plt.plot(x, taylor_sin_5(x), label='5th order Taylor')
plt.plot(x, taylor_sin_7(x), label='7th order Taylor')
plt.legend()
plt.show()