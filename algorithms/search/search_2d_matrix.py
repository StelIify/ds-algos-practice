from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        start = 0
        end = len(row) - 1
        while start <= end:
            mid = (end + start) // 2
            picked_value = row[mid]

            if picked_value == target:
                return True
            elif picked_value < target:
                start = mid + 1
            else:
                end = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix2 = [[1], [3]]
print(search_matrix(matrix2, target=3))  # true
