class SuffixArray:
    """ Adapted from https://pypi.org/project/pysuffixarray/ """

    def __init__(self, string):
        self.string = string + '$'
        self.array = self._construct_suffix_array(self.string)

    def _construct_suffix_array(self, string):
        """ Constructs suffix array in O(nlogn) time by sorting ranking
            pairs of suffixes."""
        string_len = len(string)
        suffix_array = list(range(string_len))
        rank_array = [ord(c) for c in string]

        k = 1
        # This sorting process will be repeated at most log(n) times.
        while k < string_len:
            # At first, sort suffixes with the first elements of ranking pairs.
            suffix_array = self._sort(suffix_array, rank_array, string_len, k)
            # Next, sort suffixes with the second elements of ranking pairs.
            suffix_array = self._sort(suffix_array, rank_array, string_len, 0)
            # Recompute rank of suffixes.
            rank_array = self._rerank(suffix_array, rank_array, k)
            k *= 2

        return suffix_array

    def _sort(self, suffix_array, rank_array, string_len, k):
        """ Sorts suffixes by count-sorting rank array.
            Offset k is defined such that the value used when sorting
            suffix i corresponds to rank_array[i + k].
        """
        max_length = max(2**7 - 1, string_len)
        count = [0] * max_length

        for i in range(len(rank_array)):
            if i + k < string_len:
                count[rank_array[i + k]] += 1
            else:
                count[0] += 1

        cumsum = 0
        for i in range(max_length):
            tmp = count[i]
            count[i] = cumsum
            cumsum += tmp

        temp_suffix_array = [-1] * string_len
        for i, _ in enumerate(suffix_array):
            if suffix_array[i] + k < string_len:
                target_index = rank_array[suffix_array[i] + k]
            else:
                target_index = 0

            temp_suffix_array[count[target_index]] = suffix_array[i]
            count[target_index] += 1

        return temp_suffix_array

    def _rerank(self, suffix_array, rank_array, k):
        """ Recomputes rank of suffixes. When consecutive suffixes with
            identical ranking pairs are found,
            assigns same ranks to them.
        """
        temp_rank_array = [0] * len(rank_array)
        r, s = rank_array, suffix_array

        rank = 0
        for i in range(1, len(rank_array)):
            # When ranking pairs are identical, do not increment the rank.
            if r[s[i]] == r[s[i-1]] and r[s[i] + k] == r[s[i-1] + k]:
                temp_rank_array[s[i]] = rank
            else:
                rank += 1
                temp_rank_array[s[i]] = rank

        return temp_rank_array

    # self representation for print
    def __repr__(self):
        # Return the content of the cell
        ret = "String {}\nSuffix array: {}\n".format(self.string, self.array)
        ret += "\nEasier representation:\ni\tSA\tSuffix\n"
        for pos, val in enumerate(self.array):
            ret += "{}\t{}:\t{}\n".format(pos, val, self.string[val:])
        return ret
