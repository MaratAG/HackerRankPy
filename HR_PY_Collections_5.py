"""  HR Task 5 Collections Deque """


from collections import deque


def main():
    deque_list = deque()
    N = int(input())

    for _ in range(N):
        command__and_arg = input().split()
        if command__and_arg[0] == 'append':
            deque_list.append(int(command__and_arg[1]))
        elif command__and_arg[0] == 'appendleft':
            deque_list.appendleft(int(command__and_arg[1]))
        elif command__and_arg[0] == 'pop':
            deque_list.pop()
        elif command__and_arg[0] == 'popleft':
            deque_list.popleft()

    for item in deque_list: print(item, end=' ')


if __name__ == '__main__':
    main()
