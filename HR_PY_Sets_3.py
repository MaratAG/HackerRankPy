"""HackerRank Sets 3 Symmetric Difference"""


def problem_solution(set_m, set_n):
    # Task function
    return [item for item in set_m.difference(set_n)]


def main():
    # Initialization
    m = 0
    n = 0
    set_m = set()
    set_n = set()
    difference_list = []

    while m <= 0:
        m = int(input())

    set_m = set(map(int, input().split()))

    while n <= 0:
        n = int(input())

    set_n = set(map(int, input().split()))

    difference_list += problem_solution(set_m, set_n)
    difference_list += problem_solution(set_n, set_m)

    difference_list.sort()
    for item in difference_list: print(item)


if __name__ == '__main__':
    main()
