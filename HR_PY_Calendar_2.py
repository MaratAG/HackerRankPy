"""  HR Task 2 Time Delta """


from datetime import datetime


def main():
    format_data = '%a %d %b %Y %H:%M:%S %z'

    n_tests = int(input())
    for _ in range(n_tests):
        time1 = datetime.strptime(input(), format_data)
        time2 = datetime.strptime(input(), format_data)
        print(int(abs(time2 - time1).total_seconds()))


if __name__ == '__main__':
    main()
