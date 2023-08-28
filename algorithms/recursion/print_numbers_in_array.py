# %%
array = [1,
         2,
         3,
         [4, 5, 6],
         7,
         [8,
          [9, 10, 11,
           [12, 13, 14]
           ]
          ],
         [15, 16, 17, 18, 19,
          [20, 21, 22,
           [23, 24, 25,
            [26, 27, 29]
            ], 30, 31
           ], 32
          ], 33
         ]


def print_numbers(numbers):
    for el in numbers:
        if isinstance(el, list):
            print_numbers(el)
        else:
            print(el)


# print_numbers(array)


# %%

def count_down(count):
    print(count)
    if count == 0:
        return
    else:
        count_down(count - 1)


# count_down(10)


# %%

def double_numbers(numbers, index=0):
    if index >= len(numbers):
        return
    numbers[index] *= 2
    double_numbers(numbers, index + 1)


# numbers = [1, 2, 3, 4, 5]
# double_numbers(numbers)
# print(numbers)

# top down strategy
def factorial1(number):
    if number == 1:
        return 1
    return number * factorial1(number - 1)


# bottom up strategy
def factorial2(number, index=1, result=1):
    if index > number:
        return result
    return factorial2(5, index + 1, result * index)


# print(factorial1(5))
# print(factorial2(5))

def array_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + array_sum(numbers[1:])


# print(array_sum([1, 2, 3, 4, 5]))

def reverse_string(string):
    if len(string) == 1:
        return string[0]
    return reverse_string(string[1:]) + string[0]


# print(reverse_string("Olex"))  # xelO


def array_string_sum(strings):
    if len(strings) == 0:
        return 0
    return len(strings[0]) + array_string_sum(strings[1:])


# print(array_string_sum(["ab", "c", "def", "ghij"]))


def contains_x(string, index=0):
    if string[0] == "x":
        return index
    return contains_x(string[1:], index + 1)


# print(contains_x("abcdefghijklmnopqrstuvwxyz"))


def unique_shortest_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_shortest_paths(rows - 1, columns) + unique_shortest_paths(rows, columns - 1)


# print(unique_shortest_paths(3, 4))


def find_max_value(numbers):
    if len(numbers) == 1:
        return numbers[0]
    print("recursive call")
    max_remainder = find_max_value(numbers[1:])
    if numbers[0] > max_remainder:
        return numbers[0]
    else:
        return max_remainder


# print(find_max_value([1, 2, 3, 4, 7, 5])) # 4


# fib with memoization

def fib(n, memo):
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]


print(fib(10, {}))
