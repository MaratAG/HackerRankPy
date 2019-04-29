"""HackerRank Sets 10 Set Mutations"""


def problem_solution(set_A, number_of_other_sets):
    # Task function
    count_command = 0
    while not count_command == number_of_other_sets:
        count_command += 1
        cur_command = input().split()
        cur_set = set(map(int, input().split()))

        if cur_command[0] == 'intersection_update':
            set_A.intersection_update(cur_set)
        elif cur_command[0] == 'update':
            set_A.update(cur_set)
        elif cur_command[0] == 'symmetric_difference_update':
            set_A.symmetric_difference_update(cur_set)
        elif cur_command[0] == 'difference_update':
            set_A.difference_update(cur_set)

    print(sum(set_A))


def main():
    # Initialization
    number_of_elements_A = 0
    min_A = 0
    max_A = 1000

    number_of_other_sets = 0
    min_other_sets = 0
    max_otrher_sets = 100

    while not number_of_elements_A > min_A and number_of_elements_A < max_A:
        number_of_elements_A = int(input())

    set_A = set(map(int, input().split()))

    while not number_of_other_sets > min_other_sets and number_of_other_sets < max_otrher_sets:
        number_of_other_sets = int(input())

    problem_solution(set_A, number_of_other_sets)


if __name__ == '__main__':
    main()
