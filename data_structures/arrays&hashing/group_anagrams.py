# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

# my first solution...O(n3)
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = []
    for index, string in enumerate(strs):
        if index > 0 and any(string in el for el in anagrams):
            continue
        anagram1 = {}
        for v in string:
            anagram1.setdefault(v, 0)
            anagram1[v] += 1

        new_list = []
        for i in range(index + 1, len(strs)):
            string2 = strs[i]
            anagram2 = {}

            for v in string2:
                anagram2.setdefault(v, 0)
                anagram2[v] += 1

            if anagram1 == anagram2:
                new_list.append(string2)

        new_list.append(string)
        anagrams.append(new_list)
    return anagrams


def group_anagrams2(strs: List[str]) -> List[List[str]]:
    anagram_dic = {}

    for string in strs:
        sorted_string = "".join(sorted(string))

        if sorted_string not in anagram_dic:
            anagram_dic[sorted_string] = [string]
        else:
            anagram_dic[sorted_string].append(string)
    final = []
    for value in anagram_dic.values():
        final.append(value)
    return final


print(group_anagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
