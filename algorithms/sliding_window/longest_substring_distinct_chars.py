# Longest Substring Without Repeating Characters

# s = "bacabcbb" 3
# s = "bbbbb" 1
# s = "pwwkew"
def length_of_longest_substring(s):
    max_distinct_length = 0
    distinct_chars = set()
    left_index = 0
    for _, value in enumerate(s):
        while value in distinct_chars:
            distinct_chars.remove(s[left_index])
            left_index += 1

        distinct_chars.add(value)
        max_distinct_length = max(max_distinct_length, len(distinct_chars))
    return max_distinct_length


print(length_of_longest_substring("qrsvbspk"))







