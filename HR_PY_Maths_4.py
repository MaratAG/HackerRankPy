""""HackerRank Maths 4 Find Mod Divmod"""


def problem_solution(a, b):
    # Task function
    print(a // b)
    print(a % b)
    print(divmod(a, b))


def main():
    # Initialization
    a = int(input())
    b = int(input())

    problem_solution(a, b)


if __name__ == '__main__':
    main()
