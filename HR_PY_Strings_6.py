# HackerRank Strings 6 String Validators


def problem_solution(current_string):
    # Task function
    flags = [False for i in range(5)]

    for current_symbol in current_string:
        if current_symbol.isalnum():
            flags[0] = True

        if current_symbol.isalpha():
            flags[1] = True

        if current_symbol.isdigit():
            flags[2] = True

        if current_symbol.islower():
            flags[3] = True

        if current_symbol.isupper():
            flags[4] = True

    for flag in flags:
        print(flag)


def main():
    # Initialization
    current_string = ''

    while not 0 < len(current_string) <= 1000:
        current_string = input().strip()

    problem_solution(current_string)


if __name__ == '__main__':
    main()
