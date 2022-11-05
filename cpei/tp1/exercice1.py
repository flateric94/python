def f(z):
    valeur1 = input("entrer la premiere valeur à multiplier: ")
    print(valeur1)
    a=float(valeur1)
    valeur2 = input("entrer la deuxieme valeur à multiplier: ")
    print(valeur2)
    b=float(valeur2)
    if z==a*b:
        return("Correct")
    else:
        return("Erreur")
    
print(f(4))




