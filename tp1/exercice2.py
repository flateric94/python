def pomme1():
    x=0.60
    nombredepommes = input("combien de pommes souhaitez vous ?")
    print(nombredepommes)
    a=float(nombredepommes)
    prix=x*a
    b=float(prix)
    return(b)

print(pomme1())

def pomme2():
    x=0.60
    nombredepommes = input("combien de pommes souhaitez vous ?")
    print(nombredepommes)
    a=float(nombredepommes)
    if a<=5:
        prix=x*a
    else:
        prix = 3 + 0.50 *(a-5)
    b=float(prix)
    return(b)

print(pomme2())

def pomme3():
    p=0.60
    b=0.45
    nombredepommes = input("combien de pommes souhaitez vous ?")
    print(nombredepommes)
    a=float(nombredepommes)
    nombredebananes = input("combien de bananes souhaitez vous ?")
    print(nombredebananes)
    c=float(nombredebananes)
    prix=a*p+b*c
    d=float(prix)
    return(d)

print(pomme3())