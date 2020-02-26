#parenthèsage

def parenthèsage(L):
    p = []                  #ma pile
    n=len(L)
    for i in range(n):
        if L[i] == "(":
            p.append(i)     #lorsque je rencontre une parenthèse ouvrante, j’empile sa position
        elif L[i] == ")":
            if p == []:
                return(" ) à l'indice "+ str(i) +" n'est pas ouverte ")
            else:
                p.pop()
    if p == []:
        return("parenthèsage Ok")
    else:
        return("( à l'indice "+ str(p[-1]) +" n'est pas refermée")  #sommet : p[-1]

# lorsque je rencontre une parenthèse fermante, la position de la parenthèse ouvrante correspondante
# est censée être au sommet de la pile, donc si la pile est vide je renvoie un message d’erreur, sinon je
# dépile

print(parenthèsage("(je met les deux parenthèses)"))
print(parenthèsage("(j'enlève la dernière parenthèse"))
print(parenthèsage("j'enlève la première parenthèse)"))
print(parenthèsage("a((b)c)d)"))
print(parenthèsage("(a((b)c)d)"))


        