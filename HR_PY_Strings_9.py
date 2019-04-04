# HackerRank Strings 9 Designer Door Mat


def problem_solution(current_string, N, M):
    # Task function
    symbol_of_mat = '.|.'
    for i in range(0, N - 1, 2):
        string_of_mat = symbol_of_mat * (1 + i)
        print(string_of_mat.center(M, '-'))

    print(current_string.center(M, '-'))

    for i in range(N - 1, 0, -2):
        string_of_mat = symbol_of_mat * (i - 1)
        print(string_of_mat.center(M, '-'))


def main():
    # Initialization
    current_string = 'WELCOME'
    N, M = map(int, input().split())

    problem_solution(current_string, N, M)


if __name__ == '__main__':
    main()
