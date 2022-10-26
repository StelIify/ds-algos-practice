def find_min(nums: list):
    min_number = float("inf")
    for num in nums:
        if num < min_number:
            min_number = num
    return min_number


def find_max(nums: list):
    max_number = 0
    for number in nums:
        if number > max_number:
            max_number = number
    return max_number


print(find_min([7, 4, 3, 100, 2343243, 343434, 1, 2, 32]))
print(find_max([7, 4, 3, 100, 2343243, 343434, 1, 2, 32]))
