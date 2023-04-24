import numpy as np

def my_fft(x):
    #Compute the DFT of a given input signal x using the Cooley-Tukey FFT algorithm#
    n = len(x)
    if n == 1:
        return x
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[:n // 2] * odd,
                           even + factor[n // 2:] * odd])

def my_ifft(X):
    #then we compute the inverse DFT of a given input signal X#
    n = len(X)
    X_conj = X.conj()
    Y = my_fft(X_conj) / n
    return Y.conj()

# to define out input signal of X
X = np.array([21, 22, 23, 24])

# Compute inverse DFT of X using our own implementation
x = my_ifft(X)

# Print results
print("Input signal X: ", X)
print("Inverse DFT of X: ", x)
