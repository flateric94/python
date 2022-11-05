import numpy as np
import matplotlib.pyplot as plt
import time
 
def trapezes(x,y,n):
    xi, yi = np.array([]), np.array([])
    pas = (len(x)-1)/(n-1)
    curseur = 0
    for i in range(n) :
        xi = np.append(xi,x[round(curseur)])    # attention à mettre round (arrondir) : ça peut être un float donc moins précis
        yi = np.append(yi,y[round(curseur)])    # round(nombre) = arrondi à l'entier le plus proche   
        curseur = curseur + pas
    return [xi, yi]

# x = np.linspace(0,8,100) #3eme arg => len(x)
# y = x**2*np.sin(x)
# print(trapezes(x,y,9))
# xi = trapezes(x,y,9)[0]
# yi = trapezes(x,y,9)[1]
# plt.plot(x,y)
# plt.plot(xi,yi)
# plt.show()

def intTrap(x,y,n):
    xi = trapezes(x,y,n)[0]
    yi = trapezes(x,y,n)[1]
    aire = 0
    for i in range(n-1):    #nombre intervalles = n-1 
        aire += (xi[i+1]-xi[i])*(yi[i+1]+yi[i])/2
    return aire

# ~ 24 à constante près, on trouve 22.850768873217813 pour 1000 trapezes

x = np.linspace(-5,5,1000)
# y = x**2*np.sin(x)
y = np.exp(-x**2)

a = time.time()
print(intTrap(x,y,1000))
b = time.time()
print(np.trapz(y,x))
c = time.time()
print(b-a)
print(c-b)

# print(np.sqrt(np.pi)) # = 1.7724538509055159