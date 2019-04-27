"""HackerRank Sets 4 Set.add()"""


def problem_solution(N):
    # Task function
    country = 0
    countries = set()
    while not country == N:
        country += 1
        countries.add(input())
    return len(countries)


def main():
    # Initialization
    N = 0
    min_n = 0
    max_n = 1000

    while not N > min_n and N < max_n:
        N = int(input())

    print(problem_solution(N))


if __name__ == '__main__':
    main()
