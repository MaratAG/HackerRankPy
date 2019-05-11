"""  HR Task 1 Collections Collections.namedtuple() """


from collections import namedtuple


def main():
    students = []
    N = int(input())
    columns = input().upper()

    Student = namedtuple('Student', columns)

    for _ in range(N):
        txt_student = input().split()
        students.append(Student(*txt_student))

    print('{0:.2f}'.format(sum([int(std.MARKS) for std in students]) / len(students)))


if __name__ == '__main__':
    main()
