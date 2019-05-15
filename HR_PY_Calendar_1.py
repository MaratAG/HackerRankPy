"""  HR Task 1 Calendar Module """


import calendar


def main():
    mm, dd, yyyy = map(int, input().split())
    print(list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)])


if __name__ == '__main__':
    main()
