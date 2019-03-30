# HackerRank Basic Data Types 3 Nested Lists


def problem_solution(names_and_grades):
    # Task function
    grades = [i[1] for i in names_and_grades]
    grades.sort()

    second_lowest_mark = grades[0]
    for grade in grades:
        if grade > second_lowest_mark:
            second_lowest_mark = grade
            break

    names = [i[0] for i in names_and_grades if i[1] == second_lowest_mark]
    names.sort()
    for name in names:
        print(name)


def main():
    # Initialization
    N = 0
    names_and_grades = []

    while not 1 < N < 6:
        N = int(input())

    for i in range(N):
        name = input().strip()
        grade = float(input())
        names_and_grades.append([name, grade])

    problem_solution(names_and_grades)


main()
