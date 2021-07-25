import sys


def push(q, i):
    q.append(i)


def pop(q):
    if len(q) > 0:
        print(q[0])
        q.remove(q[0])
    else:
        print("-1")


def size(q):
    print(len(q))


def empty(q):
    if len(q) == 0: print("1")
    else: print("0")


def back(q):
    if len(q) > 0: print(q[-1])
    else: print("-1")


def front(q):
    if len(q) > 0: print(q[0])
    else: print("-1")


n = int(sys.stdin.readline().strip())
q = []

for _ in range(n):
    command = list(sys.stdin.readline().split())

    command_0 = command[0]

    if command_0 == "push":
        push(q, command[1])
    if command_0 == "pop":
        pop(q)
    if command_0 == "size":
        size(q)
    if command_0 == "empty":
        empty(q)
    if command_0 == "front":
        front(q)
    if command_0 == "back":
        back(q)
