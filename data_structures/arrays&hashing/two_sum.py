from typing import List


# https://leetcode.com/problems/two-sum/description/

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        number_to_find = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == number_to_find:
                return [i, j]
    return None


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, value in enumerate(nums):
        remaining = target - value

        if remaining in seen:
            return [seen[remaining], index]
        seen[value] = index


test_nums = [2, 1, 5, 3]
test_target = 4

print(two_sum(test_nums, test_target))  # [1, 3]
