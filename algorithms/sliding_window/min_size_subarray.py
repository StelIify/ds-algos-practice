# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


def min_sub_array_length(nums: List[int], target: int) -> int:
    left_p = 0
    total = 0
    min_sub_length = float("inf")

    for right_p, value in enumerate(nums):
        total += value
        while total >= target:
            min_sub_length = min(min_sub_length, (right_p - left_p) + 1)
            total -= nums[left_p]
            left_p += 1
    return 0 if min_sub_length == float("inf") else min_sub_length


def min_sub_array_length2(nums, target):
    current = 0
    min_length = float("inf")
    sub_length = 0

    for index, value in enumerate(nums):
        current += value
        sub_length += 1
        while current >= target:
            min_length = min(min_length, sub_length)
            current -= nums[index - (sub_length - 1)]
            sub_length -= 1
    return 0 if min_length == float("inf") else min_length


print(min_sub_array_length2([2, 3, 1, 2, 4, 3], 7))  # 2
print(min_sub_array_length2([1, 4, 4], 4))  # 1
