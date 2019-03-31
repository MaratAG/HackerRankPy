# HackerRank Strings 2 String Split and Join


def problem_solution(current_string):
    # Task function
    join_string = '-'.join(current_string)
    print(join_string)


def main():
    # Initialization
    min_len_of_string = 0
    current_string = ''

    while not min_len_of_string < len(current_string):
        current_string = list(input().strip().split())

    problem_solution(current_string)


main()
