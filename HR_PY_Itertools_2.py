""""HackerRank Itertools 2 itertools.permutations()"""


from itertools import permutations


def problem_solution(A, k):
    # Task function
    list_A = [element for element in A]
    list_A.sort()
    for element in permutations(list_A, int(k)):
        print(''.join(element))



def main():
    # Initialization
    A, k = input().upper().split()

    problem_solution(A, k)


if __name__ == '__main__':
    main()
