# HackerRank Basic Data Types 6 Tuples


def problem_solution(members_of_tuple):
    # Task function
    current_tuple = tuple(members_of_tuple)
    print(hash(current_tuple))


def main():
    # Initialization
    N = 0
    members_of_tuple = []

    while N == 0:
        N = int(input())

    while not (len(members_of_tuple) == N):
        members_of_tuple = list(map(int, input().split()))

    problem_solution(members_of_tuple)


main()
