""""HackerRank Itertools 4 itertools.combinations_with_replacement()"""


from itertools import combinations_with_replacement


def problem_solution(A, k):
    # Task function
    k = int(k)
    list_A = [element for element in A]
    list_A.sort()
    for element in combinations_with_replacement(list_A, 2):
        print(''.join(element))



def main():
    # Initialization
    A, k = input().upper().split()

    problem_solution(A, k)


if __name__ == '__main__':
    main()
