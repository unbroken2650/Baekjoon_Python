import sys
import heapq
# 변수 설정 및 입력
t = int(sys.stdin.readline().rstrip())
q = list()

for _ in range(t):
    c = int(sys.stdin.readline().rstrip())
    if c!=0 :
        heapq.heappush(q, c)
    else :
        if len(q) >0 :
            print(heapq.heappop(q))
        else : print(0)
