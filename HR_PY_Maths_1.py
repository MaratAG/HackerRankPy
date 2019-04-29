"""HackerRank Maths 1 Polar Coordinates"""
import cmath

def problem_solution(complex_number):
    # Task function
    print(abs(complex_number))
    print(cmath.phase(complex_number))


def main():
    # Initialization
    complex_number = complex(input())
    problem_solution(complex_number)


if __name__ == '__main__':
    main()
