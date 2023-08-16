# https://leetcode.com/problems/valid-parentheses/

def is_valid(string) -> bool:
    close_to_open = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


print(is_valid(")(){}"))
