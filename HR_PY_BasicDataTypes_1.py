# HackerRank Basic Data Types 1 List Comprehensions


def problem_solution(x, y, z, N):
    # Task function
    print([[i, j, k] for i in range(x + 1) for j
           in range(y + 1) for k in range(z + 1) if (i + j + k) != N])


def main():
    # Initialization
    x = int(input())
    y = int(input())
    z = int(input())
    N = int(input())

    problem_solution(x, y, z, N)


main()
