# HackerRank Strings 1 Swap Case


def problem_solution(current_string):
    # Task function
    swap_string = ''
    for current_symbol in current_string:
        if current_symbol.isupper():
            swap_symbol = current_symbol.lower()
        else:
            swap_symbol = current_symbol.upper()
        swap_string += swap_symbol

    print(swap_string)


def main():
    # Initialization
    min_len_of_string = 0
    max_len_of_string = 1000
    current_string = ''

    while not min_len_of_string < len(current_string) <= max_len_of_string:
        current_string = input().strip()

    problem_solution(current_string)


main()
