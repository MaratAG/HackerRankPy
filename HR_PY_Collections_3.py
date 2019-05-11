"""  HR Task 3 Collections Counter """


from collections import Counter


def main():
    _ = int(input())
    all_sizes_of_shoes = Counter(map(int, input().split()))
    number_of_customers = int(input())
    value_of_rague = 0

    for _ in range(number_of_customers):
        size, price = map(int, input().split())
        if size in all_sizes_of_shoes.keys():
            if all_sizes_of_shoes[size] != 0:
                value_of_rague += price
                all_sizes_of_shoes[size] -= 1

    print(value_of_rague)


if __name__ == '__main__':
    main()
