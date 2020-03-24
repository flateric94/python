#parenthèsage

def parenthèsage(L):
    pile = []                  #ma pile
    n=len(L)
    for i in range(n):
        if L[i] == "(":
            pile.append(i)     #lorsque je rencontre une parenthèse ouvrante, j’empile sa position
        elif L[i] == ")":
            if pile == []:
                return(" ) à l'indice "+ str(i) +" n'est pas ouverte ")
            else:
                pile.pop()
    if pile == []:
        return("parenthèsage Ok")
    else:
        return("( à l'indice "+ str(pile[-1]) +" n'est pas refermée")  #sommet : pile[-1]

# lorsque je rencontre une parenthèse fermante, la position de la parenthèse ouvrante correspondante
# est censée être au sommet de la pile, donc si la pile est vide je renvoie un message d’erreur, sinon je
# dépile

print(parenthèsage("(je met les deux parenthèses)"))
print(parenthèsage("(j'enlève la dernière parenthèse"))
print(parenthèsage("j'enlève la première parenthèse)"))
print(parenthèsage("a((b)c)d)"))
print(parenthèsage("(a((b)c)d)"))


        