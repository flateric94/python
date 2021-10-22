#tours de Hanoi

def deplacer(tour_de_dep , tour_arriv , disque):
    #print("deplacer le disque " + str(disque) + " de la tour " + str(tour_de_dep) + " à la tour " + str(tour_arriv))
    print([int(disque), int(tour_de_dep), int(tour_arriv)])
# print(deplacer(2,3,5))

def hanoi(nombre_de_disque , tour_de_depart , tour_d_arrive):
    if nombre_de_disque < 1:
        print("le fun est présent")
    elif nombre_de_disque == 1:
        deplacer(tour_de_depart , tour_d_arrive , 1)
    else:
        autre_tour = 3 - tour_de_depart - tour_d_arrive
        # 1/ deplacer n-1 disques de la "tour de depart" à "autre tour"
        hanoi(nombre_de_disque - 1 , tour_de_depart , autre_tour)
        # 2/ deplacer 1 disque de la tour de "tour de depart" a "tour d'arrive"
        deplacer(tour_de_depart , tour_d_arrive , nombre_de_disque)
        # 3/ deplacer n-1 disques de la tour "autre tour" a "tour d'arrivee"
        hanoi(nombre_de_disque - 1 , autre_tour , tour_d_arrive)
    return 

print(hanoi(6,0,1))

