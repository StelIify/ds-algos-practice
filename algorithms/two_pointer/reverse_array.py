# reverse array

def reverse(array):
    l = 0
    r = len(array) - 1

    while l <= r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array


print(reverse([1, 2, 3, 4, 5, 6]))
