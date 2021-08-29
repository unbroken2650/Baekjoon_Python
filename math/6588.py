#210829
import sys
input = sys.stdin.readline


test = []
while True :
    t = int(input().rstrip())
    if t ==0 : break
    test.append(t)

MAX = max(test)
primes = [True for _ in range(MAX+1)]
for i in range(2, int(MAX**0.5)+1) :
    for j in range(i*2, MAX+1, i) :
        if not primes[j] : continue
        primes[j] = False #True : 소수, False : 합성수

for idx in range(len(test)) :
    i = test[idx]
    find = False
    for t in range(3, i, 2) :
        if primes[t] and primes[i-t] and (i-t)%2 != 0:
            print("%d = %d + %d" %(i, t, i-t))
            find = True
            break
    if not find : print("Goldbach's conjecture is wrong.")
