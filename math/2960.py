import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list()
primes = [True for _ in range(N+1)]

for i in range(2, N+1) :
    if primes[i] and len(nums) < K:
        nums.append(i)
    for j in range(i*2, N+1, i) :
        if not primes[j] : continue
        primes[j] = False
        if len(nums) < K :
            nums.append(j)
        else :
            break
    if len(nums) == K :
        break
print(nums[-1])

    
