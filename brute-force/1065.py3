import sys
input = sys.stdin.readline

n = int(input().rstrip())
tmp = ''
cnt = 0
if n < 100 : #n이 한 자리나 두 자리라면 무조건 등차수열을 이룸
    print(n)
else :
    for i in range(99, n+1) : #백의 자리&십의 자리의 차이와 십의 자리&일의 자리의 차이가 같다면 cnt++
        h, t, o = i//100, i%100//10, i%10 
        if h-t == t-o :
            cnt +=1
    print(99+cnt)
