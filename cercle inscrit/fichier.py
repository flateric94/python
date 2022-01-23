import numpy as np
import matplotlib.pyplot as plt

def circle(x1, y1, x2, y2, x3, y3):
    """ 
    retourne :
        - x0, y0 centre du cercle
        - r le rayon du cercle (au cas ou)
    """
    a = x1 - x2
    b = y1 - y2
    c = x1 - x3
    d = y1 - y3
    a1 = ((x1*x1 - x2*x2) + (y1*y1 - y2*y2)) / 2.0
    a2 = ((x1*x1 - x3*x3) + (y1*y1 - y3*y3)) / 2.0
    theta = b*c - a*d
    if abs(theta) < 1e-7:
        raise RuntimeError('Il devrait y avoir 3 x et y différents')
    x0 = (b*a2 - d*a1) / theta
    y0 = (c*a1 - a*a2) / theta
    r = np.sqrt(pow((x1-x0),2) + pow((y1-y0),2))
    return x0, y0, r

def affichage(x1, y1, x2, y2, x3, y3, x0, y0):
    plt.plot(x1,y1,x2,y2,x3,y3,x0,y0)

def main():
    x1 = 76
    y1 = -56
    x2 = 0
    y2 = 1
    x3 = 6
    y3 = 87
    x0, y0, r = circle(x1,y1,x2,y2,x3,y3)
    print("resultat :" + str(x0) + " " + str(y0))
    print(str(r))
    affichage(x1, y1, x2, y2, x3, y3, x0, y0)
main()
exit(0)

