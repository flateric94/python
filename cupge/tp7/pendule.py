import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.signal import argrelextrema

g = 9.81
l = 50*10**(-2)
omega0 = np.sqrt(g/l)
theta0 = np.pi/100

#######    PENDULE SIMPLE    #######

# question 1)

def solution(t,theta0,omega0):
    return theta0*np.cos(omega0*t)

# question 2)

# on veut résoudre theta" = a.theta 
# problème :  la fonction odeint ne sait résoudre que des équations d'ordre 1 mais peut en résoudre plusieurs d'un coup
# on se ramène alors à la résolution de Theta' = A*Theta
# on pose Theta = (theta , theta') , Theta' = (theta', a.theta)

a = - omega0**2
t = np.linspace(0,20,1000)

def equation_pendule(Theta,t):
    # On décompose notre Theta en (theta , dtheta) :
    (theta,dtheta) = Theta
    # On renvoit ce que vaut dTheta :
    return [dtheta,a*np.sin(theta)]

def equation_pendule_simplifie(Theta,t):
    (theta,dtheta) = Theta
    return [dtheta,a*theta]

# Pour que odeint renvoit séparément les valeurs de Theta et de dTheta, il faut rajouter .T à la fin :
Theta,dTheta=odeint(equation_pendule, (theta0,0), t).T
# print(Theta)
# print(dTheta)
# Theta_s,dTheta_s=odeint(equation_pendule_simplifie, (theta0,0), t).T
plt.figure()
plt.plot(t,Theta,'red')
plt.title("Theta en fonction de t sans approximation des petits angles")
plt.grid()
# plt.figure()
# plt.plot(t,Theta_s,'blue')
# plt.title("Theta en fonction de t avec approximation des petits angles")
# plt.grid()
plt.show()

# question 3)

# fonction qui renvoie l'intégrande de l'intégrale
W=2*np.pi/omega0
x=np.linspace(-theta0,theta0,1000)
def g(x,omega0,theta0):
    return 2 /( omega0*np.sqrt(2*(np.cos(x) - np.cos(theta0) ) ) )

y=g(x,omega0,theta0)
xmin = -theta0
xmax = theta0
res = quad(g, xmin, xmax,args=(omega0,theta0,))[0]
print(res)
print(W)

# question 5) 

#retrouver période du mouvement T grâce à la recherche d'extrema locaux

inds = argrelextrema(Theta, np.greater)
T = (t[inds[0][len(inds)]] - t[inds[0][0]])/len(inds)
print(T)


#######    PENDULE DOUBLE    #######

