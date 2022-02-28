"""
TP de ERIC et NOA

Question 2)
À partir de votre algorithme de Needleman-Wunsch, codez l’algorithme de Smith-Waterman et
utilisez la distance de Kimura suivante :
   A  C  G  T
A  1 -2 -1 -2
C -2  1 -2 -1
G -1 -2  1 -2
T -2 -1 -2  1

"""

def simple_display(seq_top, seq_left, score):
    """ Do a simple display """
    print("Seq_top:  {}\nSeq_left: {}\nScore: {}".format(seq_top[::-1], seq_left[::-1], score))

def nice_display(seq_top, seq_left, score):
    """ Do a nice display """
    # What will be printed
    to_print = "Local Aligment (Smith-Waterman) :\n"

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


KIMURA_DISTANCE = [[1, -2, -1, -2], 
                   [-2, 1, -2, -1],
                   [-1, -2, 1, -2],
                   [-2, -1, -2, 1]]

class Cell:
    def __init__(self, score = None, prev_pos = None):
        self.score = score
        self.prev_pos = prev_pos

    def __repr__(self):
        return "Value = {}\nPosition = {}\n".format(self.score, self.prev_pos)

class DynamicMatrix:
    """ Class to generate an empty matrix """
    def __init__(self, seq_top, seq_left, kimura, indel):
        # Init all "self" variables
        self.seq_top = seq_top
        self.seq_left = seq_left
        self.kimura = KIMURA_DISTANCE
        self.indel = indel
        # Create the matrix of Cell()
        self.matrix = []
        for i in range(len(self.seq_left) + 1):
            self.matrix.append([])
            for j in range(len(self.seq_top) + 1):
                self.matrix[-1].append(Cell())
    # self representation for print
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

    def numb(self, letter):
        if letter == "A":
            return 0
        elif letter == "C":
            return 1
        elif letter == "G":
            return 2
        elif letter == "T":
            return 3

    def compare(self, ntd_a, ntd_b):
        return self.kimura[self.numb(ntd_a)][self.numb(ntd_b)]

    def init(self):
        """ Initialize the matrix, i.e. fill the first line and column """
        # First cell is 0
        self.matrix[0][0].score = 0
        for i in range(len(self.seq_top)):
            self.matrix[0][i+1].score = 0
            self.matrix[0][i+1].prev_pos = [0,i]
        for j in range(len(self.seq_left)):
            self.matrix[j+1][0].score = 0
            self.matrix[j+1][0].prev_pos = [j, 0]

    def fill_matrix(self):
        """ Fill-up the matrix """
        for i in range(1,len(self.seq_left)+1):
            for j in range(1,len(self.seq_top)+1):
                # i numéro de ligne j numéro de colonne
                top = self.matrix[i-1][j].score + self.indel
                left = self.matrix[i][j-1].score + self.indel
                diag = self.matrix[i-1][j-1].score + self.compare(self.seq_top[j-1],self.seq_left[i-1])
                maximum = max(diag, left, top)
                if(maximum == diag):
                    self.matrix[i][j].score = diag
                    self.matrix[i][j].prev_pos = [i-1,j-1]
                elif(maximum == left):
                    self.matrix[i][j].score = left
                    self.matrix[i][j].prev_pos = [i,j-1]
                else:
                    self.matrix[i][j].score = top
                    self.matrix[i][j].prev_pos = [i-1,j]
                if maximum < 0:
                    self.matrix[i][j].score = 0

    def depart(self):
        max_score = 0
        depart_pos = [0, 0]
        for i in range(len(self.seq_left)):
            for j in range(len(self.seq_top)):
                if self.matrix[i][j].score >= max_score:
                    max_score = self.matrix[i][j].score
                    depart_pos = [i, j]
        return depart_pos

    def local_alignment(self):
        next_pos = self.depart()
        score = self.matrix[next_pos[0]][next_pos[1]].score
        current_score = score
        al_seq_top = ""
        al_seq_left = ""
        while(current_score != 0):
            work = self.matrix[next_pos[0]][next_pos[1]]
            work_pos = next_pos
            next_pos = work.prev_pos
            current_score = self.matrix[next_pos[0]][next_pos[1]].score
            # test s'il y a un gap
            if(next_pos != None and next_pos[0]-work_pos[0] == 0):
                # si gap horizontal
                al_seq_left = al_seq_left + "-"
                al_seq_top = al_seq_top + self.seq_top[work_pos[1]-1]
            elif(next_pos != None and next_pos[1]-work_pos[1] == 0):
                # si gap vertical
                al_seq_left = al_seq_left + self.seq_left[work_pos[0]-1]
                al_seq_top = al_seq_top + "-"
            else:
                # si pas de gap
                al_seq_left = al_seq_left + self.seq_left[work_pos[0]-1]
                al_seq_top = al_seq_top + self.seq_top[work_pos[1]-1]
        return al_seq_top,al_seq_left,score



def main():
    """ The main of TP3"""
    mat = DynamicMatrix("TGTTACGG", "GGTTGACTA", KIMURA_DISTANCE, -2)
    mat.init()
    mat.fill_matrix()
    print(mat)
    al_seq_top, al_seq_left, score = mat.local_alignment()
    nice_display(al_seq_top, al_seq_left, score)

# Launch the main
main()
# Exit without error
exit(0)
# Always put one extra return line
