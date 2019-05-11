""""HackerRank Itertools 7 Maximize It!"""


from itertools import product

def problem_solution(N):
    # Task function
    print(N)


def main():
    # Initialization
    K, M = map(int, input().split())
    N = (list(map(int, input().split())) for _ in range(K))

    problem_solution(N)


if __name__ == '__main__':
    main()
