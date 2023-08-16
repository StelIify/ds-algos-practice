from collections import deque
from typing import List


# https://leetcode.com/problems/sliding-window-maximum/
# Given an integer list, nums, find the maximum values in all the contiguous subarrays
# (windows) of size w.

# nums [-4, 2, -5, 3, 6], window size = 3, result: 2, 3, 6

def find_max_values(lst, size) -> List[int]:
    output = []
    temp_window = deque()
    for index, value in enumerate(lst):
        temp_window.append(value)
        if index >= size - 1:
            output.append(max(temp_window))
            temp_window.popleft()
    return output


def find_max_sliding_window(nums, size):
    if len(nums) == 0:
        return []
    if size > len(nums):
        size = len(nums)
    output = []
    max_values = deque()  # Use a deque to maintain the maximum values within the sliding window
    for index, value in enumerate(nums):
        # Remove elements that are out of the current sliding window
        while max_values and max_values[0] <= index - size:
            max_values.popleft()

        # Remove elements from the end of the deque that are smaller than the current element
        while max_values and nums[max_values[-1]] < value:
            max_values.pop()
        max_values.append(index)
        # The front of the deque contains the index of the maximum element within the window
        if index >= size - 1:
            output.append(nums[max_values[0]])
    return output


# function to find the maximum in all possible windows
def find_max_sliding_window2(nums, w_size):
    if len(nums) == 0:
        return []
    output = []
    current_window = deque()  # store index
    left_p = 0
    right_p = 0

    while right_p < len(nums):
        # pop smaller value from the window
        while current_window and nums[current_window[-1]] < nums[right_p]:
            current_window.pop()
        current_window.append(right_p)

        # remove left value from window
        if left_p > current_window[0]:
            current_window.popleft()
        if (right_p + 1) >= w_size:
            output.append(nums[current_window[0]])
            left_p += 1
        right_p += 1
    return output


test_case = [-4, 2, -5, 3, 6]
test_case2 = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
# print(find_max_values(test_case2, 3))
print(find_max_sliding_window2(test_case2, 3))
