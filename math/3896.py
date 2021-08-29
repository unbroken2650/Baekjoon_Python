#210829
import sys
input = sys.stdin.readline

N = int(input().rstrip())
MAX = 1299709
primes = [True for _ in range(MAX+1)]

for i in range(2, MAX+1) :
    for j in range(i*2, MAX+1, i) :
        if not primes[j] : continue
        primes[j] = False

for i in range(N) :
    t = int(input().rstrip())
    if primes[t] : 
        print(0)
        continue
    a, b = 0, 0
    for k in range(t, -1, -1) :
        if primes[k] :
            a = k
            break
    for k in range(t, MAX+1, 1) :
        if primes[k] :
            b = k
            break
    print(b-a)
    
