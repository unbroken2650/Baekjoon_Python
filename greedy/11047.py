# 2021/07/13 23:43
# https://www.acmicpc.net/source/30985626

n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n) :
    coin.append(int(input()))
coin.sort(reverse = True)

for i in coin :
    if k < i : continue
    tgt = (k//i)*i
    cnt += k//i
    k -= tgt

print(cnt)
