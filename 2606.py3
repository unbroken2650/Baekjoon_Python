import sys

def dfs(graph, t, visited) :
    visited[t] = True
    for i in graph[t] :
        if not visited[i] :
            dfs(graph, i, visited)


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
net = list()
com = [[] for _ in range(n+1)]

v = [False] * (n+1)
for _ in range(m) :
    net.append(list(map(int, sys.stdin.readline().split())))

for i in net :
    com[i[0]].append(i[1])
    com[i[1]].append(i[0])
dfs(com, 1, v)

cnt = 0
for i in v :
    if i == True :
        cnt += 1
print(cnt-1)