from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, value in enumerate(nums):
        remaining = target - value

        if remaining in seen:
            return [seen[remaining], index]
        seen[value] = index


test_nums = [2, 1, 5, 3]
test_target = 4

print(two_sum(test_nums, test_target)) # [1, 3]
