# écriture postfixée 

def is_operation(char):
    if char == "+" or char == "-" or char == "*":
        return True
    else:
        return False

def exec_operation(a,b,op):
    if op == "+":
        return (a+b)
    elif op == "-":
        return (a-b)
    elif op == "*":
        return (a*b)
    else:
        print("uniquement + , - , * autorisés")
        return 

def postfixee(l):
    pile = []
    n = len(l)
    for i in range(n):
        if is_operation(l[i]) == True:
            x=pile.pop()    #je récupère le dernier élément de la liste avant l'opérateur, je le stocke
            y=pile.pop()    #puis on stocke celui encore avant.
            print(x,y)
            z=exec_operation(y,x,l[i])
            print(z)
            pile.append(z)
        else:
            pile.append(int(l[i]))  #il n'y a qu'un nombre (par ex: 3453)  
    resultat = pile.pop()
    return(resultat)

print(postfixee("456++3*"))
# print(postfixee("3572+*+489*++"))