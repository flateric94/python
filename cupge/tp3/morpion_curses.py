# "apprehendez les classes, openclassroom" : 
#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232721-apprehendez-les-classes

import random as rd
import curses

compteJoueur = 0 # va servir a affecter un numero derriere chaque joueur pour les differencier
def incremente_joueur():
    global compteJoueur # explique qu'on se referre à la variable globale, sinon on ne peut la modifier depuis une methode
    compteJoueur += 1

class joueur():   #définition de notre classe joueur
    """Classe définissant les informations relatives aux joueurs par : 
    -   le type du joueur (ordinateur ou humain)
    -   le type de sigle utilisé (x ou o)

    --> va simplifier le problème pour l'attribution des joueurs, permettant de faire joueur 
    humain/humain, ordi/ordi
    """
    def __init__(self, typedejoueur, sigle): # Notre méthode constructeur 
        if typedejoueur not in ["humain" , "ordinateur"]:
            print("attribuer un nom correct (humain/ordinateur)")
            return
        else:
            incremente_joueur()
            self.typedejoueur = typedejoueur
            self.sigle = sigle
            self.nom = typedejoueur + str(compteJoueur)

    """ question1)
    créer une classe morpion() et sa fonction init qui définit l'état initial du plateau de jeu.
    On notera le plateau par une liste, emplie initialement de zéros 3*3. La classe doit prendre
    en argument le nom du joueur qui commence ("humain" ou "ordinateur").
    """

class morpion:   #défition de notre classe morpion
    """Classe définissant l'état initial du plateau de jeu par :
    -   le type de plateau, ici 3*3
    -   le nom de l'utilisateur"""

    def __init__(self, premier_joueur, deuxieme_joueur): # Notre méthode constructeur
        self.plateau=[[0,0,0],[0,0,0],[0,0,0]]
        self.joueurs = [joueur(premier_joueur, 1), joueur(deuxieme_joueur, -1)]

  
    def afficher_plateau(self):
        """ question2)
        écrire une fonction afficher_plateau() qui permet d'afficher le plateau ligne par ligne avec des 
        croix à la place des -1, des ronds à la place des 1, et rien à la place des 0.
        """
        for i in range(3):
            ligne = []
            for j in range(3):
                if self.plateau[i][j]==1:
                    ligne.append("o")
                elif self.plateau[i][j]==-1:
                    ligne.append("x")
                elif self.plateau[i][j]==0:
                    ligne.append(" ")
            print(ligne)

    def afficher_plateau_curses(self):
        Y = 5
        X = 5
        for i in range(3):
            ligne = []
            for j in range(3):
                if self.plateau[i][j]==1:
                    sw_affichage_morpion.addstr(Y,X,"O")
                    # ligne.append("o")
                elif self.plateau[i][j]==-1:
                    sw_affichage_morpion.addstr(Y,X,"X")
                    # ligne.append("x")
                elif self.plateau[i][j]==0:
                    sw_affichage_morpion.addstr(Y,X," ")
                    # ligne.append(" ")
                sw_affichage_morpion.addstr(Y,X+1,"|")
                print(X)
                X += 2
            X = 5
            sw_affichage_morpion.addstr(Y+1,X,"-+-+-|")
            Y += 2
        sw_affichage_morpion.refresh()
        

    def jouer_humain(self, sigle):
        """ question3)
        écrire une fonction jouer_humain() qui vous permet via input() de dire où vous voulez jouer
        en numéro de ligne et de colonne. Cette fonction doit gérer le fait que vous n'avez le droit de 
        jouer que dans une case vide.
        """
        # choix de la ligne et vérification de son existence
        print("choisissez la ligne : ")
        ligne=int(input())
        if ligne>2 or ligne<0:
            print("les lignes existantes sont entres 0 et 2")
            self.joueur_humain(sigle)
        # choix de la colonne et vérification de son existence
        print("choisissez la colonne : ")
        colonne=int(input())
        if colonne>2 or colonne<0:
            print("les colonnes existantes sont entres 0 et 2")
            self.joueur_humain(sigle)
        #vérification case vide
        if self.plateau[ligne][colonne] != 0:
            print("joue dans une case vide")
            self.joueur_humain(sigle)
        #la case se remplit
        else:
            self.plateau[ligne][colonne] = sigle
            self.afficher_plateau()
            self.afficher_plateau_curses()

    def jouer_humain_curses(self, sigle):
        """ question3)
        écrire une fonction jouer_humain() qui vous permet via input() de dire où vous voulez jouer
        en numéro de ligne et de colonne. Cette fonction doit gérer le fait que vous n'avez le droit de 
        jouer que dans une case vide.
        """
        # choix de la ligne et vérification de son existence
        print("choisissez la ligne : ")
        # sw_affichage_instruction.addstr(1,1,"choisissez la ligne : ")
        # entree = sw_affichage_instruction.getstr(2,1).decode(encoding="utf-8")
        # sw_affichage_instruction.refresh()
        # sw_affichage_instruction.addstr(2,1,entree)
        ligne=int(input())
        if ligne>2 or ligne<0:
            print("les lignes existantes sont entres 0 et 2")
            self.joueur_humain(sigle)
        # choix de la colonne et vérification de son existence
        print("choisissez la colonne : ")
        colonne=int(input())
        if colonne>2 or colonne<0:
            print("les colonnes existantes sont entres 0 et 2")
            self.joueur_humain(sigle)
        #vérification case vide
        if self.plateau[ligne][colonne] != 0:
            print("joue dans une case vide")
            self.joueur_humain(sigle)
        #la case se remplit
        else:
            self.plateau[ligne][colonne] = sigle
            self.afficher_plateau()
            self.afficher_plateau_curses()

    def trouver_cases_vides(self):
        """question4)
        écrire une fonction trouver_cases_vides() qui renvoie une liste des indices (lignes, colonnes)
        des cases vides.
        """
        liste_indice_cases_vides=[]
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j]==0:
                    liste_indice_cases_vides.append((i,j))
        return(liste_indice_cases_vides)
    
    def jouer_aleatoire(self, sigle):
        """question5)
        écrire une fonction jouer_aleatoire() qui joue aléatoirement dans une des cases vides.
        """
        L=self.trouver_cases_vides()
        (i,j)=rd.choice(L)
        self.plateau[i][j]=sigle
        self.afficher_plateau()
        self.afficher_plateau_curses()

    def jouer_un_coup(self, indiceJoueur):
        """
        va nous permettre de pouvoir faire jouer nos joueurs tour par tour (coup par coup)
        """
        print(self.joueurs[indiceJoueur].nom + " joue:")
        if self.joueurs[indiceJoueur].typedejoueur == "humain":
            # self.jouer_humain(self.joueurs[indiceJoueur].sigle)
            self.jouer_humain_curses(self.joueurs[indiceJoueur].sigle)
        else:
            self.jouer_aleatoire(self.joueurs[indiceJoueur].sigle)
    
    def partie_gagnee(self):
        """question6)
        ecrire une fonction partie_gagnee() qui renvoie le joueur gagnant : None, "humain", 
        ou "ordinateur", en fonction des règles du jeu du morpion.
        """
        resultat = 99
        if self.plateau[0][0]==1 and self.plateau[0][1]==1 and self.plateau[0][2]==1:
            resultat=0
        if self.plateau[1][0]==1 and self.plateau[1][1]==1 and self.plateau[1][2]==1:
            resultat=0
        if self.plateau[2][0]==1 and self.plateau[2][1]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][0]==1 and self.plateau[1][0]==1 and self.plateau[2][0]==1:
            resultat=0
        if self.plateau[0][1]==1 and self.plateau[1][1]==1 and self.plateau[2][1]==1:
            resultat=0
        if self.plateau[0][2]==1 and self.plateau[1][2]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][0]==1 and self.plateau[1][1]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][2]==1 and self.plateau[1][1]==1 and self.plateau[2][0]==1:
            resultat=0
        if self.plateau[0][0]==-1 and self.plateau[0][1]==-1 and self.plateau[0][2]==-1:
            resultat=1
        if self.plateau[1][0]==-1 and self.plateau[1][1]==-1 and self.plateau[1][2]==-1:
            resultat=1
        if self.plateau[2][0]==-1 and self.plateau[2][1]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][0]==-1 and self.plateau[1][0]==-1 and self.plateau[2][0]==-1:
            resultat=1
        if self.plateau[0][1]==-1 and self.plateau[1][1]==-1 and self.plateau[2][1]==-1:
            resultat=1
        if self.plateau[0][2]==-1 and self.plateau[1][2]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][0]==-1 and self.plateau[1][1]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][2]==-1 and self.plateau[1][1]==-1 and self.plateau[2][0]==-1:
            resultat=1
        if resultat in [0, 1]:
            return resultat
        else:
            return None

    def jouer(self):
        self.afficher_plateau()
        self.afficher_plateau_curses()
        while self.partie_gagnee() != 0 or self.partie_gagnee() != 1 or self.partie_gagnee() != None:
            for i in range(9):
                self.jouer_un_coup(i%2)
                if self.partie_gagnee() in [0, 1]:
                    print(self.joueurs[self.partie_gagnee()].nom + " remporte la partie.")
                    return
            print("Match nul, pas de gagnant")
            return

# demarre curses
stdscr = curses.initscr()

sw_affichage_morpion = stdscr.subwin(17,17,0,60)
sw_affichage_morpion.box()
sw_affichage_morpion.refresh()

sw_affichage_instruction = stdscr.subwin(20,60,0,0)
sw_affichage_instruction.box()
sw_affichage_instruction.refresh()
        
partie = morpion("ordinateur", "humain")
partie.jouer()
sw_affichage_morpion.getkey()

