""" TP7 where we perform some fuzzy string comparison """
import time
import tracemalloc

def get_all_uniq_kmers(genome_file, k):
    """ Get each and every kmer (only one time) of a file """
    # Open the file
    with open(genome_file) as file:
        # Skip first line
        next(file)
        # Get the genome WITHOUT LAST CHAR
        genome = next(file).strip()
        # The set that will contains all uniq k-mers
        k_mers = set()
        # K-mer decomposition
        for i, _ in enumerate(genome[:len(genome)-k+1]):
            # Add the current k-mer
            k_mers.add(genome[i:i+k])
    return k_mers

def jaccard_index(k_mers_1, k_mers_2):
    """ Compute Jaccard distance between two sets """
    # Count how many k-mers are in both set1 and set2
    shared_k_mers = 0
    # For each k-mer in set1
    for i in k_mers_1:
        # If this k-mer is in set 2
        if i in k_mers_2:
            # It is a shared one
            shared_k_mers += 1
    # Jaccard index: |AnB| / (|A| + |B| - |AnB|)
    jaccard = shared_k_mers / (len(k_mers_1) + len(k_mers_2) - shared_k_mers)

    return jaccard

def min_hash(genome_file, k, n):
    """ Get the MinHash of a file. N is the number of minimal hash we want """
    # Open the file
    with open(genome_file) as file:
        # Skip first line
        next(file)
        # Get the genome
        genome = next(file)
        # Initialize the array
        hashes = []
        # Last position in the genome after the array is full
        next_pos = 0
        # First step: fill the array with n element
        # K-mer decomposition
        for i, _ in enumerate(genome[:len(genome)-k]):
            # Get the current hash
            tmp_hash = hash(genome[i:i+k])
            # if it is not already in our array
            if tmp_hash not in hashes:
                # If the array is not full
                if len(hashes) < n:
                    # Add the current k-mer
                    hashes.append(tmp_hash)
                else:
                    # Sort the array
                    hashes.sort()
                    # Backup next i value
                    next_pos = i + 1
                    # Exit this loop
                    break
        # Second step: add only the smallest hashes and keep the array sorted
        # K-mer decomposition, from next_pos
        for i, _ in enumerate(genome[next_pos:len(genome)-k]):
            # Get the current hash, /!\ it starts at i+next_pos /!\
            current_hash = hash(genome[i+next_pos:i+next_pos+k])
            # if it is not already in our array
            # and it is smaller than the biggest element
            if current_hash not in hashes and current_hash < hashes[-1]:
                # Update the last one
                hashes[-1] = current_hash
                # Sort the array
                hashes.sort()
    # Return the hashes array
    return hashes

def min_hash_binary(genome_file, k, n):
    """ Get the MinHash of a file. N is the number of minimal hash we want """
    # Open the file
    with open(genome_file) as file:
        # Skip first line
        next(file)
        # Get the genome
        genome = next(file)
        # Initialize the array
        hashes = []
        # Last position in the genome after the array is full
        next_pos = 0
        # First step: fill the array with n element
        # K-mer decomposition
        for i, _ in enumerate(genome[:len(genome)-k]):
            # Get the current hash
            tmp_hash = hash(genome[i:i+k])
            # if it is not already in our array
            if tmp_hash not in hashes:
                # If the array is not full
                if len(hashes) < n:
                    # Add the current k-mer
                    hashes.append(tmp_hash)
                else:
                    # Sort the array
                    hashes.sort()
                    # Backup next i value
                    next_pos = i + 1
                    # Exit this loop
                    break
        # Second step: add only the smallest hashes and keep the array sorted
        # K-mer decomposition, from next_pos
        for i, _ in enumerate(genome[next_pos:len(genome)-k]):
            # Get the current hash, /!\ it starts at i+next_pos /!\
            current_hash = hash(genome[i+next_pos:i+next_pos+k])
            # if it is not already in our array
            # and it is smaller than the biggest element
            if current_hash not in hashes and current_hash < hashes[-1]:
                # Find where we should add it (binary search)
                # From beginning...
                beg_pos = 0
                # To last item (we already check the last one)
                end_pos = len(hashes) - 1
                # While we are not at the correct position
                while beg_pos < end_pos:
                    # Where to look
                    mid_pos = (beg_pos + end_pos) // 2
                    # If the hash is bigger than the looked element
                    if current_hash > hashes[mid_pos]:
                        # Skip the current mid_pos, already tested
                        beg_pos = mid_pos + 1
                    else:
                        # Skip the current mid_pos
                        end_pos = mid_pos
                # Insert the value in the array
                hashes.insert(beg_pos, current_hash)
                # Remove last pos of the array
                hashes.pop()
    # Return the hashes array
    return hashes

def main():
    """ The main of TP7 """
    #file1 = "small1.fasta"
    #file2 = "small2.fasta"
    file1 = "20K1.fasta"
    file2 = "20K2.fasta"
    #file1 = "e_coli_IAI39.fasta"
    #file2 = "e_coli_UMN026.fasta"
    k = 30
    n = 500
    ram_stat = False

    if ram_stat:
        # Start mem trace footprint
        tracemalloc.start()
    # Get the current time
    start = time.time()
    # Naive algorithm
    k_mers_1 = get_all_uniq_kmers(file1, k)
    k_mers_2 = get_all_uniq_kmers(file2, k)
    print("{:.2f}%".format(jaccard_index(k_mers_1, k_mers_2)*100))
    # Get the current time
    end = time.time()
    # Print the execution time (2 digits precision)
    print("Naive: {:.2f}s".format(end - start))
    if ram_stat:
        # Print the mem footprint
        snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)
        # Stop the trace
        tracemalloc.stop()

        # Start mem trace footprint
        tracemalloc.start()
    # Get the current time
    start = time.time()
    min_hash_1 = min_hash(file1, k, n)
    min_hash_2 = min_hash(file2, k, n)
    print("{:.2f}%".format(jaccard_index(min_hash_1, min_hash_2)*100))
    # Get the current time
    end = time.time()
    # Print the execution time (2 digits precision)
    print("MinHash: {:.2f}s".format(end - start))
    if ram_stat:
        # Print the mem footprint
        snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)
        # Stop the trace
        tracemalloc.stop()

        # Start mem trace footprint
        tracemalloc.start()
    # Get the current time
    start = time.time()
    min_hash_1 = min_hash_binary(file1, k, n)
    min_hash_2 = min_hash_binary(file2, k, n)
    print("{:.2f}%".format(jaccard_index(min_hash_1, min_hash_2)*100))
    # Get the current time
    end = time.time()
    # Print the execution time (2 digits precision)
    print("MinHashBinary: {:.2f}s".format(end - start))
    if ram_stat:
        # Print the mem footprint
        snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)
        # Stop the trace
        tracemalloc.stop()


def display_top(snapshot, key_type='lineno'):
    """ RAM usage statistics """
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

# Launch the main
main()
# Exit without error
exit(0)
# Always put one extra return line