""""HackerRank Itertools 7 Maximize It!"""


from itertools import product


def problem_solution(N, M):
    # Task function
    results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
    print(max(results))


def main():
    # Initialization
    K, M = map(int, input().split())
    N = [list(map(int, input().split())) for _ in range(K)]
    problem_solution(N, M)


if __name__ == '__main__':
    main()
