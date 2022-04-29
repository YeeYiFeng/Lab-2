import statistics


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


def calc_median_temperature(x):
    x.sort()
    print(x)
    middle = len(x) / 2
    print(middle)
    if len(x) % 2 != 0:
        mediann = x[int(middle)]
    elif len(x) % 2 == 0:
        mediann = (x[int(middle)] + x[int(middle) - 1]) / 2
    print(mediann)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg = calc_average_temperature(num_list)
    minmax = calc_min_max_temperature(num_list)
    print(avg)
    print(minmax)
    calc_median_temperature(num_list)


if __name__ == "__main__":
    main()
