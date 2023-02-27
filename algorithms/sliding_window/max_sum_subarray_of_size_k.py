# find the max sum subarray of size k
# Example input [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], size= 3

def max_sum_of_subarray(nums, size):
    current_value = 0
    max_value = 0

    for index, value in enumerate(nums):
        current_value += value

        if index >= size -1:
            max_value = max(max_value, current_value)
            current_value -= nums[index - (size - 1)]
    return max_value


test_nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
test_size = 3
print(max_sum_of_subarray(test_nums, test_size))  # 16


def count_good_sub_string(s):
    current_sub_string = ""
    length = 3
    number_of_good_strings = 0

    for index, value in enumerate(s):
        current_sub_string += value

        if index >= length - 1:
            is_good = len(set(current_sub_string)) == length
            if is_good:
                number_of_good_strings += 1
            current_sub_string = current_sub_string.replace(s[index - (length -1)], "", 1)
    return number_of_good_strings


print(count_good_sub_string("aababcabc"))
