""""HackerRank Maths 5 Power Mod power"""


def problem_solution(a, b, m):
    # Task function
    print(pow(a, b))
    print(pow(a, b, m))


def main():
    # Initialization
    a = int(input())
    b = int(input())
    m = int(input())

    problem_solution(a, b, m)


if __name__ == '__main__':
    main()
