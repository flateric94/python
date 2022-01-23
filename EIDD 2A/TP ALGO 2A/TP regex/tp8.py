""" TP8 where we play with regex """
# Import regex
import re

def read_file_old(file_in):
    """ Read the file and return its content (array of tuples) """
    content = []
    # Open the file
    with open(file_in) as file:
        # The header of the current sequence
        header = False
        # For each line
        for line in file:
            # If the header is False, this is a new sequence
            if not header:
                # Backup the header
                header = line.strip()
            # Header is not False, we are in a sequence
            else:
                # Create a tuple (not modifiable) with the header and the sequence
                tmp = (header, line.strip())
                # Add it to the returned list
                content.append(tmp)
                # Put header to False
                header = False
    # Return the content of the file
    return content

def read_file(file_in):
    """ Read the file and return its content (array of tuples) """
    content = []
    # Open the file
    with open(file_in) as file:
        # For each line
        for line in file:
            # Get the header
            header = line.strip()
            # Get the sequence
            seq = file.readline().strip()
            # Create a tuple (not modifiable) with the header and the sequence
            tmp = (header, seq)
            # Add it to the returned list
            content.append(tmp)
    # Return the content of the file
    return content

def main():
    """ The main of TP8 that launch regex """
    # The file to process
    file_in = "sequences.fasta"
    # Get its content
    content = read_file(file_in)

    # Get all occurrences of 'GTA'
    res = []
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        res += re.findall("GTA", i[1])
    print("Q2: There is {} 'GTA' in the file".format(len(res)))


    # Is there a sequence containing 'GTA(some characters)CT'?
    # Not founded yet
    founded = False
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        if re.search("GTA.*CT", i[1]):
            # We found one!
            founded = True
            # Stop the process
            break
    # Did we find it?
    if founded:
        print("\nQ3: There is!")
    else:
        print("\nQ3: There is not :(")


    # Is there a sequence containing 'GTA(max 3 characters)CTAAT'?
    # Not founded yet
    founded = False
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        if re.search("GTA.{0,3}CTAAT", i[1]):
            # We found one!
            founded = True
            # Stop the process
            break
    # Did we find it?
    if founded:
        print("\nQ4: There is!")
    else:
        print("\nQ4: There is not :(")

    # Is there a sequence containing 'GG T or C GG'?
    # Not founded yet
    founded = False
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        if re.search("GG[TC]GG", i[1]):
        #if re.search("GGCGG|GGTGG", i[1]):
        #if re.search("GG(C|T)GG", i[1]):
            # We found one!
            founded = True
            # Stop the process
            break
    # Did we find it?
    if founded:
        print("\nQ5: There is!")
    else:
        print("\nQ5: There is not :(")


    # Is there a sequence finishing by 'ATATAT'?
    # Not founded yet
    founded = False
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        if re.search("ATATAT$", i[1]):
            # We found one!
            founded = True
            # Stop the process
            break
    # Did we find it?
    if founded:
        print("\nQ6: There is!")
    else:
        print("\nQ6: There is not :(")

    # Is there a sequence starting or finishing by 'ATATAT'?
    # Not founded yet
    founded = False
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only
        if re.search("^ATATAT|ATATAT$", i[1]):
            # We found one!
            founded = True
            # Stop the process
            break
    # Did we find it?
    if founded:
        print("\nQ7: There is!")
    else:
        print("\nQ7: There is not :(")


    # Get headers containing mmus or musm
    res = []
    # For each headers/sequences
    for i in content:
        # Regex on the header only, starting and ending by anything and containing something that is not A, C, G or T
        if re.search("mmus|musm", i[0]):
            res.append(i[0])
    print("\nQ8: Mus Musculus headers: {}".format(res))


    # Count headers containing / or \
    res = []
    # For each headers/sequences
    for i in content:
        # Regex on the header only, you need to escape the escape... \\ is a literal \ IN THE REGEX, so you need to escape it. Python only.
        if re.search("\\\\|/", i[0]):
            res.append(i[0])
    print("\nQ9: There is {} headers containing (back)slash".format(len(res)))


    # Find the sequence containing not only DNA
    res = []
    # For each headers/sequences
    for i in content:
        # Regex on the sequence only, starting and ending by anything and containing something that is not A, C, G or T
        res += re.findall("^.*[^ACGT].*$", i[1])
    print("\nQ10: Buggy sequence: {}".format(res))


    # Get the part of headers containing an id composed of 3 letters, 1 digit, 1 alphanumeric character, 1 character and surrounded by spaces
    res = []
    # For each headers/sequences
    for i in content:
        # Regex on the header only
        res += re.findall("\ [A-Za-z]{3}\d{1}\w{1}.{1}\ ", i[0])
    print("\nQ11: Special header sequences: {}".format(res))


    # Get the sequence where the header contains an email address.
    res = ""
    # For each headers/sequences
    for i in content:
        # Regex on the header only
        if re.search("[^\W][a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*\@[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*\.[a-zA-Z]{2,4}", i[0]):
            res = i[1]
    print("\nQ12: Sequence with email on the header: {}".format(res))

# Launch the main
main()
# Exit without error
exit(0)
# Always put one extra return line
