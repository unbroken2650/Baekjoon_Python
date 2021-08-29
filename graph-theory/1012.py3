import sys

# 변수 설정 및 입력
t = int(sys.stdin.readline().rstrip())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
# BFS 함수 설정
def bfs(tx, ty) :
    if tx <= -1 or ty <= -1 or tx >= m or ty >= n :
        return
    if baechu[tx][ty] == 0 :
        return
    baechu[tx][ty] = 0

    bfs(tx+1, ty)    
    bfs(tx-1, ty)
    bfs(tx, ty+1)
    bfs(tx, ty-1)

# 실행

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    baechu = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        baechu[y][x] = 1
    ans = 0
    for i in range(m) :
        for j in range(n) :
            if baechu[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
