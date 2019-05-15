"""  HR Task 1  Exceptions """


def main():

    n_tests = int(input())
    for _ in range(n_tests):

        try:
            a, b = map(int, input().split())
            print(a / b)
        except ValueError as e:
            print('Error Code: {}'.format(e))
        except ZeroDivisionError as e:
            print('Error Code: {}'.format(e))
        except TypeError as e:
            print('Error Code: {}'.format(e))


if __name__ == '__main__':
    main()
