""""HackerRank Itertools 3 itertools.combinations()"""


from itertools import combinations


def problem_solution(A, k):
    # Task function
    k = int(k)
    list_A = [element for element in A]
    list_A.sort()
    for i in range(1, k + 1):
        for element in combinations(list_A, i):
            print(''.join(element))



def main():
    # Initialization
    A, k = input().upper().split()

    problem_solution(A, k)


if __name__ == '__main__':
    main()
