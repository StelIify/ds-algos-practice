def is_happy_number(n):
    def get_squired_digits_sum(n):
        return sum([int(d) ** 2 for d in str(n)])

    slow = n
    fast = get_squired_digits_sum(n)

    if n == 1:
        return True

    while fast != slow:
        if fast == 1:
            return True
        slow = get_squired_digits_sum(slow)
        fast = get_squired_digits_sum(get_squired_digits_sum(fast))
    return False


print(is_happy_number(2147483646))  # False
print(is_happy_number(28))  # True
