"""  HR Task 2 Time Delta """


import calendar


def main():
    mm, dd, yyyy = map(int, input().split())
    print(list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)].upper())


if __name__ == '__main__':
    main()
