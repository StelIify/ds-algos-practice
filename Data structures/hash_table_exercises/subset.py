arr1 = ["a", "b", "c", "d", "e", "f"]
arr2 = ["b", "d", "f"]


def is_subset(array1: list, array2: list) -> bool:
    """determine whether one array is subset of another"""

    # determine small and large array
    array1_copy = array1.copy()
    array2_copy = array2.copy()
    small_array: list
    large_array: list

    if len(array1) > len(array2):
        large_array = array1_copy
        small_array = array2_copy
    else:
        large_array = array2_copy
        small_array = array1_copy

    # store all items in large array in hash table

    hash_table = {el: True for el in large_array}

    for el in small_array:
        if not hash_table.get(el):
            return False
    return True


print(is_subset(arr1, arr2))