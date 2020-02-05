#triangle de pascal

def pascal(N):     
    #attention! N commence à 1            
    #je definie la 1ere et la 2eme ligne
    liste=[[1],[1,1]]         
    # print(liste[0])
    # print(liste[1])
    if N==1:
        return([1])
    if N==2:
        return([1,1])
    if N==3:
        return([1,2,1])
    #je m'occupe des nouvelles lignes
    for i in range(2,N): 
        #chaque ligne commence par un 1    
        liste.append([1])      
        #je m'occupe des nouveaux termes, en sachant qu'il y a un 1 en debut de ligne
        for j in range(1,i):  
            #calcul du j^ieme terme  
            liste[i].append(liste[i-1][j-1] + liste[i-1][j])  
        #chaque ligne finie par un 1  
        liste[i].append(1)     
    return(liste[i])

for i in range(1,9):
    print(pascal(i)) 
   