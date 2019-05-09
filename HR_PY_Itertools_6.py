""""HackerRank Itertools 6 Iterables and iterators"""


from collections import defaultdict
from itertools import combinations


def problem_solution(A, N, K):
    # Task function
    dict_a = defaultdict(list)
    list_index = []

    for index, symbol_A in enumerate(A):
        list_index.append(index)
        if symbol_A == 'a':
            dict_a['a'].append(index)

    count = 0
    list_combinations = list(combinations(list_index, K))
    print(dict_a['a'])
    print(list_combinations)
    for element in list_combinations:
        for tulip_element in element:
            if tulip_element in dict_a['a']:
                count += 1
                break

    print('{0:.3f}'.format(count / len(list_combinations)))


def main():
    # Initialization
    N = int(input())
    A = input().split()
    K = int(input())

    problem_solution(A, N, K)


if __name__ == '__main__':
    main()
