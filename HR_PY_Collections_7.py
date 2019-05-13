"""  HR Task 7 Collections Word Order """


from collections import Counter


def main():
    n_words = int(input())
    list_words = []

    for _ in range(n_words):
        list_words.append(input())
    count_of_words = Counter(list_words)

    print(len(count_of_words))
    for item in count_of_words.items(): print(item[1], end=' ')


if __name__ == '__main__':
    main()
