#arbre binaires de recherche

class Arbre():
    def __init__(self, contenu, gauche, droit):
        if type(contenu) != int:
            return("erreur")
        else:
            self.contenu = contenu
            self.gauche = gauche
            self.droit = droit
    
    def afficherPrefixe(self):
        print(self.contenu)
        if self.gauche != None:
            self.gauche.afficherPrefixe()
        if self.droit != None:
            self.droit.afficherPrefixe()

    def afficherInfixe(self):
        if self.gauche != None:
            self.gauche.afficherInfixe()
        print(self.contenu)
        if self.droit != None:
            self.droit.afficherInfixe()

    def afficherPostfixe(self):
        if self.gauche != None:
            self.gauche.afficherPostfixe()
        if self.droite != None:
            self.droit.afficherPostfixe()
        print(self.contenu)

    def inserer(self, valeur):
        if valeur < self.contenu:
            if self.gauche == None:
                self.gauche = Arbre(valeur, None, None)
            else:
                self.gauche.inserer(valeur)
        else:
            if self.droit == None:
                self.droit = Arbre(valeur, None, None)
            else:
                self.droit.inserer(valeur)

    def rechercher(self, valeur):
        if self.contenu == valeur:
            return self
        elif valeur < self.contenu and self.gauche != None:
            return self.gauche.rechercher(valeur)
        elif valeur > self.contenu and self.droit != None:
            return self.droit.rechercher(valeur)
        return None

# création d'un arbre
feuille1 = Arbre(1, None, None)
feuille4 = Arbre(4, None, None)
feuille7 = Arbre(7, None, None)
feuille13 = Arbre(13, None, None)

sousarbre6 = Arbre(6, feuille4, feuille7)
sousarbre14 = Arbre(14, feuille13, None)
sousarbre3 = Arbre(3, feuille1, sousarbre6)
sousarbre10 = Arbre(10, None, sousarbre14)

monArbre = Arbre(8, sousarbre3, sousarbre10)

# affichage de l'arbre
print("#### test affichage de l'arbre ####")
monArbre.afficherPrefixe()

# insertion valeur
print("")
print("#### test insertion valeur ####")
monArbre.inserer(15)
monArbre.afficherPrefixe()