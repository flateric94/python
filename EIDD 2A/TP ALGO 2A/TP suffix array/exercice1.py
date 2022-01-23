# Import the Suffix Array object
import suffix_array as sa
import unittest


""""
QUESTION 1)

Pour rechercher les premières positions de la chaîne où 
apparaît un motif, quel algorithme peut-on utiliser ?
-> dichotomie

"""
def first_occurrence(suffix_array, pattern):
    start = 0
    end = len(suffix_array.array) - 1
    while start < end:
        middle = (start + end) // 2
        if suffix_array.string[suffix_array.array[middle]:suffix_array.array[middle]+len(pattern)] < pattern:
            start = middle + 1
        else:
            end = middle
    return suffix_array.array[start]
    

def match(suffix_array, pattern):
    start = 0
    end = len(suffix_array.array) - 1
    while start < end:
        middle = (start+end) // 2
        if suffix_array.string[suffix_array.array[middle]:suffix_array.array[middle]+len(pattern)] < pattern:
            start = middle + 1
        else:
            end = middle
    begin = start
    end = len(suffix_array.array) - 1
    while start < end:
        middle = (start+end) // 2
        if suffix_array.string[suffix_array.array[middle]:suffix_array.array[middle]+len(pattern)] > pattern:
            end = middle
        else:
            start = middle + 1
    result = []
    for i in range(begin, end):
        result.append(suffix_array.array[i])
    return result
 



def main():
    my_sa = sa.SuffixArray("ACACAG")
    print("i\tSA\tSuffix")
    for pos, val in enumerate(my_sa.array):
        print("{}\t{}:\t{}".format(pos, val, my_sa.string[val:]))
    print(my_sa)
    print(match(my_sa,"AG"))
    # TEST FIRST_OCCURRENCE
    assert first_occurrence(my_sa, "A") == 0
    assert first_occurrence(my_sa, "AC") == 0
    assert first_occurrence(my_sa, "ACA") == 0
    assert first_occurrence(my_sa, "ACAG") == 2
    assert first_occurrence(my_sa, "CA") == 1
    assert first_occurrence(my_sa, "CAC") == 1
    assert first_occurrence(my_sa, "CAG") == 3
    assert first_occurrence(my_sa, "G") == 5

    # TEST MATCH
    assert match(my_sa, "A") == [0,2,4]
    assert match(my_sa, "AC") == [0,2]
    assert match(my_sa, "CA") == [1,3]
    

    unittest.main()

main()