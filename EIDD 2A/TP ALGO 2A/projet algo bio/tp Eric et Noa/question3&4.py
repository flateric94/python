"""
TP de ERIC et NOA

Question 3) 
Créez un compteur de k-mers (k=30).
Question 4)
Utilisez ce compteur pour identifier les reads mal séquencés. Affichez les identifiants des sé-
quences "fausses" du jeu de données. On va fixer la limite à 2 occurrences : un k-mers apparaissant trois fois dans
le jeu de données est considéré comme valide, un k-mer n’apparaissant qu’une ou deux fois sera considéré comme
comportant une erreur de séquençage.

"""

""" 
fonction store :
Découpe la séquence et la stocke dans le dictionnaire
paramètres : dico le dictionnaire, seq la séquence à découper, ide l'identificateur de la séquence
"""
def store(dico, seq, ide):
    k = 30
    # découpe la séquence en morceaux de longueur k
    for i, _ in enumerate (seq[:len(seq)-k+1]):
        kmer = seq[i:i+k]
        # vérifie si ces k-mer sont présents dans le dictionnaire
        val = dico.pop(kmer, None)
        # il reprend la liste d'identificateurs précédentes et ajoute le nouveau
        if(val != None):
            val.append(ide)
            dico[kmer] = val
        # il ajoute le k-mer et son identificateur dans le dictionnaire
        else:
            dico[kmer] = [ide]

""" 
fonction read :
Lit le document et range les kmer dans un dictionnaire
key : kmer, value : liste des identificateurs des séquences où on retrouve ce kmer
le nombre d'apparitions de chaque kmer est la longueur de la liste 
"""
def read(genome_file):
    # on crée dictionnaire
    dico = {}
    # on lit fichier
    with open(genome_file) as file:
        for line in file:
            if(line[0] == ">"):
                # on recupere l'ide
                ide = line[1:len(line)-1:]
            else:
                store(dico, line.strip(), ide)
    return dico


""" 
Renvoie un set contenant tous les identificateurs des séquences
que l'on considère comme des erreurs de lecture 
"""
def false_ID(dico):
    result = set()
    for i in dico.values():
        if (len(i) == 1):
            result.add(i[0])
        elif (len(i) == 2):
            result.add(i[0])
            result.add(i[1])
    return result


def main(genome_file):
    dico = read(genome_file)
    list_false_ID = false_ID(dico)
    print(list_false_ID)

main("reads.fasta")
