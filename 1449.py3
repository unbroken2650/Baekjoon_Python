import sys

n, l  = map(int, sys.stdin.readline().split())
hole = list(map(int, sys.stdin.readline().split()))
cnt = 0
while hole :
    hole.sort()
    for i in hole :
        tmp_tape = [j for j in range(i, i+l, 1)]
        hole = list(set(hole) - set(tmp_tape))
        cnt += 1
        break


print(cnt)