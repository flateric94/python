#parenthèsage

def parenthèsage(L):
    p = []
    n=len(L)
    for i in range(n):
        if L[i] == "(":
            p.append(i)
        elif L[i] == ")":
            if p == []:
                return(" ) à l'indice "+ str(i) +" n'est pas ouverte ")
            else:
                j= p.pop()
    if p == []:
        return("parenthèsage Ok")
    else:
        return("( à l'indice "+str(p[0])+" n'est pas refermée")


print(parenthèsage("(je met les deux parenthèses)"))
print(parenthèsage("(j'enlève la dernière parenthèse"))
print(parenthèsage("j'enlève la première parenthèse)"))
print(parenthèsage("a((b)c)d)"))
print(parenthèsage("(a((b)c)d)"))


        