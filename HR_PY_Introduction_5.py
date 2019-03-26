# HackerRank Introduction 5 Loops


def problem_solution(N):
    # Task function
    for i in range(N):
        print(i ** 2)


def main():
    # Initialization
    N = 0

    while (N < 1) or (N > 20):
        N = int(input())

    problem_solution(N)


main()
