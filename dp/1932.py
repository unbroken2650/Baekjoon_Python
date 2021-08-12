import sys
input = sys.stdin.readline

#변수 설정 및 입력
n = int(input().rstrip())
tri = [0]
for _ in range(n):
    tri.append(list(map(int, input().split())))

#n이 1보다 크다면
if n > 1 :
    tri[2][0] += tri[1][0]
    tri[2][1] += tri[1][0]

    for i in range(3, n+1) :
        tri[i][0] += tri[i-1][0] #맨 왼쪽
        for j in range(1, i-1) :
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j]) #가운데
        tri[i][i-1] += tri[i-1][i-2] #맨 오른쪽


print(max(tri[n])) #모든 경로 중 가장 큰 값 출력
