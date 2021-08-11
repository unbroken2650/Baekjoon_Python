import heapq
import sys

n = int(sys.stdin.readline().rstrip())

timetable = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timetable.sort(key=lambda x:x[0])

q = []
heapq.heappush(q, timetable[0][1])

for i in range(1, n) :
    if q[0] > timetable[i][0] :
        heapq.heappush(q, timetable[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, timetable[i][1])

print(len(q))
