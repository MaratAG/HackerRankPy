"""HackerRank Sets 12 Check Subset"""


def problem_solution(T):
    # Task function
    count = 0
    check_subset = []
    while count != T:
        count += 1
        len_A = int(input())
        set_A = set(map(int, input().split()))
        len_B = int(input())
        set_B = set(map(int, input().split()))
        check_subset.append(set_A <= set_B)

    for element in check_subset: print(element)


def main():
    # Initialization
    T = 0
    min_size = 0
    max_size = 21

    while not T > min_size and T < max_size:
        T = int(input())

    problem_solution(T)


if __name__ == '__main__':
    main()
