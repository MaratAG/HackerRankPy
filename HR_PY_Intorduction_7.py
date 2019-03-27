# HackerRank Introduction 7 Print Function


def problem_solution(N):
    # Task function
    print(*range(1, N + 1), sep='')


def main():
    # Initialization
    N = 0

    while (N < 1):
        N = int(input())

    problem_solution(N)


main()
