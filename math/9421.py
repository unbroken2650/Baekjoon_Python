#210829
import sys
from collections import deque
input = sys.stdin.readline


N = int(input().rstrip())
MAX = N

primes = [True for _ in range(MAX+1)]
for i in range(2, int(MAX**0.5+1)) :
    for j in range(i*2, MAX+1, i) :
        if not primes[j] : continue
        primes[j] = False #True : 소수, False : 합성수

for idx in range(2, len(primes)) :
    i = primes[idx]
    if not i :
        continue
    s = set()
    t = deque(str(idx))
    while True :
        tot = 0
        while t :
            tot += int(t.pop())**2
            #print(idx, tot)
        if tot == 1 :
            print(idx)
            break
        if tot in s : break
        else :
            s.add(tot)
            t = deque(str(tot))
