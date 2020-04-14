import numpy as np
import matplotlib.pyplot as plt

# question 1)

C = 10
x = np.linspace(0,20,100)
y = C*np.exp(-x)
plt.plot(x,y)
plt.show()

# question 2)

def f(y,t):
    return -y


# question 3)

def Euler(f,y0,t):
    y = [y0]
    n = len(t)
    for i in range(1,n):
        y.append(y[i-1] + f(y[i-1],t[i-1])*(t[i]-t[i-1]))
    return(y)

# question 4)

t1 = np.linspace(0,10,10)
t2 = np.linspace(0,20,1000)
y1 = Euler(f,10,t1)
y2 = Euler(f,10,t2)
plt.figure()
plt.plot(t2,y2,'g')
plt.grid()
plt.figure()
plt.plot(t1,y1,'r')
plt.grid()
plt.show()

# question 5) 

def Euler_mod(f,y0,t):
    resultat = []*len(y0)
    for p in y0:
        y=[p]
        n = len(t)
        for i in range(1,n):
            y.append(y[i-1] + f(y[i-1],t[i-1])*(t[i]-t[i-1]))
        resultat.append(y)    
    return(resultat)


t2 = np.linspace(0,10,100)
L = [0,10,20,30,2.89]
y2 = Euler_mod(f,L,t2)
for i in range(len(L)):
    plt.figure()
    plt.plot(t2,y2[i],'r')
    plt.grid()
    plt.show()

# question 7)

omega = 3
t = np.linspace(0,10,1000)
y = np.cos(omega*t)
plt.plot(t,y)
plt.show()

# question 8)

def oscillateur(Y,t) :
    dYdt = []
    for fi in Y : 
        dYdt.append((fi(t+ np.finfo(np.float32).eps) - fi(t) )/(np.finfo(np.float32).eps))
    return(dYdt)

y = np.cos
v = np.sin
Y = np.array((y,v))
print(oscillateur(Y,1))
print(oscillateur(Y,0))

# question 9)

omega = 3

def f(y,v,t):
    return((-omega**2)*y)

def Euler_2(f,y0,v0,t):
    y=[y0]
    v=[v0]
    for i in range(1,len(t)):
        v.append(v[i-1] + f(y[i-1],v[i-1],t[i-1])*(t[i]-t[i-1]))
        y.append(y[i-1] + v[i-1]*(t[i]-t[i-1]))
    return(y)

t = np.linspace(0,10,10000)
y = Euler_2(f,1,0,t)
plt.plot(t,y)
plt.show()