""""HackerRank Itertools 5 Compress the String!"""


from itertools import groupby


def problem_solution(A):
    # Task function
    for i, j in groupby(A):
        print('({}, {})'.format(len(list(j)), i), end= ' ')


def main():
    # Initialization
    A = input()

    problem_solution(A)


if __name__ == '__main__':
    main()
