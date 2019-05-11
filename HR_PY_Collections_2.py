"""  HR Task 2 Collections DefaultDict Tutorial """


from collections import defaultdict


def main():
    words = defaultdict(list)
    search_words = []
    n, m = map(int, input().split())
    for i in range(n):
        word = input()
        words[word].append(str(i + 1))

    for i in range(m):
        search_words.append(input())

    for search_word in search_words:
        if search_word in words:
            print(' '.join(words[search_word]))
        else:
            print(-1)


if __name__ == '__main__':
    main()
