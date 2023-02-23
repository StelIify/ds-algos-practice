# find the max sum subarray of size k
# Example input [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], size= 3

def max_sum_of_subarray(nums, size):
    current_sum = 0
    max_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        if i >= size - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - (size - 1)]
    return max_sum


test_nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
test_size = 3
print(max_sum_of_subarray(test_nums, test_size))  # 16
