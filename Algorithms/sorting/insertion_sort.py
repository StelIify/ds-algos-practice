nums_to_sort = [4, 2, 7, 1, 3]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp_value = nums[i]
        position = i - 1  # variable to compare values left of the temp_value

        while position >= 0 and nums[position] > temp_value:
            nums[position + 1] = nums[position]
            position -= 1

        nums[position + 1] = temp_value
    return nums


print(insertion_sort(nums_to_sort))
