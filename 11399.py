# 2021/07/13 23:35
# https://www.acmicpc.net/source/30985292

def sum_list(tms, a, b) :
    tot = 0
    for i in range(a, b+1):
        tot += tms[i]
    return tot

ppl = int(input())
times = list(map(int, input().split()))
ans = 0

times.sort()
for i in range(0,ppl) :
    ans += sum_list(times, 0, i)

print(ans)