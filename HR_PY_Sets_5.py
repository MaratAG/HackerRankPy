"""HackerRank Sets 5 Set.discard(), remove()&pop()"""


def problem_solution(my_set, N):
    # Task function
    count_command = 0
    while not count_command == N:
        count_command += 1
        cur_command = input().split()
        if cur_command[0] == 'pop':
            my_set.pop()
        elif cur_command[0] == 'remove' and len(cur_command) == 2:
            my_set.remove(int(cur_command[1]))
        elif cur_command[0] == 'discard' and len(cur_command) == 2:
            my_set.discard(int(cur_command[1]))
        print(my_set)

    print(sum(my_set))


def main():
    # Initialization
    n = 0
    N = 0
    min_n = 0
    max_n = 20

    while not n > min_n and n < max_n:
        n = int(input())

    my_set = set(map(int, input().split()))

    while not N > min_n and N < max_n:
        N = int(input())

    problem_solution(my_set, N)


if __name__ == '__main__':
    main()
