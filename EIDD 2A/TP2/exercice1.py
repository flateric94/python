################## TP2 : NEEDLEMAN-WUNSCH le 24/09/2021 ##################

# Question 1)


# Question 2)

'''
On va utiliser une classe d'objet Cell qui va contenir :
- la valeur de la cellule
- sa postion (x,y)
'''

class Cell:
    def __init__(self, score = None, prev_pos = None):
        # score de la cellule
        self.score = score
        # position (x,y) de la cellule d'avant
        # condittion d'initialisation
        if self.prev_pos == None:
            self.prev_pos = []
        else:
            self.prev_pos = prev_pos

    def __repr__(self):
        return "Val = {}\nDir = {}\n".format(self.score,self.prev_pos)



def simple_display(seq_top, seq_left, score):
    """ Do a simple display """
    print("Seq_top:  {}\nSeq_left: {}\nScore: {}".format(seq_top[::-1], seq_left[::-1], score))

def nice_display(seq_top, seq_left, score):
    """ Do a nice display """
    # What will be printed
    to_print = ""

    # Print seq_top
    # For each positions in a sequence
    for i, _ in enumerate(seq_top):
        # Add the corresponding letter (reverse order)
        to_print += seq_top[-(i+1)]
    # Print a next line after printing the seq_top
    to_print += "\n"

    # Print middle line
    # For each positions in a sequence
    for i, _ in enumerate(seq_top):
        # If it is a match between the two sequences
        if seq_top[-(i+1)] == seq_left[-(i+1)]:
            # Print a pipe
            to_print += "|"
        # Otherwise
        else:
            # Print a space
            to_print += " "
    # Print a next line after printing the middle line
    to_print += "\n"

    # Print seq_left
    # For each positions in a sequence
    for i, _ in enumerate(seq_top):
        # Add the corresponding letter (reverse order)
        to_print += seq_left[-(i+1)]

    # Add the score at the end
    to_print += "\nScore: {}\n".format(score)
    # Print everything!
    print(to_print)

# Question 3)

class DynamicMatrix:
    def __init__(self, seq_top, seq_left, match, mismatch, indel):
        # initialisation des variables 
        self.seq_top = seq_top
        self.seq_left = seq_left
        self.match = match
        self.mismatch = mismatch
        self.indel = indel
        # pour la Matrice : on va utiliser les listes
        self.matrix = []
        # parcourt des lignes en partant de la gauche (donc seq.left)
        for i in range(len(self.seq_left) + 1):
            self.matrix.append([])
            # parcourt des colonnes 
            for j in range(len(self.seq_top) + 1):
                # on ajoute la cellule dans la dernière ligne créée
                self.matrix[-1].append(Cell())

    
    def __repr__(self):
        # What will be returned
        return "Scores:\n{}\nPrev_pos:\n{}\n\n".format(self.print_scores(), self.print_prev_pos())

    # self representation for print
    def print_scores(self):
        """ Output the values of the matrix """
        # What will be returned
        ret_scores = ".  . "
        # Print top_seq
        for i in self.seq_top:
            ret_scores += "  {} ".format(i)
        # New line
        ret_scores += "\n"
        # For each line
        for ind, i in enumerate(self.matrix):
            # Print seq_left
            if ind > 0:
                ret_scores += "{} ".format(self.seq_left[ind-1])
            else:
                ret_scores += ". "
            # For each column
            for j in i:
                # If this cell has no value
                if j.score is None:
                    # Add a dot to the return
                    ret_scores += (" . ")
                # If this cell is not empty
                else:
                    # Add its content to the return
                    tmp_val = str(j.score)
                    if len(tmp_val) == 1:
                        ret_scores += " " + tmp_val + " "
                    if len(tmp_val) == 2:
                        ret_scores += tmp_val + " "
                    if len(tmp_val) == 3:
                        ret_scores += tmp_val
                # Always add a space after the value we add
                ret_scores += " "
            # End of this line, go to next line
            ret_scores += "\n"
        # Return the content of the Matrix
        return ret_scores


    # self representation for print
    def print_prev_pos(self):
        """ Output the values of the matrix """
        # What will be returned
        ret_prev_pos = ".   .  "
        # Print top_seq
        for i in self.seq_top:
            ret_prev_pos += "     {} ".format(i)
        # New line
        ret_prev_pos += "\n"
        # For each line
        for ind, i in enumerate(self.matrix):
            # Print seq_left
            if ind > 0:
                ret_prev_pos += "{} ".format(self.seq_left[ind-1])
            else:
                ret_prev_pos += ".   "
            # For each column
            for j in i:
                # If this cell has no value
                if j.prev_pos is None:
                    # Add a dot to the return
                    ret_prev_pos += (".   ")
                # If this cell is not empty
                else:
                    # Add its content to the return
                    tmp_val = str(j.prev_pos)
                    ret_prev_pos += tmp_val
                # Always add a space after the value we add
                ret_prev_pos += " "
            # End of this line, go to next line
            ret_prev_pos += "\n"
        # Return the content of the Matrix
        return ret_prev_pos

# Question 4)

    def compare(self, ntd_a, ntd_b):
        '''consigne : 
        creation d'une fonction comparant les nucleo
        retourne : la valeur de match si c'est identique
                    mismatch sinon 
        '''
        if ntd_a == ntd_b : 
            # return 2
            return self.match
        # return -1
        return self.mismatch

# Question 5)        

    def init(self):
        """ Initialize the matrix, i.e. fill the first line and column """
        # First cell is 0
        self.matrix[0][0].score = 0
        # On initialise la premiere ligne
        for i in range(1, len(self.seq_top) + 1):
            # indel = -2
            # on initialise la valeur (score) à la position i ...
            self.matrix[0][i].score = self.indel*i
            # ... puis, on initialise les coordonnées de la position précédente i-1
            self.matrix[0][i].prev_pos = [0 , i-1]
        # On initialise la première colonne 
        for i in range(1, len(self.seq_left) + 1):
            # idem
            self.matrix[i][0].score = self.indel*i
            self.matrix[i][0].prev_pos = [i-1 , 0]

# Question 6)

    def fill_matrix(self):
        """ Fill-up the matrix """
        ''' METHODE :
            - on va parcourir toutes les cellules de la matrice (double boucle)
            - puis, à une cellule donnée, on va initialiser les 3 valeurs des cases possibles
              (en haut, à gauche, dans la diagonale)
            - enfin, on met dans une variable le plus !grand! des scores (ça part dans les négatifs !)
            - on met à jour la matrice avec les nouvelles valeurs

        '''
        # On parcourt les cellules
        for i in range(1, len(self.seq_left) + 1):
            for j in range(1, len(self.seq_top) + 1):
        # On va initialiser les 3 cases : top_score, diago_score, left_score
                '''
                                        [diago_score][top_score (attention au indel)](j)
                    [left_score (attention au indel)][la case à qui on veut attribuer un score]
                    (i)
                '''
                top_score = self.matrix[i-1][j].score + self.indel
                top_prev_pos = [i-1 , j]

                left_score = self.matrix[i][j-1].score + self.indel
                left_prev_pos = [i , j-1]
                
                # pour la diagonale : verifier si il y a des nucleo egales
                diago_score = self.matrix[i-1][j-1].score + self.compare(self.seq_left[i-1], self.seq_top[j-1])
                diago_prev_pos = [i-1 , j-1]

                score_retenu = max(top_score, left_score, diago_score)

                self.matrix[i][j].score = score_retenu
                # VERSION SANS RECURSIVITE
                # On va mettre à jour la position précédente

                # if left_score == score_retenu:
                #     self.matrix[i][j].prev_pos = left_prev_pos
                # elif top_score == score_retenu:
                #     self.matrix[i][j].prev_pos = top_prev_pos
                # elif diago_score == score_retenu:
                #     self.matrix[i][j].prev_pos = diago_prev_pos
                if left_score == score_retenu:
                    self.matrix[i][j].prev_pos.append(left_prev_pos)
                if top_score == score_retenu:
                    self.matrix[i][j].prev_pos.append(top_prev_pos)
                if diago_score == score_retenu:
                    self.matrix[i][j].prev_pos.append(diago_prev_pos)


# Question 7)

    def global_alignment(self):
        """ Make a global alignment of two sequences """
        ''' METHODE :
            - on crée nos 2 séquences alignés renversées VIDES
            - On part de la fin de la matrice et on récupère le score
            - Puis, on récupère à chaque fois la position précédente jusqu'à
              revenir au premier terme de la matrice
        '''
        ali_seq_top = ""
        ali_seq_left = ""
        current_position = [len(self.seq_left), len(self.seq_top)]
        score = self.matrix[current_position[0]][current_position[1]]
        # On commence la recherche dans la matrice
        # distinction de cas :
        #   - si la position x précédente est la même que la current x position :
        #       -> insertion, donc gap
        #     sinon, on écrit le caractère précédent dans la seq_left
        #   - idem pour seq_top
        # et current position devient previous position
        prev_pos = []
        while prev_pos != [0,0] :
            prev_pos = self.matrix[current_position[0]][current_position[1]].prev_pos
            if (current_position[0] == prev_pos[0]) :
                ali_seq_left += "-"
            else : 
                ali_seq_left += self.seq_left[prev_pos[0]]
            if (current_position[1] == prev_pos[1]) :
                ali_seq_top += "-"
            else :                
                ali_seq_top += self.seq_top[prev_pos[1]]
            current_position = prev_pos
        return ali_seq_top, ali_seq_left, score
            
# QUESTION BONUS : BACKTRACKING        

def main():
    """ The main of TP3"""
    mat = DynamicMatrix("ACGGCTAT", "ACTGTAG", 2, -1, -2)
    mat.init()
    mat.fill_matrix()
    print(mat)
    al_seq_top, al_seq_left, score = mat.global_alignment()
    nice_display(al_seq_top, al_seq_left, score)
# Launch the main
main()
# Exit without error
exit(0)
# Always put one extra return line
