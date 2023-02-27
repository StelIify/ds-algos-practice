from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def two_sum(numbers: List, target: int) -> List[int]:
    low = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high) // 2
        if numbers[low] + numbers[high] == target:
            return [low +1, high +1]
        elif numbers[low] + numbers[high] < target:
            low = + 1
        else:
            high = mid - 1


# print(two_sum([2, 7, 11, 15], 9))  # [1, 2]
print(two_sum([5, 25, 75], 100))
