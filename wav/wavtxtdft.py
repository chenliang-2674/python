import numpy
from numpy import arange, sin, pi, cos
#import matplotlib.pyplot as plt
import cmath
#from scipy.fftpack import fft,ifft

Kl = arange(0, 100, 1)
Xk = []
f0 = 10
fs = 50
N = len(Kl)
y = sin(2*pi*f0*Kl/fs)    # x[n]
for k in Kl:  # 求 X[k] k = 1....N
    temp = 0
    for l in range(0, N):  # 求X[k]
        cm = 1j
        cm *= 2*pi*l*k/N
        temp += sin(2*pi*f0*l/fs)*cmath.exp(cm)
    temp = temp
    Xk.append(abs(temp))
