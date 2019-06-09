#exercice1

def  f(x,y):
    if x==y:
        z=1
    else:
        z=0
    return(z)
print("resultats exo1")
print(f(1,2))
print(f(1,1))

print(f(True,False))
#que x ou y soient des booleens ne change pas la fonctionnalité du programme.

#exercice2

a=1
b=2
a=b
b=a
print("resultats exo2")
print(a,b) #ça ne fonctionne pas car on obtient a=2 mais b=2 (on efface 1).

a=1
b=2

c=a
a=b
b=c
print(a,b) #on a reussi à echanger les valeurs.

#exercice3

print("resultat exo3")
def f1(a,b):
    if a>0:
        x=a
        y=b
    else :
        x=a
    y=0
    return(x,y)
print(f1(5,3))
#ligne 40 mal indentée ce qui fait que la suite ne peut marcher, on a toujours y=0.

def f2(a,b):
    if a>0:
        x=a
        y=b
    else:
        x=a
        y=0
    return(x,y)
print(f2(5,3))
#version qui fonctionne (bonne indentation)
    
#exercice4

print("resultats exo4")
def nb_racines(a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        z=2
    elif delta==0:
        z=1
    elif delta<0:
        z=0
    return(z)
print(nb_racines(1,0,-1))
print(nb_racines(1,-2,1))
print(nb_racines(1,1,1))

def nb_racines_general(a,b,c):
    if a==0:
        if b==0 and c!=0:
            z=0
        elif b==0 and c==0:
            z=-1
        else:
            z=1
    else:
        z=nb_racines(a,b,c)
    return(z)
print(nb_racines_general(0,1,1))
print(nb_racines_general(0,0,1))
print(nb_racines_general(0,0,0))

    

