import sys

cnt = 0
rank = 0

# 값 입력받기
n, sc_song, p = map(int, sys.stdin.readline().split())
sc = list(map(int, sys.stdin.readline().split()))

# 기존 점수에 송유진의 점수 있는지 확인
for i in sc:
    if i == sc_song: cnt += 1

# 송유진의 점수 추가하고 내림차순 정렬
sc.append(sc_song)
sc.sort(reverse=True)

#랭크를 구하고 순위 안에 드는지 확인
rank = sc.index(sc_song)+cnt+1
if rank > p : print("-1")
else : print(rank-cnt)
