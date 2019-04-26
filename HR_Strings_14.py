# HackerRank Strings 14 Merge The Tools!


def problem_solution(input_string, k):
    # Task function
    count = 0
    print_string = ''

    for symbol in input_string:
        if symbol not in print_string:
            print_string += symbol
        count += 1

        if count == k:
            print(print_string)
            count = 0
            print_string = ''

    if len(print_string) != 0:
        print(print_string)


def main():
    # Initialization
    input_string = ''
    k = 0
    min_len = 0
    max_len = 10 ** 4

    while not min_len < len(input_string) <= max_len:
        input_string = input()

    n = len(input_string)
    while k == 0 or n % k != 0:
        k = int(input())

    problem_solution(input_string, k)


if __name__ == '__main__':
    main()
