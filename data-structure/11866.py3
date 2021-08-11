import sys
from collections import deque

n, k  = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])
ans = list()
k = k - 1
q.rotate(-k)
while q :
    ans.append(q.popleft())
    q.rotate(-k)

print("<", end="")
for i in range(len(ans)-1) :
    print(ans[i], end=", ")
print(ans[len(ans)-1], end=">")
