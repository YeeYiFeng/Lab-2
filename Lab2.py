def display_main_menu():
    print("display_main_menu")


def get_user_input():
    print('Enter User Input:')
    x = input()
    print(x)
    y = x.split(",")
    print(y)
    i = []
    for z in y:
        i.append(float(z))
    return i


def calc_average_temperature(x):
    avg = sum(x) / len(x)
    return avg


def calc_min_max_temperature(x):
    minmax = []
    minmax = [min(x), max(x)]
    return minmax


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg = calc_average_temperature(num_list)
    minmax = calc_min_max_temperature(num_list)
    print(avg)
    print(minmax)


if __name__ == "__main__":
    main()
