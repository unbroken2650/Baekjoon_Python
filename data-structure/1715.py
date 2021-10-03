import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
nums = []
tot = 0

for _ in range(N):
    heapq.heappush(nums, int(input().rstrip()))
for _ in range(N):
    if len(nums) == 2:
        tot += sum(nums)
        break
    elif len(nums) == 1:
        break
    else:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        heapq.heappush(nums, a+b)
        tot += a+b
print(tot)
