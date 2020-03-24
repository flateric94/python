# a) Questions préliminaires

from collections import deque

# définition d'une classe Graphe

class Graphe:
    def __init__(self, n):
        self.n = n

        m = [False]*n
        for i in range(n):
            m[i] = [False]*n
        self.m = m

    def ajouterArrete(self, i, j):
        self.m[i][j] = True
        self.m[j][i] = True

    def trouverVoisins(self, k):
        voisins = []
        for i in range(self.n):
            if self.m[k][i] == True:
                voisins.append(i)
        return(voisins)

    # b) parcours en largeur

    def parcoursLargeur(self, source):
        visites = []
        file = deque()
        file.append(source)
        while len(file) != 0:
            sommetCourant = file.popleft()
            visites.append(sommetCourant)
            print(sommetCourant)
            voisins = self.trouverVoisins(sommetCourant)
            for v in voisins:
                if visites.count(v) == 0:
                    file.append(v)

    # c) Parcours en profondeur

    def parcoursProfondeur(self, source, visites):
        visites.append(source)
        print(source)
        voisins = self.trouverVoisins(source)
        for v in voisins:
            if visites.count(v) == 0:
                self.parcoursProfondeur(v , visites)

# on implémente le graphe de la fig. 2
monGraphe = Graphe(8)

monGraphe.ajouterArrete(0,1)
monGraphe.ajouterArrete(0,4)
monGraphe.ajouterArrete(1,5)
monGraphe.ajouterArrete(5,2)
monGraphe.ajouterArrete(5,6)
monGraphe.ajouterArrete(0,4)
monGraphe.ajouterArrete(2,3)
monGraphe.ajouterArrete(3,7)

# test trouverVoisin
print(monGraphe.trouverVoisins(3))

# test parcours largeur
print("###########")
monGraphe.parcoursLargeur(5)

# test parcours longueur
print("###########")
monGraphe.parcoursProfondeur(4, [])


# d) Recherche du plus court chemin : l'algorithme de Dijkstra
pos_inf = float('inf')
class GraphePondere:
    def __init__(self, n):
        self.n = n

        m = [False]*n
        for i in range(n):
            m[i] = [False]*n
        self.m = m
        
        poids = [1]*n
        for i in range(n):
            poids[i] = [1]*n
        self.poids = poids

    def ajouterArrete(self, i, j, poids):
        self.m[i][j] = True
        self.m[j][i] = True

        self.poids[i][j] = poids
        self.poids[j][i] = poids

    def trouverVoisins(self, k):
        voisins = []
        for i in range(self.n):
            if self.m[k][i] == True:
                voisins.append(i)
        return(voisins)

    def dijkstra(self, source ,destination):
        visites = []
        distance = [pos_inf]*self.n
        distance[source] = 0
        while visites.count(destination) == 0:

            for i in range(self.n):
                if visites.count(i) == 0:
                    sommetCourant = i
                    break
            for k in range(self.n):
                if visites.count(k) == 0 and distance[k] < distance[sommetCourant]:
                    sommetCourant = k
            # sommetCourant est le sommet non visité avec la plus petite distance
            # print(sommetCourant)
            visites.append(sommetCourant)

            # calcule la distance entre les voisins et l'origine
            voisins = self.trouverVoisins(sommetCourant)
            for v in voisins:
                nouvelleDistance = distance[sommetCourant] + self.poids[sommetCourant][v]
                if nouvelleDistance < distance[v]:
                    distance[v] = nouvelleDistance
        
        return distance[destination]

# on implémente le graphe de la fig. 3
monGraphe = GraphePondere(6)

monGraphe.ajouterArrete(0,1,2)
monGraphe.ajouterArrete(0,3,1)
monGraphe.ajouterArrete(1,3,1)
monGraphe.ajouterArrete(1,4,1)
monGraphe.ajouterArrete(1,2,4)
monGraphe.ajouterArrete(3,4,1)
monGraphe.ajouterArrete(4,2,1)
monGraphe.ajouterArrete(4,5,1)
monGraphe.ajouterArrete(2,5,3)


# test dijkstra : 
print("##########")
print(monGraphe.dijkstra(0,2))
                    


