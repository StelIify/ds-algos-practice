# https://leetcode.com/problems/3sum/
#

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue
        low = index + 1
        high = len(nums) - 1
        while low < high:
            sum = value + nums[low] + nums[high]
            if sum == 0:
                triplets.append([value, nums[low], nums[high]])
                low += 1
                while nums[low] == nums[low - 1] and low < high:
                    low += 1
            elif sum > 0:
                high -= 1
            else:
                low += 1
    return triplets


# print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([-1, 0, 1, 2, -1, -4]))
