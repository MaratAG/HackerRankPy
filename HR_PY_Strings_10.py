# HackerRank Strings 10 String Formatting


def problem_solution(n):
    # Task function
    width_of_string = len('{0:b}'.format(n))
    for i in range(1, n + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width_of_string))


def main():
    # Initialization
    n = 0

    while not 0 < n < 100:
        n = int(input())

    problem_solution(n)


if __name__ == '__main__':
    main()
