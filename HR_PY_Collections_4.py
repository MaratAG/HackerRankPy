"""  HR Task 4 Collections OrderedDict """


from collections import OrderedDict


def main():
    prices = OrderedDict()
    N = int(input())

    for _ in range(N):
        goods_and_price = input().split()
        goods = ' '.join(goods_and_price[:-1])
        price = int(goods_and_price[-1:][0])
        if goods not in prices.keys():
            prices[goods] = 0
        prices[goods] += price

    for key, value in prices.items():
        print('{} {}'.format(key, value))


if __name__ == '__main__':
    main()
