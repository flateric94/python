################## TP1 : REVERSE COMPLEMENT le 17/09/2021 ##################

import random
import time

# Question 1)

def reverse_complement_naive(seq):
    """consigne : 
       renverser la sequence 
       et retourner sa sequence renversée complémente
    """
    # on crée la séquence initialement vide
    result = ""
    # puis, on parcourt la séquence, et on itère sur chaque nucléotide
    # Si il n'y a pas de A T C G, on retourne une erreur
    for nucleo in seq :
        if nucleo != "A" and nucleo != "T" and nucleo != "C" and nucleo != "G":
            print("ERREUR : la séquence initiale est incorrecte")
            return
        else :
            if nucleo == "A":
                result = "T" + result
            if nucleo == "T":
                result = "A" + result
            if nucleo == "C":
                result = "G" + result
            if nucleo == "G":
                result = "C" + result
    # enfin, on retourne la séquence complémentaire inversée
    return result

def reverse_complement_naive2(seq):
    """consigne : 
       renverser la sequence 
       et retourner sa sequence renversée complémente
    """
    ### VERSION OPTIMISEE ###
    # on crée la séquence initialement vide
    result = ""
    # puis, on parcourt la séquence, et on itère sur chaque nucléotide
    # Si il n'y a pas de A T C G, on retourne une erreur
    for nucleo in seq[::-1] :
        if nucleo != "A" and nucleo != "T" and nucleo != "C" and nucleo != "G":
            print("ERREUR : la séquence initiale est incorrecte")
            return
        else :
            if nucleo == "A":
                result = "T" + result
            if nucleo == "T":
                result = "A" + result
            if nucleo == "C":
                result = "G" + result
            if nucleo == "G":
                result = "C" + result
    # enfin, on retourne la séquence complémentaire inversée
    return result


# Question 2)

def reverse_complement_less_naive(seq):
    """consigne : 
       renverser la sequence 
       et retourner sa sequence renversée complémente
    """  
    # on code la fonction de hashage :
    hash_funct = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    # puis on recommence le raisonnement (seq vide, on itère, on complète)
    result = ""
    for nucleo in seq :
        result = hash_funct[nucleo] + result
    return result

def reverse_complement_less_naive2(seq):
    """consigne : 
       renverser la sequence 
       et retourner sa sequence renversée complémente
    """  
    ### VERSION OPTIMISEE ###
    # on code la fonction de hashage :
    hash_funct = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    # puis on recommence le raisonnement (seq vide, on itère, on complète)
    result = ""
    for nucleo in seq[::-1] :
        result = hash_funct[nucleo] + result
    return result

# Question 3)

def generator_of_sequence(size):
    """consigne :
       on cree une sequence de nucleotide aléatoirement choisie entre
       A T C G, de taille size
    """
    # initialisation :
    result = ""
    # on va la remplir aléatoirement
    for i in range(size):
        list_nucleo = ["A", "T", "C", "G"]
        result += random.choice(list_nucleo)
    return result

# Question 4)

def main():
    # Test Question 1)
    seq = "AATCGT"
    result = reverse_complement_naive(seq)
    print(result)
    # Test Question 2)
    seq2 = "AATCGT"
    result2 = reverse_complement_less_naive(seq2)
    print(result2)
    # Test Question 3)
    size = 14
    print(generator_of_sequence(size))
    # Question 4)
    """consigne : on va tester la rapidité de 
       toutes nos fonctions
    """
    # on importe la bibli time
    # je cree une sequence assez longue :
    seq_test = generator_of_sequence(500000)
    print("#### Question 4) ####")
    start = time.time()
    func1 = reverse_complement_naive(seq_test)
    end = time.time()
    print("func1 (reverse_complement_naive) : {:.12f}s".format(end-start))
    start = time.time()
    func2 = reverse_complement_naive2(seq_test)
    end = time.time()
    print("func2 (reverse_complement_naive2) : {:.12f}s".format(end-start))
    start = time.time()
    func3 = reverse_complement_less_naive(seq_test)
    end = time.time()
    print("func3 (reverse_complement_less_naive) : {:.12f}s".format(end-start))
    start = time.time()
    func4 = reverse_complement_less_naive2(seq_test)
    end = time.time()
    print("func4 (reverse_complement_less_naive2) : {:.12f}s".format(end-start))
main()





