import matplotlib.pyplot as plt
import math as ma

N=1000
Listex=[k*4*ma.pi/N for k in range(N+1)]
Listeycos=[ma.cos(x) for x in Listex]
Listeysin=[ma.sin(x) for x in Listex]

plt.plot(Listex,Listeycos,label='y=cos(x)')
plt.plot(Listex,Listeysin,label='y=sin(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Graphique_test")
plt.legend(loc=3)
plt.show()

plt.figure()

plt.subplot(2,1,1) #plt.subplot(n,p,k)
#la fenetre graphique est découpée en n*p figures (n:ligne,p:colonne) et le code concerne la kieme de ces figures
plt.plot(Listex,Listeycos,label='y=cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=3)

plt.subplot(2,1,2)    
plt.plot(Listex,Listeysin,label='y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=3)

plt.show()

#on a du ajouter une extension à python pour tracer les courbes (matplotlib) ainsi que la bibliothèque numpy
#cmd en tant qu'admin, install matplotlib, telechargement et le tour est joué.