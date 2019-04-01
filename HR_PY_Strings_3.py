# HackerRank Strings 3 String What's your name


def problem_solution(first_name, last_name):
    # Task function
    print('Hello {} {}! You just delved into python.'.
          format(first_name, last_name))


def main():
    # Initialization
    first_name = input().strip()
    last_name = input().strip()

    problem_solution(first_name, last_name)


main()
