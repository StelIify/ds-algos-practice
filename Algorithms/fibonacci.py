def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def main():
    for i in range(33):
        print(f"Input: {i} -> {fibonacci_recursive(i)}")


main()