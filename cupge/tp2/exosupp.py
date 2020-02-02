#triangle de pascal

def pascal(N):                  #N:numero de la ligne avec premiere ligne à 1
    liste=[[1],[1,1]]         #je definie la 1ere et la 2eme ligne
    print(liste[0])
    print(liste[1])
    for i in range(2,N):        #je m'occupe des nouvelles lignes
        liste.append([1])       #chaque ligne commence par un 1
        for j in range(1,i):    #je m'occupe des nouveaux termes, en sachant qu'il y a un 1 en debut de ligne
            liste[i].append(liste[i-1][j-1] + liste[i-1][j])    #calcul du j^ieme terme
        liste[i].append(1)      #chaque ligne finie par un 1
        print(liste[i])
    return(liste[i])

print(pascal(3))    #fonctionne pour N>2