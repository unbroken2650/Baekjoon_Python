import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt, tot = 0, 0

def dfs(cur):
    global cnt, tot
    if cur == N: return
    if tot + numbers[cur] == S:
        cnt += 1
    dfs(cur + 1)
    tot += numbers[cur]
    dfs(cur + 1)
    tot -= numbers[cur]


dfs(0)
print(cnt)
