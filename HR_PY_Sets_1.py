# HackerRank Sets 1 Introduction to set!


def problem_solution(distinct_heights, N):
    # Task function
    Average = sum(distinct_heights) / len(distinct_heights)
    return Average


def main():
    # Initialization
    input_string = ''
    N = 0
    min_count = 0
    max_count = 100

    while not min_count < N <= max_count:
        N = int(input())

    distinct_heights = set(map(int, input().split()))

    print(problem_solution(distinct_heights, N))


if __name__ == '__main__':
    main()
