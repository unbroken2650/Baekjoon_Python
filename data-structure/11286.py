import sys
import heapq

input = sys.stdin.readline

nums = []

N = int(input().rstrip())
for _ in range(N):
    n = int(input().rstrip())
    if n == 0:
        if len(nums) != 0:
            print(heapq.heappop(nums)[1])
        else:
            print(0)
    else:
        heapq.heappush(nums, [abs(n), n])
