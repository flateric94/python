#question1) fonction qui calcule pour une liste l la somme des éléments entre les 2 indices i et j

def sommepartielle(l,i,j):
    valeur=0
    for k in range(i,j+1):  #par exemple: for i in range(1,4)->[1,2,3], le 4 est en fait le n-1 terme
        # print(k,valeur)
        valeur=valeur+l[k]
    return(valeur)

#version plus simple:
def sommepartiellebis(l,i,j):
    return(sum(l[i:j]))
# print("#### sommepartielle ####")
# print(sommepartielle([1,2,3,4,5,6,3],0,6))      #doit retourner 1+2+3+4+5+6+3=24
# print(sommepartielle([0,0,1,1,1,1,0,0],2,5))    #doit retourner 1+1+1+1=4
# print("#### fin sommepartielle ####")
# print("#### sommepartiellebis ####")
# print(sommepartiellebis([1,2,3,4,5,6,3],0,6))   #doit retourner 1+2+3+4+5+6+3=24
# print(sommepartiellebis([0,0,1,1,1,1,0,0],2,5)) #doit retourner 1+1+1+1=4
# print("#### fin sommepartiellebis ####")

#question2) fonction permettant de repérer la plus "grande" sous liste en passant en revue toutes les sommes partielles
#complexité: O(n^3)
#consiste à calculer les sommes de toutes les sous-séquences et de garder les i,j qui ont permis d’obtenir la meilleure sous-séquence

def plus_grande_sous_liste(l):
    n=len(l)
    meilleur=min(l)
    i_meilleur,j_meilleur = -1,-1
    for i in range(n):
        for j in range(i+1,n+1):
            # print(i,j)
            s=sommepartielle(l,i,j-1)
            print(meilleur,s)
            if s>meilleur:
                meilleur=s
                i_meilleur,j_meilleur = i,j
    return(l[i_meilleur:j_meilleur])

print("#### plus grande sous liste ####")
# print(plus_grande_sous_liste([4,-6,7,-1,8,-50,3]))
print("#### fin plus grande sous liste ####")

#question3) améliorer la complexité en O(n^2)
#on évite la répétition de certains calculs lors du calcul de la somme des sous-séquences

def plus_grande_sous_liste_bis(l):
    meilleur=0
    n=len(l)
    i_meilleur,j_meilleur = -1,-1
    for i in range(n):
        somme=0
        for j in range(i,n):
            somme = somme + l[j]
            if somme>meilleur:
                meilleur=somme
                i_meilleur,j_meilleur = i,j+1
    return(l[i_meilleur:j_meilleur])

print("#### plus grande sous liste bis ####")
print(plus_grande_sous_liste_bis([4,-6,7,-1,8,-50,3]))
print("#### fin plus grande sous liste bis ####")

  