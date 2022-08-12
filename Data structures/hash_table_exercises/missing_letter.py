import string


def missing_letter(message: str, alphabet) -> str:
    """accepts a string that contains all the letters of the
    alphabet except one and returns the missing letter."""
    msg = list(message.replace(" ", ""))

    msg_hash_table = {el: True for el in msg}

    for letter in alphabet:
        if not msg_hash_table.get(letter):
            return letter


alphabet = string.ascii_lowercase
u_message = "the quick brown box jumps over a lazy dog"
print(missing_letter(message=u_message, alphabet=alphabet))
# expected output "f"
