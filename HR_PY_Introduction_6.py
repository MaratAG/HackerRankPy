# HackerRank Basic Data Types 1 List Comprehensions


def problem_solution(year):
    # Task function
    year_is_leap = False

    if (year % 4 == 0):
        year_is_leap = True
        if (year % 100 == 0) and (year % 400 != 0):
            year_is_leap = False

    return year_is_leap


def main():
    # Initialization
    year = 0

    while (year < 1900) or (year > 10 ** 5):
        year = int(input())

    print(problem_solution(year))


main()
