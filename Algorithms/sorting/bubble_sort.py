numbers_to_sort = [12, 1, 3, 5, 11, 8, 9, 22, 6, 17, 14, 15, 4, 7]


def bubble_sort(numbers: list[int]) -> list[int]:
    list_to_sort = numbers.copy()
    swapping = True
    array_len = len(numbers) - 1
    while swapping:
        swapping = False
        for i in range(array_len):
            if list_to_sort[i] > list_to_sort[i + 1]:
                # element_to_swap = list_to_sort[i]
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                # list_to_sort[i + 1] = element_to_swap
                swapping = True
        array_len -= 1
    return list_to_sort


print(bubble_sort(numbers_to_sort))
