def trouver_nombre_premier(n):
    test = "nombre premier"
    if n<2:
        return("erreur : le nombre doit être supérieur à 2")
    for i in range(2,n):
        if n%i == 0:
            test = "pas nombre premier"
    return(test)

def nombres_premiers(n):
    L=[]
    for i in range(n):
        if trouver_nombre_premier(i)=="nombre premier":
            L.append(i)
    return(L)

# for i in range(2,43):
#     print(nombres_premiers(i))

#avec crible d'erastothène:

def erastothène(n):
    L = [0,0] + [i for i in range(2,n+1)]
    for i in range(n+1):
        if L[i] != 0:
            for j in range(i*2,n+1,i):
                L[j] = 0
    return([k for k in L if k != 0])


print(erastothène(100))