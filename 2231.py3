import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(n//2, n+1) :
    seng = list(map(int, str(i)))
    sm = sum(seng) + i
    if sm == n : ans = i ; break

print(ans if ans!=0 else 0)