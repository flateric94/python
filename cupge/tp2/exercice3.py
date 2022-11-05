#question1) renvoyer une liste de n éléments aléatoires tous compris entre 1 et n^2, n donné en paramètre
import random as rd
import matplotlib.pyplot as plt

def listealeatoire(n):
    L=[]
    for i in range(n):
        a=rd.randint(1,n**2)
        L.append(a)
    return(L)

# print("#### test listealetaoire ####")
# print(listealeatoire(4))
# print(listealeatoire(3))
# print(listealeatoire(9))
# print("#### fin test listealetaoire ####")

#question2) 2 à 2 différents

def sansdoublon(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n):
            if l[i]==l[j]:
                return False        
    return True

# print("#### test sansdoublon ####")
# print(sansdoublon([1,2,3,4,-1]))
# print(sansdoublon([1,2,3,1,8]))
# print("#### fin test sansdoublon ####")

def intuition1(n):
    L=listealeatoire(n)
    return(sansdoublon(L))

print(intuition1(23))

def intuition2(n):
    marqueur=0
    for i in range(100):
        L=listealeatoire(n)
        if sansdoublon(L) == True:
            continue
        else:
            marqueur=marqueur+1
    return(marqueur)

print(intuition2(37))   #sur 100 tests, combien de fois a-t-il trouvé un doublon??



    

