def linear_search_on_ordered_array(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            print('Searched value was not found in the array')
            break
    return None


print(linear_search_on_ordered_array([11, 22, 33, 44, 55], 24))


# we need to define lower bound and higher bound of the array(start and end)
# define middle position
# we run algorithm while lower bound < higher
# we choose element in the middle of array
# check if this value is what we are looking for
# if not, check if it's lower or higher than value that we search for
# if searched value higher than selected element we increase

def binary_search(ordered_array, search_value):
    start = 0
    end = len(ordered_array) - 1

    while start <= end:
        middle = (end + start) // 2

        picked_value = ordered_array[middle]

        if picked_value == search_value:
            return middle
        elif picked_value < search_value:
            start = middle + 1
        else:
            end = middle - 1


print(binary_search([1, 3, 5, 7, 9, 11, 13], 9))