# we need to import the numpy library first.
import numpy as np
import time

# we need to generate the signal of length 2048
signal = np.random.rand(2048)

# to compute the FFT and record the time needed to complete it
start_time = time.time()
fft = np.fft.fft(signal)
fft_time = time.time() - start_time

# to compute the OFT and record the time it takes for it to finish
start_time = time.time()
oft = np.zeros_like(fft)
N = signal.size
for x in range(N):
    for z in range(N):
        oft[x] += signal[z] * np.exp(-2j*np.pi*x*z/N)
oft_time = time.time() - start_time
# to compare the speeds between the OFT and FFT
print(f"FFT time: {fft_time:.6f} seconds")
print(f"OFT time: {oft_time:.6f} seconds")
