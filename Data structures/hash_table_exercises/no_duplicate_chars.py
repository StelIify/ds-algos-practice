

def get_non_duplicate_chars(message: str) -> list[str]:
    number_of_occur = {}
    for char in message.lower():
        number_of_occur.setdefault(char, 0)
        number_of_occur[char] += 1
    non_duplicates = [key for key, value in number_of_occur.items() if value == 1]
    return non_duplicates



u_message = "minimum"
print(get_non_duplicate_chars(u_message)) # expected output ["n", "u"]