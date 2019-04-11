# HackerRank Strings 11 Alphabet Rangoli
import string


def problem_solution(n):
    # Task function
    alpha = string.ascii_lowercase

    list_of_symbols = []
    for i in range(n):
        current_string = '-'.join(alpha[i:n])
        list_of_symbols.append((current_string[::-1] +
                                current_string[1:]).center(4 * n - 3, '-'))

    print('\n'.join(list_of_symbols[:0:-1] + list_of_symbols))


def main():
    # Initialization
    n = 0

    while not 0 < n < 27:
        n = int(input())

    problem_solution(n)


if __name__ == '__main__':
    main()
