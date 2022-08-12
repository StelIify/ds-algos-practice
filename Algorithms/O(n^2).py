def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if f'{first_name} {last_name}' == full_name:
                return True
    return False



def main():
    print(does_name_exist(get_first_names(100), get_last_names(100), "bob0 gonzalez0"))
    print(does_name_exist(get_first_names(500), get_last_names(500), "bob0 smith1"))
    print(does_name_exist(get_first_names(1000), get_last_names(1000), "bob500 smith6"))
    print(
        does_name_exist(
            get_first_names(2000), get_last_names(2000), "bob1999 wagner1998"
        )
    )
    print(
        does_name_exist(
            get_first_names(3000), get_last_names(3000), "sally2999 smith2998"
        )
    )


def get_first_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"bob{i}")
        elif m == 1:
            names.append(f"maria{i}")
        if m == 2:
            names.append(f"sally{i}")
    return names


def get_last_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"gonzalez{i}")
        elif m == 1:
            names.append(f"smith{i}")
        if m == 2:
            names.append(f"wagner{i}")
    return names


main()