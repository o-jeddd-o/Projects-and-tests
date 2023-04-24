import numpy as np

# first we need to define the input signal
X = np.array([10, 20, 30, 40])

# then we need to write code to compute inverse DFT of X that we just got.
x = np.fft.ifft(X)

# to print our results
print("Input signal X: ", X)
print("Inverse DFT of X: ", x)
