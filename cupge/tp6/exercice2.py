import numpy as np
import matplotlib.pyplot as plt
import math as mp

# question 1) :

theta = np.linspace(0 , 4*np.pi , 1000)
theta0 = np.pi/3
p = 1
e = 0.9

r = p/(1+e *np.cos(theta-theta0))

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure()
plt.plot(x,y)
plt.show()

# question 2) :

# influence de e :
theta = np.linspace(0 , 4*np.pi , 1000)
theta0 = np.pi/3
p = 1
e_valeurs = np.linspace(0.1 , 0.9 , 10)


plt.figure()
for e in e_valeurs:
    r = p/(1+e *np.cos(theta-theta0))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x,y, label ='e = '+str(e))
# plt.legend()
plt.show()

# influence de theta0 : 

theta = np.linspace(0 , 4*np.pi , 1000)
e = 1
p = 1
theta0_valeurs = np.linspace(0 , 2*np.pi , 10)


plt.figure()
for theta0 in theta0_valeurs:
    r = p/(1+e *np.cos(theta-theta0))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    plt.plot(x,y, label ='theta0 = '+str(theta0))
plt.legend()
plt.show()

# question 3) :

theta = np.linspace(0 , 4*np.pi , 1000)
theta0 = np.pi/3
p = 1
e = 0.9

r = p/(1+e *np.cos(theta-theta0))

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.figure()
plt.plot(x,y)

a = 0.01
theta0modif = a*theta
rmodif = p/(1+e*np.cos(theta-theta0modif))
xmodif = rmodif*np.cos(theta)
ymodif = rmodif*np.sin(theta)

plt.plot(xmodif,ymodif)
plt.show()
