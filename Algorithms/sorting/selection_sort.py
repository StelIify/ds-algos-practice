numbers_to_sort = [12, 1, 3, 5, 11, 8, 9, 22, 6, 17, 14, 15, 4, 7]
numbers_to_sort2 = [4, 2, 7, 1, 3]


def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        lowest_number_index = i
        for j in range(i + 1, len(numbers)):
            # find the lowest number index
            if numbers[j] < numbers[lowest_number_index]:
                lowest_number_index = j
        if lowest_number_index != i:  # check if lowest value not already in correct place
            numbers[i], numbers[lowest_number_index] = numbers[lowest_number_index], numbers[i]
    return numbers


print(selection_sort(numbers_to_sort2))
