import numpy as np
import matplotlib.pyplot as plt
import math as mp

# on va creer une super matrice
a = -10
b = 10
n = 1000

# question 1) :

def myMeshgrid(a,b,n):
    x = np.linspace(a,b,n)
    y = np.linspace(a,b,n)
    A = np.zeros((2,n,n))
    for i in range(n):
        A[0,i,:] = x
        A[1,:,i] = y
    return A

maillage = myMeshgrid(a,b,n)
# print(maillage)

# question 2) :

x = np.linspace(a,b,n)
y = np.linspace(a,b,n)
[X , Y] = np.meshgrid(x , y)
# exemple : tracer la fonction gaussienne en 2D:
gauss = np.exp(- X**2 - Y**2)
plt.imshow(gauss)
# plt.show()

# question 3) et 4) :

def Dist(X,Y,i,j):
    return np.sqrt((X-i)**2 + (Y-j)**2)

x = np.linspace(a,b,n)
y = np.linspace(b,a,n)
X,Y = np.meshgrid(x,y)
distance = Dist(X,Y,3,3)
plt.imshow(distance, extent=[a,b,a,b])
plt.colorbar()
# plt.show()

# question 5) :
# créer un masque pour les distances > r0 :

r0 = 10
masque = distance > r0
distance[masque] = 0
plt.imshow(distance, extent=[a,b,a,b])
# plt.show()

# question 6) :

def surfacedisque(r0 ,N, a, b):
    coord = np.random.random((2,N))
    coord[0,:] = coord[0,:]*(b-a)-(b-a)/2
    coord[1,:] = coord[1,:]*(b-a)-(b-a)/2
    mask= [False]*N
    for i in range(N):
        # est-ce que la distance du point i est inférieure à r0
        if Dist(coord[0,i],coord[1,i],0,0) <= r0:
            mask[i] = True
    plt.plot(coord[0,:],coord[1,:],".")
    plt.plot(coord[0,mask],coord[1,mask],".")
    plt.show()
    surface = np.sum(mask)/N*((b-a)**2)
    return surface
        
print(surfacedisque(1,10000,1,-1))
