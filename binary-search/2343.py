import sys

input = sys.stdin.readline

#변수 설정 및 입력
N, M = map(int, input().split())  #레슨의 수, 블루레이의 수
lesson = list(map(int, input().split()))  #레슨 길이
#한 테이프의 길이에 대해 이분 탐색
ans = sum(lesson)
start = 0
end = sum(lesson)
while start <= end:
    blue = [0 for _ in range(M)]
    mid = (start + end) // 2
    i = 0
    p = True
    for les in lesson:
        if blue[i] + les > mid:
            i = i + 1
        if i == M:
            p = False
            break
        blue[i] += les
    if i != M : p = True
    if p:
        end = mid - 1
        ans = min(ans, max(blue))
    else:
        start = mid + 1
print(ans)
