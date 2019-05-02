""""HackerRank Maths 2 Find Angle MBC"""

import math

def problem_solution(ab, bc):
    # Task function
    mbc = math.degrees(math.atan2(ab, bc))
    print('{0:.0f}°'.format(mbc))


def main():
    # Initialization
    ab = float(input())
    bc = float(input())

    problem_solution(ab, bc)


if __name__ == '__main__':
    main()
