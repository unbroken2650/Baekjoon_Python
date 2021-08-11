# 2021/07/13 22:44
# https://www.acmicpc.net/source/30982726

n = int(input())
tile = [0, 1]
i = 1 ; j = 1
if n == 1 : ans = 4
else :
    n -= 1
    for _ in range(n) :
        tile.append(tile[-1] + tile[-2])
    ans = tile[-1]*4 + tile[-2]*2
print(ans)
