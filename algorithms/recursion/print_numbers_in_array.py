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


print_numbers(array)


# %%

def count_down(count):
    print(count)
    if count == 0:
        return
    else:
        count_down(count - 1)


count_down(10)


# %%

def double_array(array, index=0):
    if index >= len(array):
        return

    array[index] *= 2
    double_array(array, index + 1)


array = [1, 2, 3, 4, 5]
double_array(array)
print(array)

# %%


def sum_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_numbers(numbers[1:len(numbers)])


nums = [1, 2, 3, 4, 5]
print(sum_numbers(nums))