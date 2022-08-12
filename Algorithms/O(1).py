import time


# function with O(n) time complexity, goal to improve it to be O(1)
def find_last_name_On(names_dict, first_name):
    for current_first_name, last_name in names_dict.items():
        if current_first_name == first_name:
            return last_name


def find_last_name_O1(names: dict, first_name: str):
    return names.get(first_name)


def main():
    complexity = 2000000
    names_dict = get_name_dict(complexity)
    start = time.time()
    v = find_last_name_O1(names_dict, "bsqeeq")
    end = time.time()
    print(v)
    if (end - start) < 0.05:
        print("Fast :)")
    else:
        print("Slow :(")


def get_name_dict(num):
    names = {}
    for i in range(num):
        names[f"bree{i}"] = f"fuca{i}"
    return names


main()
