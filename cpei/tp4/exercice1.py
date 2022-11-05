def impair_iter(n):
    i=0
    depart=1
    resultat=0
    if n==0:
        return(0)
    for i in range(n):
        resultat=resultat+(depart+2*i) 
    return(resultat)

def impair_iter_detail(n):
    i=0
    depart=1
    resultat=0
    detail=""
    j=0
    if n==0:
        return(0)
    for i in range(n):
        resultat=resultat+(depart+2*i)
        detail = detail + str(depart+2*i)
        if i!=n-1:
            detail = detail + " + "
        else:
            detail = detail + " = "
    print(detail + str(resultat))
    return(resultat)

def impair_recu(n):
    if n==1:
        return(1)
    else:
        return(n+(n-1)+impair_recu(n-1))




print(impair_iter(8))
print(impair_iter_detail(8))
print(impair_recu(8))

