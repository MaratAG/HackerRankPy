# HackerRank Strings 13 The Minion Game


def problem_solution(input_string):
    # Task function
    input_string = input_string.lower()
    winners_name = 'Stuart'
    winners_score = 0
    kevin_score = 0
    vowels = 'aeiou'

    for i in range(len(input_string)):
        scores = len(input_string) - i
        if input_string[i] in vowels:
            kevin_score += scores
        else:
            winners_score += scores

    if kevin_score == winners_score:
        print('Draw')
    else:
        if kevin_score > winners_score:
            winners_name = 'Kevin'
            winners_score = kevin_score

        print('{} {}'.format(winners_name, winners_score))


def main():
    # Initialization
    input_string = ''
    min_len = 0
    max_len = 10 ** 6

    while not min_len < len(input_string) <= max_len:
        input_string = input().lower()

    problem_solution(input_string)


if __name__ == '__main__':
    main()
