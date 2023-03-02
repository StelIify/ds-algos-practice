from typing import List


def number_of_paths(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)


# print(number_of_paths(5))


def anagram_generation(string: str) -> List[str]:
    if len(string) == 1:
        return [string[0]]
    anagrams = []

    substring_anagrams = anagram_generation(string[1:])

    for substring in substring_anagrams:
        for index in range(len(substring) +1):
            anagram_copy = substring[:]
            new_anagram = anagram_copy[:index] + string[0] + anagram_copy[index:]
            anagrams.append(new_anagram)

    return anagrams


test_string = "oleksandr"
print(anagram_generation(test_string))
print(len(anagram_generation(test_string)))

# ["abc","acb","bac", "bca", "cab","cba"]
