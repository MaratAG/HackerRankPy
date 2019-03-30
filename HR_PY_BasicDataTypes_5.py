# HackerRank Basic Data Types 5 Lists


def problem_solution(commands):
    # Task function
    prepare_list = []
    for current_command in commands:
        command_text = current_command[0].strip()
        if len(current_command) > 1:
            argument_1 = int(current_command[1])
        if len(current_command) > 2:
            argument_2 = int(current_command[2])

        if command_text == 'insert':
            prepare_list.insert(argument_1, argument_2)
        elif command_text == 'print':
            print(prepare_list)
        elif command_text == 'remove':
            prepare_list.remove(argument_1)
        elif command_text == 'append':
            prepare_list.append(argument_1)
        elif command_text == 'sort':
            prepare_list.sort()
        elif command_text == 'pop':
            prepare_list.pop()
        elif command_text == 'reverse':
            prepare_list.reverse()


def main():
    # Initialization
    N = 0
    commands = []

    while N == 0:
        N = int(input())

    for i in range(N):
        add_command = list(input().strip().split())
        commands.append(add_command)

    problem_solution(commands)


main()
