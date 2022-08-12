import random
import time

list_of_numbers = [n for n in range(0, 100)]

def get_nums(num):
    nums = []
    for i in range(num):
        nums.append(i)
    return nums

def time_it(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {round((end - start) * 100, 4)} mil seconds")
        return result

    return wrapper


def binary_search(target: int, numbers: list[int]):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        value_at_mid = numbers[mid]
        if value_at_mid == target:
            return mid
        elif value_at_mid < target:
            low = mid + 1
        else:
            high = mid - 1



# @time_it
# def linear_search(my_list, item):
#     for index, n in enumerate(my_list):
#         if n == item:
#             return index


def main():
    complexity = 2000000
    nums = get_nums(complexity)
    start = time.time()
    print(binary_search(int(complexity * 0.2344), nums))
    print(binary_search(int(complexity * 2), nums))
    print(binary_search(int(complexity + 1), nums))
    print(binary_search(int(complexity * 0.765), nums))
    end = time.time()
    if (end - start) < 0.05:
        print("Fast :)")
    else:
        print("Slow :(")

main()