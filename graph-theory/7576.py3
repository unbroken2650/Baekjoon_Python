import sys
from collections import deque

# 변수 설정 및 입력
n, m = map(int, sys.stdin.readline().split())
tomato = list()
for _ in range(m):
    tomato.append(list(map(int, sys.stdin.readline().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

# BFS 함수 설정
def bfs() :
    while q :
        a, b = q.popleft()
        for i in range(4) :
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<m and 0<=ny<n and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[a][b] + 1
                q.append([nx, ny])

# 익은 토마토의 좌표를 queue에 append
for i in range(m) :
    for j in range(n) :
        if tomato[i][j] == 1:
            q.append([i, j])

bfs()

no_tomato=False
res = -2

#익지 않은 토마토가 있는지 확인 / 없다면 날짜를 출력
for i in tomato :
    for k in i :
        if k == 0 :
            no_tomato = True
        res = max(res, k)

if no_tomato == True : #모두 익을 수 없을 때
    print(-1)
elif res == -1 : #이미 모두 익어있을 때
    print(0)
else : #모두 익을 수 있을 때
    print(res-1)
