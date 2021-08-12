import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
#변수 설정 및 입력
    #정점, 간선
V, E = map(int, input().split())
start = int(input().rstrip())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

    #간선 정보
for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(s) :
    q = []
    #시작 노드 초기화
    distance[s] = 0
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 pop
        dist, now = heapq.heappop(q)
        #이미 최단 거리라면 continue
        if distance[now] < dist :
            continue
        #주변 노드들에 대해 체크
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, V+1) :
    print(distance[i] if distance[i]!= INF else "INF")
