# Given a string, s, that represents a DNA subsequence, and a number kk,
# return all the contiguous subsequences (substrings) of length kk that occur more than once in the string.
# The order of the returned subsequences does not matter. If no repeated substring is found,
# the function should return an empty set.


def find_repeated_sequence(s, k):
    uniques = set()
    sequences = set()
    l, r = 0, 0
    while r < len(s):
        r += 1
        if r >= k - 1:
            sequence = s[l:r + 1]
            if sequence in uniques:
                sequences.add(sequence)
            uniques.add(sequence)
            l += 1
    return sequences


test = "GAGTCACAGTAGTTTCA"
k = 3
print(find_repeated_sequence(test, k))  # AGT, TCA
