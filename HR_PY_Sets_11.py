"""HackerRank Sets 11 Captains Room"""


def problem_solution(guests_rooms, size_of_group):
    # Task function
    rooms = set(guests_rooms)
    captain_room = ((sum(rooms) * size_of_group) - sum(guests_rooms)) // (size_of_group - 1)

    print(captain_room)


def main():
    # Initialization
    size_of_group = 0
    min_size = 0
    max_size = 1000

    while not size_of_group > min_size and size_of_group < max_size:
        size_of_group = int(input())

    guests_rooms = list(map(int, input().split()))
    problem_solution(guests_rooms, size_of_group)


if __name__ == '__main__':
    main()
