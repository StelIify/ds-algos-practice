# You are given an integer array nums and an integer k.
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
#
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
#
# Return the maximum subarray sum of all the subarrays that meet the conditions.
# If no subarray meets the conditions, return 0.
# [1,5,4,2,9,9,9,7,6], k = 3

def max_sum_of_subarray(nums, k):
    current_sum = 0
    max_sum = 0

    distinct_numbers = {}
    for index, value in enumerate(nums):
        distinct_numbers.setdefault(value, 0)
        distinct_numbers[value] += 1
        current_sum += value

        distinct = len(distinct_numbers) == k
        if index >= k - 1 and distinct:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[index - (k - 1)]
            distinct_numbers.pop(nums[index - (k - 1)])
        elif index >= k - 1 and not distinct:
            current_sum -= nums[index - (k - 1)]
            if distinct_numbers[nums[index - (k - 1)]] == 1:
                distinct_numbers.pop(nums[index - (k - 1)])
            else:
                distinct_numbers[nums[index - (k - 1)]] -= 1
    return max_sum


print(max_sum_of_subarray([1, 5, 4, 2, 9, 9, 9], 3))
print(max_sum_of_subarray([1, 2, 2], 2))
