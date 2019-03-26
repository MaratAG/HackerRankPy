# HackerRank Introduction 3 Arithmetic Operators


def problem_solution(a, b):
    # Task function
    print(a + b)
    print(a - b)
    print(a * b)


def main():
    # Initialization
    a = 0
    b = 0
    n = 10 ** 10

    while (a < 1) or (a > n):
        a = int(input())

    while (b < 1) or (b > n):
        b = int(input())

    problem_solution(a, b)


main()
