"""  HR Task 8 Piling Up! """


from collections import deque


def main():
    n_tests = int(input())

    for _ in range(n_tests):
        _ = input()
        side_lengths = deque(map(int, input().split()))
        result = 'Yes'
        if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
            result = 'No'

        print(result)


if __name__ == '__main__':
    main()
