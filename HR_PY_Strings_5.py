# HackerRank Strings 5 Find a string


def problem_solution(current_string, sub_string):
    # Task function
    start_symbol = 0
    count_of_enter = 0

    while not start_symbol == -1:
        start_symbol = current_string.find(sub_string, start_symbol)
        if not start_symbol == -1:
            current_string = current_string[start_symbol+1:]
            start_symbol = 0
            count_of_enter += 1

    return count_of_enter


def main():
    # Initialization
    current_string = input().strip()
    sub_string = input().strip()

    print(problem_solution(current_string, sub_string))


if __name__ == '__main__':
    main()
