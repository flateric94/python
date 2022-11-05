import numpy as np
import matplotlib.pyplot as plt
import math as mp

# question 1) :

def sommeliste(a,b):
    n = len(a)
    c = [0]*n
    for i in range(n):
        c[i] = a[i] + b[i]
    return c

# print(sommeliste([1,2,2,4],[4,2,2,3]))

# comparaison avec numpy
a = np.array([1,2,2,1])
b = np.array([4,2,2,3])
c = a + b
# print(c)

# question 2) & question 3) :

def generateX(a,n):
    L = []
    for i in range(n+1):
        L.append(i/n*a)
    return L

# print(generateX(10,10))

def calcCos(x):
    L = []
    n = len(x)
    for i in range(n):
        L.append(np.cos(x[i]))
    return L

x = generateX(10,100)
cosinus = calcCos(x)
plt.figure()
plt.plot(x,cosinus)
plt.show()

# en numpy 
x = np.linspace(0,100,1000)
cosinus = np.cos(x)
plt.figure()
plt.plot(x,cosinus)
plt.show()

# question 4) 

x = np.linspace(-10,10,1000)
a = -10
b = 10
c = 5
y = a*x**2 + b*x + c

plt.figure()
plt.plot(x,y)
plt.show()

# exemple de l'étude de l'influence de b : 
x = np.linspace(-10,10,1000)
a = 1
c = 5

b_valeurs = np.linspace(-10,10,5)

plt.figure()
for b in b_valeurs:
    y = a*x**2 + b*x + c
    plt.plot(x,y, label = 'b = '+str(b))
plt.legend()
plt.show()

# question 6) :

x_bin = x.reshape(10,100)
y_bin = y.reshape(10,100)
y_bin = y_bin.sum(axis=1)/100
x_bin = x_bin.sum(axis=1)/100

print(y_bin)
print(x_bin)

plt.figure()
plt.plot(x,y, label='continu')
plt.plot(x_bin , y_bin , '+' , label='échantillonage n=10')
plt.legend()
plt.show()

