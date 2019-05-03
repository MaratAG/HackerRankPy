""""HackerRank Itertools 1 itertools.product()"""


from itertools import product


def problem_solution(A, B):
    # Task function
    for element in product(A, B):
        print(element, end=' ')



def main():
    # Initialization
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    problem_solution(A, B)


if __name__ == '__main__':
    main()
