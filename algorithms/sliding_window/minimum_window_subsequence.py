#
def min_window(str1, str2) -> str:
    size1, size2 = len(str1), len(str2)
    p1, p2 = 0, 0
    min_sub_len = float("inf")
    min_sub = ""

    while p1 < size1:
        if str1[p1] == str2[p2]:
            p2 += 1
            if p2 == size2:
                start, end = p1, p1
                p2 -= 1
                while p2 >= 0:
                    if str1[start] == str2[p2]:
                        p2 -= 1
                    start -= 1
                start += 1
                if end - start + 1 < min_sub_len:
                    min_sub_len = end - start + 1
                    min_sub = str1[start: end + 1]
                p1 = start
                p2 = 0
        p1 += 1
    return min_sub


test_case1 = "abcdebdde"
test_case_1_str2 = "bde"
print(min_window(test_case1, test_case_1_str2))  # bcde
