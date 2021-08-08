#18352 by dijkstra algorithm
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)

def get_smaller_node() :
    min_value = INF
    index = 0
    for i in range(n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index  = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j] = 1
    for i in range(n-1) :
        now = get_smaller_node()
        visited[now] = True
        for j in graph[now] :
            cost = distance[now] + 1
            if cost < distance[j] :
                distance[j] = cost

dijkstra(x)

no_node = True
for i in range(n+1) :
    if distance[i] == k :
        no_node = False
        print(i)
if no_node : print(-1)