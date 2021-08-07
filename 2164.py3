import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque(range(1, n+1))

while len(q) > 1 :
    q.popleft()
    q.append(q.popleft())
print(q[0])
