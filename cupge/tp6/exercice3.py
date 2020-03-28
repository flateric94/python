import numpy as np
import matplotlib.pyplot as plt
import math as mp

# question 1) :

def gauss(x):
    return np.exp(-x**2)

x = np.linspace(-5, 5, 1000)
y = gauss(x)
plt.figure()
plt.plot(x,y)
plt.show()

# question 2) :

N = 10000
coord = np.random.random((5,5))
print(coord)

# question 3) et 4) :

N = 1000000
coord = np.random.random((2,N))
coord[0,:] *= 10
coord[0,:] -= 5

# on crée un masque
mask = [False]*N
for i in range(N):
    if coord[1,i] < gauss(coord[0,i]):
        mask[i] = True
plt.figure()
monhistogramme = plt.hist(coord[0,mask], bins = 100)
plt.show()

print(np.sum(mask)/N*10)
print(np.sqrt(np.pi))
