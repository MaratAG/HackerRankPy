# HackerRank Basic Data Types 4 Finding the percentage


def problem_solution(students_and_grades):
    # Task function
    name_of_students = input().strip()
    if name_of_students in students_and_grades.keys():
        grades_of_students = students_and_grades[name_of_students]
        average_mark_of_student = \
            sum(grades_of_students) / len(grades_of_students)
        print('{:.2f}'.format(average_mark_of_student))


def main():
    # Initialization
    N = 0
    students_and_grades = {}

    while not 1 < N < 11:
        N = int(input())

    for i in range(N):
        name_and_grades = list(input().strip().split())
        name = name_and_grades[0]
        grades = [float(name_and_grades[i])
                  for i in range(1, len(name_and_grades))]
        students_and_grades[name] = grades

    problem_solution(students_and_grades)


main()
