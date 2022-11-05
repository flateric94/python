def syracuse1(u):
    n=0
    while u!=1:
        if u%2==0:
            u=u/2
        else:
            u=3*u+1
        n=n+1
    return(n)

print(syracuse1(2))
print(syracuse1(9))

def syracuse2(u,b):
    n=0
    while u!=b and u!=1:
        if u%2==0:
            u=u/2
        else:
            u=3*u+1
        n=n+1
    if u==b:
        return(n)
    elif b==4:
        return(n+1)
    elif b==2:
        return(n+2)
    else:
        return("Erreur")

print(syracuse2(3,3))
print(syracuse2(5,2))
print(syracuse2(6,1))
print(syracuse2(84,54))
