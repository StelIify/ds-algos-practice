def partition(array, left_pointer, right_pointer):
    pivot_index = right_pointer
    pivot = array[right_pointer]
    right_pointer -= 1

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1
        while array[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

    array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]

    return left_pointer


def partition2(array, low, high) -> int:
    pivot = array[high]

    index = low - 1

    for i in range(low, high):
        if array[i] <= pivot:
            index += 1
            array[i], array[index] = array[index], array[i]

    index += 1
    array[high] = array[index]
    array[index] = pivot
    return index


def quick_sort(array, left_pointer, right_pointer) -> None:
    if right_pointer - left_pointer <= 0:
        return
    pivot_index = partition2(array, left_pointer, right_pointer)

    quick_sort(array, left_pointer, pivot_index - 1)
    quick_sort(array, pivot_index + 1, right_pointer)


test_array = [9, 3, 7, 4, 69, 420, 42]

test_array2 = [0, 5, 2, 1, 6, 3]

quick_sort(test_array2, 0, len(test_array2) - 1)
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array2)
print(test_array)
