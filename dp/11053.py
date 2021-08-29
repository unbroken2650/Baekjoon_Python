import sys
input = sys.stdin.readline

#변수 설정 및 입력
N = int(input().rstrip())
inp = list(map(int, input().split()))
dp = [0 for _ in range(N)]

#DP
for i in range(N) : #모든 원소들 각각
    for k in range(i) : #마지막 원소가 되었을 때 최장 증가 부분수열의 길이 구하기
        if inp[i] > inp[k] and dp[i] < dp[k] : #전 숫자보다 크고, 전 숫자까지 수열이 이어진다면
            dp[i] = dp[k]
    dp[i] += 1

print(max(dp))
