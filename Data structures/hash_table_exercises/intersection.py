arr1 = [1, 2, 3, 4, 5, 6, 12, 14, 27]
arr2 = [0, 2, 4, 6, 8]


def intersection(array1: list, array2: list) -> list:
    """determine intersection of two arrays
    @:return list of intersected elements"""

    hash_table = {el: True for el in array1}

    intersected_elements = [el for el in array2 if hash_table.get(el)]

    return intersected_elements


print(intersection(arr1, arr2))