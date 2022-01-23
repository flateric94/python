import random
import time

'''
Question 1) 
Implement a naive algorithm of exact pattern matching in the function
'''

def naive_exact_pattern_matching(pattern, text):
    result=[]
    # Start of the matching
    for i in range(0,len(text)-len(pattern)+1):
        if(text[i:i+len(pattern)] == pattern):
            result.append(i)
    return result

'''
Question 2)
Write a class RollingHash taking two arguments (text and k, the size of the pattern)
• define the alphabet mapping (A=0, C=1, G=2, T=3),
• store the length of the alphabet (a),
• compute the hash of the first portion of k characters (k-mer) of text,
• create two index, one for the starting position of current hash, and one for the ending position of
current hash.
'''

class RollingHash:
    """ The main class for rolling hash, k is the size of the pattern"""
    def __init__(self, text, k):
        """ Initialize all needed variables and compute the first hash """
        self.text = text
        self.k = k
        # Maps characters to int
        self.alphabet = {'A':0, 'C':1, 'G':2, 'T':3}
        # Size of the alphabet
        self.a = 4
        # Compute the first hash
        self.hash = 0
        for i in range(0,k):
            self.hash += self.alphabet[self.text[i]]*(self.a**(k-i-1))
        # Start and End of the current hash
        self.init=0
        self.end=k-1

    # Operations for the next hash
    def next_hash(self):
        # supression du terme
        self.hash -= self.alphabet[self.text[self.init]]*(self.a**(self.k-1))
        # ajout du terme
        self.hash *= self.a
        self.hash += self.alphabet[self.text[self.end+1]]
        # MAJ des indexs
        self.init+=1
        self.end+=1
        
    # Return of the current hash   
    def get_hash(self):
        return self.hash

    # Return of the current k-mer
    def get_string(self):
        return self.text[self.init:self.end+1]

'''
Question 3)
Duplicate and modify your naive algorithm to implement rabin_karp(pattern, text)
'''

def rabin_karp(pattern, text):
    result = []
    # Initialize of the hashs
    hash_text = RollingHash(text, len(pattern))
    hash_pattern = RollingHash(pattern, len(pattern))  
    # Start the search of matching  
    for i in range(1,len(text)-len(pattern)+1):
        if hash_text.get_hash() == hash_pattern.get_hash() and hash_text.get_string() == pattern:
            result.append(i-1)
            hash_text.next_hash()
        else :
            hash_text.next_hash()
    # Because we're always looking for the next hash, at the index len(text)-1 there's not operations possible (Index size error)
    # So, we do this test
    if hash_text.get_hash() == hash_pattern.get_hash() and hash_text.get_string() == pattern:
        result.append(len(text)-1) 
    return result 

def generator_of_sequence(size):
    result = ""
    alphabet = ["A","C","G","T"]
    for i in range(0,size):
        result += alphabet[random.randrange(4)]
    return result

def main():
    #Tests question 1
    pattern="AG"
    text="ATAGCTAGCAT"
    print(naive_exact_pattern_matching(pattern,text))
    text+="AG"
    print(naive_exact_pattern_matching(pattern,text))

    # intialisation des séquences
    text = generator_of_sequence(10)
    pattern = generator_of_sequence(2)
    print("Sequence : ",text,"\nPattern : ", pattern)

    # Méthode naive
    start_time = time.time()
    result = naive_exact_pattern_matching(pattern,text)
    end_time = time.time()
    print("---- Methode naive\nTemps : ",end_time-start_time,"\nResultat : ",result)

    # Méthode rabin_karp
    start_time = time.time()
    result=rabin_karp(pattern,text)
    end_time = time.time()
    print("---- Methode Rabin_Karp\nTemps : ",end_time-start_time,"\nResultat : ",result)

    '''
    Conclusion :
    Rabbin karp is lower than Naive's methods, because python already use hashcodes in his implementation.
    '''
main()