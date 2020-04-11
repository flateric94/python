import numpy as np
import matplotlib.pyplot as plt


def trapezes(x,y,n):
    Xi = np.array([])
    Yi = np.array([])
    for i in range(n-1):    #nombre intervalles : n-1
        x_trapeze = [x[i] , x[i] , x[i+1] , x[i+1] , x[i]]
        y_trapeze = [0 , y[i] , y[i+1] , 0 , 0]
        # Xi = np.append(Xi,x_trapeze)
        # Yi = np.append(Yi,y_trapeze)
        plt.plot(x,y,"bo-")
        plt.plot(x_trapeze,y_trapeze,"r")
    plt.show()
    return [Xi,Yi]

# solution trop "graphique", utile pour visualiser mais pour calculer trop complexe 



