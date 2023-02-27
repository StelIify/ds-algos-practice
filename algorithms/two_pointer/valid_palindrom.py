import re

# https://leetcode.com/problems/valid-palindrome/


def is_palindrome(s: str) -> bool:
    new_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    low = 0
    high = len(new_str) - 1
    if new_str == "":
        return True

    while low <= high:
        if new_str[low] == new_str[high]:
            low += 1
            high -= 1
        else:
            return False
    return True


print(is_palindrome("ab_a"))
