from typing import List
# https://leetcode.com/problems/container-with-most-water/


def get_max_area(height: List[int]) -> int:
    low = 0
    high = len(height) - 1

    max_area = 0
    while low < high:
        min_height = min(height[low], height[high])
        max_area = max(max_area, min_height * (high - low))
        if len(height) == 2:
            return min_height
        elif height[low] <= height[high]:
            low += 1
        elif height[low] > height[high]:
            high -= 1
    return max_area


print(get_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(get_max_area([1, 1]))  # 1
print(get_max_area([4, 3, 2, 1, 4]))  # 16
print(get_max_area([1, 2, 4, 3]))  # 4
