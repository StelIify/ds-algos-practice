# https://leetcode.com/problems/valid-anagram/

# solution 1

def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    anagram = {}
    anagram2 = {}

    for i, v in enumerate(s):
        anagram.setdefault(v, 0)
        anagram[v] += 1
        anagram2.setdefault(t[i], 0)
        anagram2[t[i]] += 1

    for v in s:
        if anagram[v] != anagram2.get(v, 0):
            return False
    return True


# solution 2

def is_anagram2(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return True if sorted(s) == sorted(t) else False
