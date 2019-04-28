"""HackerRank Sets 6 Set.union() operation"""


def problem_solution(set_n, set_b):
    # Task function
    print(len(set_n.union(set_b)))


def main():
    # Initialization
    n = 0
    b = 0
    min_nb = 0
    max_nb = 1000

    while not n > min_nb and n < max_nb:
        n = int(input())

    set_n = set(map(int, input().split()))

    while not b > min_nb and b < max_nb:
        b = int(input())

    set_b = set(map(int, input().split()))

    problem_solution(set_n, set_b)


if __name__ == '__main__':
    main()
