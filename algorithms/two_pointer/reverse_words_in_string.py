import re


def reverse_words_in_string(s: str):
    words = s.split(" ")
    words = [word for word in words if word]
    l = 0
    r = len(words) - 1

    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
    return " ".join(words)


print(reverse_words_in_string("Welcome to Educative"))  # Educative to Welcome
