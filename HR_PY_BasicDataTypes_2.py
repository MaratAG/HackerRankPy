# HackerRank Basic Data Types 2 Find The Runner-Up Score


def problem_solution(A):
    # Task function
    A.sort()
    A.reverse()

    runner_up = A[0]
    for element_A in A:
        if element_A < runner_up:
            runner_up = element_A
            break
    print(runner_up)


def main():
    # Initialization
    n = 0
    A = []

    while (n < 2) or (n > 10):
        n = int(input())

    while len(A) != n:
        A = list(map(int, input().split()))

    problem_solution(A)


main()
