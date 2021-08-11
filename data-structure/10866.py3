import sys


def push_front(q, i):
    q.insert(0, i)


def push_back(q, i):
    q.append(i)


def pop_front(q):
    if len(q) > 0:
        print(q[0])
        del q[0]
    else:
        print("-1")


def pop_back(q):
    if len(q) > 0:
        print(q[-1])
        del q[-1]
    else:
        print("-1")


def size(q):
    print(len(q))


def empty(q):
    if len(q) == 0: print("1")
    else: print("0")


def front(q):
    if len(q) > 0: print(q[0])
    else: print("-1")


def back(q):
    if len(q) > 0: print(q[-1])
    else: print("-1")


n = int(sys.stdin.readline().strip())
q = []

for _ in range(n):
    command = list(sys.stdin.readline().split())

    command_0 = command[0]

    if command_0 == "push_front":
        push_front(q, command[1])
    if command_0 == "push_back":
        push_back(q, command[1])    
    if command_0 == "pop_front":
        pop_front(q)
    if command_0 == "pop_back":
        pop_back(q)
    if command_0 == "size":
        size(q)
    if command_0 == "empty":
        empty(q)
    if command_0 == "front":
        front(q)
    if command_0 == "back":
        back(q)
