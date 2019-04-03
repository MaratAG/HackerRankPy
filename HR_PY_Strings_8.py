# HackerRank Strings 8 Text Wrap


def problem_solution(current_string, w):
    # Task function
    while len(current_string) > w:
        wrap_string = current_string[:w]
        current_string = current_string[w:]
        print(wrap_string)

    print(current_string)


def main():
    # Initialization
    current_string = ''
    w = 0

    while not 0 < len(current_string) <= 1000:
        current_string = input().strip()

    while not 0 < w < len(current_string):
        w= int(input())

    problem_solution(current_string, w)


if __name__ == '__main__':
    main()
