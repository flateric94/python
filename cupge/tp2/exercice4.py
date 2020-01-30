#bonus : si la liste n'est pas triée

def tri_liste(liste):
    r=[]
    while liste:
        mini=min(liste)
        for i in liste:
            if i < mini:
                mini=i
        liste.remove(mini)  #retire le 1er minimum trouvé
        r.append(mini)      #puis l'ajoute dans la liste r
    return(r)

print(tri_liste([-1,2,6,3,9,70,-23,6,24,23,0]))

#question1) recherche dichomotique

def recherche_dichotomique_2(e,l):
    l=tri_liste(l)
    print(l)
    a=0
    b=len(l)-1
    while a<b:
        med=int((a+b)/2)    #prendre la partie entière
        if e==l[med]:
            a=med
            b=med
        else:
            if e>l[med]:
                a=med+1
            else:
                b=med-1
    if e==l[a]:
        return(a)
    else:
        return False

print(recherche_dichotomique_2(4,[1,-2,4,5,-67,-45,234]))





