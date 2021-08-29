import sys

input = sys.stdin.readline

L, C = map(int, input().split())
alp = sorted(list(input().split()))
arr = []
check = [0 for _ in range(C)]

def dfs(len, idx):
    if len == L : #전체 개수 만족할 때
        con, vow = 0, 0
        for i in range(L) : #자음, 모음 개수 세고
            if arr[i] in 'aeiou' : vow += 1
            else : con += 1
        if vow >= 1 and con >= 2 : #만족하면 출력
            print(''.join(arr))
        return
    
    for i in range(idx, C) : #확인하지 않은 문자 추가하며 확인
        if check[i] == 0 :
            arr.append(alp[i])
            check[i] = 1
            dfs(len+1, i+1) 
            check[i] = 0
            del arr[-1]

dfs(0, 0)
