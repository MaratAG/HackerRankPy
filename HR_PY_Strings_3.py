# HackerRank Strings 4 Mutations


def problem_solution(current_string, parametres):
    # Task function
    index_of_string = int(parametres[0])
    symbol_for_change = parametres[1]

    new_string = current_string[:index_of_string] + symbol_for_change + current_string[index_of_string + 1:]
    print(new_string)


def main():
    # Initialization
    current_string = input().strip()
    parametres = list(input().split())

    problem_solution(current_string, parametres)


main()
