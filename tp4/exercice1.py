def impair_iter(n):
    i=0
    depart=1
    resultat=0
    if n==0:
        return(0)
    for i in range(n):
        resultat=resultat+(depart+2*i) 
    return(resultat)

print(impair_iter(3))