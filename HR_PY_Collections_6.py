"""  HR Task 6 Collections Company Logo """


from collections import Counter


def main():
    name_of_company = list(input())
    count_of_symbols = Counter(name_of_company)
    maximize_symbols = sorted(count_of_symbols.items(), key=lambda x: (-x[1], x[0]))[:3]
    for symbol, value in maximize_symbols:
        print(symbol, value)


if __name__ == '__main__':
    main()
