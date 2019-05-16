"""  HR Task 2  Exceptions """

import re

def main():
    n_tests = int(input())
    for _ in range(n_tests):
        test_string = 'Python forever'
        regex = input()
        try:
            _ = re.search(regex, test_string)
            print(True)
        except:
            print(False)


if __name__ == '__main__':
    main()
