import sys

input = sys.stdin.readline

#변수 설정 및 입력
nhome, nmachine = map(int, input().split())  #집의 개수, 공유기의 개수
xy = list(int(input().rstrip()) for _ in range(nhome))  #집의 좌표

#집의 좌표 정렬
xy = sorted(xy)

#공유기 사이의 거리 dist로 이분 탐색
start = 1
end = xy[-1]
ans = xy[-1] - xy[0]
while (start <= end):
    dist = (start + end) // 2
    installed = xy[0]
    cnt = 1
    for i in range(1, len(xy)):
        if xy[i] - installed >= dist:
            cnt += 1
            installed = xy[i]        

    if cnt < nmachine:  #집이 부족한 경우 -> 거리 줄이기
        end = dist - 1
    else:
        start = dist + 1
        ans = dist

print(ans)
