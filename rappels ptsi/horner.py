import numpy as np

def horner_rec(i,x,n):
    print("entrez coefficient " + str(i) + " : ")
    valeur=input("la valeur est : ")
    print(valeur)
    a=np.float64(valeur)
    if i==n:
        return(a)
    else:
        return(a + x * horner_rec(i+1,x,n))

print(horner_rec(0,10**155,2))