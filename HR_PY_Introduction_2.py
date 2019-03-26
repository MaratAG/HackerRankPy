# HackerRank Introduction 2 Python If-Else


def problem_solution(n=0):
    # Task function
    result_of_solution = 'Weird'

    if (n % 2 == 0) and ((n > 1 and n < 6) or (n > 20)):
        result_of_solution = 'Not Weird'

    print(result_of_solution)


def main():
    # Initialization
    n = 0

    while (n < 1) or (n > 100):
        n = int(input())

    problem_solution(n)


main()
