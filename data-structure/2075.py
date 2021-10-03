import sys
import heapq
from heapq import merge
MAX = int(-1e9)
input = sys.stdin.readline

N = int(input().rstrip())
table = [MAX for _ in range(N)]

for i in range(N):
    inp = list(map(int, input().split()))
    for j in inp:
        heapq.heappush(table, j)
    for j in range(N):
        heapq.heappop(table)

print(heapq.heappop(table))
