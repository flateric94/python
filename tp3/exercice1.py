def milieu(x1,y1,x2,y2):
    xm=(x1+x2)/2
    ym=(y1+y2)/2
    print("les coordonnées du milieu sont " + str(xm) + " et " + str(ym))
    return

print(milieu(1,1,2,2))
print(milieu(3,87,2,9))

def droite(x1,y1,x2,y2):
    a=y1-y2
    b=x2-x1
    c=y2*x1-y1*x2
    print("l'équation de la droite passant par ces points est "+str(a)+"x**2 +"+str(b)+"x +"+str(c))
    return

print(droite(3,76,8,232))

def test(x1,y1,x2,y2,x3,y3):
    a=y1-y2
    b=x2-x1
    c=y2*x1-y1*x2
    resultat=a*x3+b*y3+c
    if resultat==0:
        print("les 3 points sont alignés")
    else:
        print("les 3 ne sont pas alignés")
    return

print(test(1,1,2,2,3,3))
print(test(1,2,65,4,6,90))