"""HackerRank Sets 13 Check Strict Superset"""


def problem_solution(set_A, N):
    # Task function
    count = 0
    its_superset = True
    while count != N:
        count += 1
        set_B = set(map(int, input().split()))
        its_subset = set_B <= set_A
        if its_subset is False and its_superset is True:
            its_superset = False

    print(its_superset)


def main():
    # Initialization
    N = 0
    min_size = 0
    max_size = 21

    set_A = set(map(int, input().split()))

    while not N > min_size and N < max_size:
        N = int(input())

    problem_solution(set_A, N)


if __name__ == '__main__':
    main()
