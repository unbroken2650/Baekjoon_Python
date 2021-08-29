import sys
input = sys.stdin.readline

n = int(input().rstrip())
rope = sorted([int(input().rstrip()) for _ in range(n)], reverse=True)
ans = 0
for i in range(n) :
    if rope[i] * (i+1) > ans:
        ans = rope[i] * (i+1)   
print(ans)
