# HackerRank Sets 2 No Idea!


def problem_solution(moodies, happy, unhappy):
    # Task function
    my_mood = 0

    for mood in moodies:
        if mood in happy:
            my_mood += 1
        elif mood in unhappy:
            my_mood -= 1

    return my_mood


def main():
    # Initialization
    m = 0
    n = 0
    min_count = 1
    max_count = 10 ** 9

    while not (min_count <= m <= max_count and min_count <= n <= max_count):
        m, n = map(int, input().split())

    moodies = map(int, input().split())
    happy = set(map(int, input().split()))
    unhappy = set(map(int, input().split()))

    print(problem_solution(moodies, happy, unhappy))


if __name__ == '__main__':
    main()
