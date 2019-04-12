# HackerRank Strings 12 Capitalize!


def problem_solution(input_string):
    # Task function
    final_string = ''
    previous_symbol = ' '

    for each_symbol in input_string:
        if each_symbol != ' ' and previous_symbol == ' ':
            each_symbol = each_symbol.upper()
        previous_symbol = each_symbol
        final_string += each_symbol
    print(final_string)


def main():
    # Initialization
    input_string = ''

    while not 0 < len(input_string) < 1000:
        input_string = input()

    problem_solution(input_string)


if __name__ == '__main__':
    main()
