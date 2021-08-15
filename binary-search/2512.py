import sys
input = sys.stdin.readline

#변수 설정 및 입력
N = int(input().rstrip()) #지방의 수
budget_cand = list(map(int, input().split())) #예산요청
tot = int(input().rstrip()) #총 예산

#1 : 모든 요청이 배정될 수 있는 경우
if sum(budget_cand) == tot :
    print(max(budget_cand))
else : #2 : 모든 요청이 배정될 수 없는 경우
    start = 0
    end = max(budget_cand)
    while start <= end :
        cnt = 0
        mid = (start+end)//2
        for i in budget_cand :
            cnt += i if mid > i else mid
        if cnt <= tot :
            start = mid + 1
            ans = mid
        else : end = mid -1
    print(ans)
